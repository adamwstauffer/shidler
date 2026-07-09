"""Shared zip-extraction helper for the BUS-629 grading scripts.

`zipfile.ZipFile.extractall()` does not validate member paths, so a zip
entry named e.g. `../../evil` would write outside the destination directory
("zipslip"). The submission zips come from the LMS export, which in turn
bundles student-uploaded files — treat them as untrusted.

`safe_extractall()` validates every member name resolves to a path strictly
inside `dest` before extracting, and refuses absolute paths.
"""
from __future__ import annotations

import zipfile
from pathlib import Path


def safe_extractall(zf: zipfile.ZipFile, dest: Path) -> None:
    """Extract `zf` into `dest`, refusing any member that would escape.

    Raises `ValueError` on the first unsafe member; nothing is extracted in
    that case (we validate the whole namelist before unpacking).
    """
    dest_resolved = Path(dest).resolve()
    for name in zf.namelist():
        # Reject absolute paths and Windows drive-letter paths outright.
        if name.startswith(("/", "\\")) or (len(name) >= 2 and name[1] == ":"):
            raise ValueError(f"unsafe zip member (absolute path): {name!r}")
        target = (dest_resolved / name).resolve()
        try:
            target.relative_to(dest_resolved)
        except ValueError:
            raise ValueError(
                f"unsafe zip member (escapes destination): {name!r}"
            ) from None
    zf.extractall(dest)
