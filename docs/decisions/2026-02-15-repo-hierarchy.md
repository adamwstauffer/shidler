# SHIDLER PORTFOLIO & COURSE MATERIALS REPOSITORY
## Directory and File Hierarchy Documentation

**Prepared by:** Adam W. Stauffer
**Date:** February 15, 2026
**Purpose:** Document the logical organization and purpose of all directories, subdirectories, and key files in the shidler repository

---

## 1. REPOSITORY OVERVIEW

This repository serves as a unified portfolio and course materials hub for Shidler College of Business courses taught by Adam W. Stauffer. The structure is designed for:

* **Course Documentation** – Syllabi, learning objectives, and course frameworks
* **Project Management** – Student assignment templates, rubrics, and deliverable specifications
* **Asset Management** – Branded materials, templates, and archive of past work
* **Professional Portfolio** – Bio, resume, and work samples

---

## 2. ROOT-LEVEL DIRECTORIES

### `/BUS-314-International-Business-Finance/`
**Purpose:** Materials for BUS 314 - International Business Finance (undergraduate course)

**Key Contents:**
- `README.md` – Course syllabus and overview
- `accounting-ratios/` – Multi-stage project on financial ratio analysis using Excel
  - `_templates/excel/` – Skeleton templates and automated generation scripts
  - `archive/` – Specs, prompts, analysis, and deliverables from past iterations
- `_spreadsheets/` – Master financial analysis tools and templates

**Project Structure:** Each project follows a 5-stage workflow (memo → spec → excel → prompt engineering → final recommendation)

---

### `/BUS-313-Global-Business-Environment/`
**Purpose:** Materials for BUS 313 - The Economic and Financial Environment of Global Business (undergraduate course)

**Key Contents:**
- `README.md` – Course overview and syllabus
- `extra-credit.md` – Optional assignments and enrichment activities

**Note:** This course emphasizes trade theory, international economics, and geopolitical case studies. Project deliverables follow the GitHub-based workflow with AI integration.

---

### `/BUS-620-Micro-And-Macro-Economics/`
**Purpose:** Materials for BUS 620 - Micro- and Macro-Economic Foundations for Managers (MBA course)

**Key Contents:**
- `README.md` – MBA course syllabus and framework
- `team-project/` – Guidelines for team case study presentations on AI, climate change, and geopolitics
- `individual-project/` – Individual research paper guidelines with peer-review rubrics

**Pedagogical Focus:** Integration of economic theory with geopolitics and business strategy. Heavy use of case studies and AI-assisted analysis.

---

### `/FIN-321-International-Finance/`
**Purpose:** Materials for FIN 321 - International Business Finance (upper-level undergraduate course)

**Key Contents:**
- `README.md` – Course syllabus and learning objectives
- `project-fx-hedging/` – Multi-stage FX risk management project
  - `_templates/excel/` – Hedging calculation templates
  - Stage assignments (1–5) covering memo, spec, Excel build, prompt engineering, and final recommendations
- `archive/` – Past project specifications, analyses, and deliverables

**Project Focus:** Practical application of forward contracts, options, and hedging strategies in multinational business contexts.

---

## 3. SUPPORTING ROOT-LEVEL DIRECTORIES

### `/_archive/`
**Purpose:** Historical materials, deprecated assignments, and past versions of courses

**Contents:**
- Old course iterations
- Deprecated Excel models
- Legacy project rubrics
- Archived student work (anonymized)

---

### `/docs/`
**Purpose:** Centralized documentation hub containing institutional documentation, reusable templates, and brand guidelines

**Key Subdirectories:**

#### `docs/decisions/`
Strategic and administrative decision memos being reviewed, discussed, and refined for organizational direction. These memos inform the development of plans, specifications, and course materials.

**Contents:**
- `2026-02-15-repo-hierarchy.md` – (This document) Comprehensive guide to directory structure
- Additional strategic memos on pedagogical approaches, course redesign, and organizational initiatives

#### `docs/templates/`
Reusable templates for assignments, projects, and professional materials.

**Contents:**
- `memo-template.md` – Template for memo writing stage
- `spec-template.md` – Template for specification/planning stage
- `case-brief-template.md` – Template for case analysis briefs
- `risk-memo-template.md` – Template for risk analysis memos
- `prompt-log-template.md` – Template for logging AI prompts
- Completed examples (e.g., `spec-example-interest-rate-parity.md`)
- `bio-and-resume/` – Professional bio and resume templates
  - `bio/` – Biography template and samples
  - `resume/` – Resume/CV template and samples

#### `docs/_branding/`
University of Hawaiʻi at Mānoa and Shidler College of Business brand guidelines and design system.

**Contents:**
- `design.json` – Design token system (colors, typography, spacing, etc.)
- `design-system.html` – Visual reference guide for brand standards
- Brand colors, typography standards, and logo usage guidelines

#### `docs/` (General Guides)
- `ai-usage-guidelines.md` – Guidelines for integrating AI tools into coursework
- `writing-style-guide.md` – Institutional writing standards
- `reproducibility-playbook.md` – Guidelines for reproducible course materials

---

### `/notes/`
**Purpose:** Personal research notes, reading summaries, and intellectual development

**Contents:**
- Notes on economic theory, finance, and geopolitics
- Research summaries for course development
- Ideas for future course content

---

## 4. ROOT-LEVEL FILES

### `README.md`
**Purpose:** Main repository overview and entry point

**Contents:**
- Brief description of the repository
- Links to major course directories
- Getting started instructions

---

### `BIO.md`
**Purpose:** Consolidated instructor biography (single source of truth)

**Contents:**
- Professional background and credentials
- Career highlights (Wharton MBA, CFA, fintech experience, etc.)
- Contact information

**Design Rationale:** Eliminates redundancy by centralizing instructor bio. All course READMEs link to this file with `[BIO.md](../BIO.md)`.

---

### `.claude.json`
**Purpose:** Claude Code configuration file for IDE integration

**Contents:**
- Claude-specific settings and hook configurations
- Repository rules and automation settings

---

### `.git/` and `.gitignore`
**Purpose:** Git version control system files

**Contents:**
- Full git history of the repository
- Staging area and local configuration
- `.gitignore` to exclude sensitive files and build artifacts

---

### `_claude/` directory
**Purpose:** Claude Code workspace configuration

**Contents:**
- Workspace settings
- Custom hooks for linting and formatting

---

## 5. DIRECTORY NAMING CONVENTIONS

### Course Directories
All course directories follow the pattern: `[COURSE-CODE]-[Descriptive-Title]`

Examples:
- `BUS-314-International-Business-Finance`
- `BUS-620-Micro-And-Macro-Economics`
- `FIN-321-International-Finance`

**Rationale:**
* Course code enables easy identification
* Descriptive title provides context without opening files
* Consistent capitalization (PascalCase with hyphens) improves readability
* Alphabetical sorting groups courses by code

### Internal Project Directories
Within each course, project subdirectories follow a clear naming convention:

- `project-[project-name]/` – Active project with latest materials
- `archive/` – Historical versions and past deliverables
- `_templates/` – Reusable templates with underscore prefix (convention for tooling)
- `_spreadsheets/` – Supporting Excel models and calculations

### Special Directories
Prefixed with `_` to denote system/organizational directories:
- `_archive/` – Historical materials and deprecated courses
- `_claude/` – IDE-specific configuration
- `docs/_branding/` – Brand assets and design system
- `docs/decisions/` – Strategic decision memos
- `docs/templates/` – Reusable templates across all courses

---

## 6. FILE ORGANIZATION WITHIN PROJECTS

### Standard Project Workflow
Each major project follows this file structure:

```
project-[name]/
├── README.md                          # Assignment brief & learning objectives
├── stage1-memo-assignment.md          # Memo writing stage
├── stage2-spec-assignment.md          # Project specification/planning
├── stage3-excel-build-assignment.md   # Spreadsheet/quantitative modeling
├── stage4-prompt-engineering.md       # AI integration and prompt design
├── stage5-final-rec.md                # Final synthesis and recommendations
├── template-memo.md                   # Template for stage 1 deliverable
├── template-spec.md                   # Template for stage 2 deliverable
├── _templates/
│   └── excel/
│       ├── README.md                  # Instructions for template use
│       └── [Model].xlsx               # Skeleton Excel workbook
└── archive/
    ├── specs/
    ├── prompts/
    ├── analysis/
    └── deliverables/
```

### README.md Files (Course-Level)
Located at `[Course-Directory]/README.md`, each course README contains:

1. **Course Header** – Title and institutional affiliation
2. **Course Overview** – 2–3 sentence description of content and focus
3. **Instructor** – Name, email, and link to `BIO.md`
4. **Learning Objectives / Topics** – Core competencies and subject matter
5. **Course Outline** – General progression through topics (no specific dates)
6. **Skills Gained** – Workplace-ready competencies developed
7. **Grading** – Grading breakdown (table format)
8. **Grading Components** – Detailed descriptions of each assessment
9. **AI Use Policy** – Guidelines for AI tools in coursework
10. **Campus Policies** – Disability accommodations, academic honesty, etc.

**Design Rationale:** This standardized structure makes courses comparable and maintainable, while removing time-sensitive information (dates, room numbers, specific schedules).

---

## 7. VERSIONING AND ARCHIVES

### Version Control Strategy
- **Active Materials** – Stored in project directories with clear stage labels
- **Historical Materials** – Moved to `archive/` subdirectories within projects
- **Deprecated Courses** – Moved to root-level `_archive/` directory

### Archive Subdirectories
Within projects, `archive/` contains:
- `specs/` – Past project specifications
- `prompts/` – AI prompt logs and engineering notes
- `analysis/` – Student work samples and analysis
- `deliverables/` – Template deliverables from past semesters

---

## 8. SPECIAL FILES AND THEIR PURPOSES

### `.md` (Markdown) Files
- **`README.md`** – Main documentation for each directory
- **`assignment-*.md`** – Assignment instructions for specific stages
- **`template-*.md`** – Templates for deliverables
- **`*-memo.md`** – Memo templates and samples
- **`*-spec.md`** – Project specification templates

### `.xlsx` (Excel) Files
- **Naming:** `[Project-Name]-[Purpose].xlsx` or `[Project-Name]-MASTER.xlsx`
- **Purpose:** Financial models, calculations, scenario analysis
- **Location:** `_spreadsheets/` or `_templates/excel/`

### `.json` Configuration Files
- **`.claude.json`** – Claude Code environment settings
- **`.gitignore`** – Git exclusion rules
- Purpose: System configuration and tooling

---

## 9. NAVIGATION AND CROSS-LINKING

### Link Structure
- **Internal Links:** Use relative paths (e.g., `../BIO.md` for parent directory)
- **Cross-Course Links:** Link to projects in other courses via relative paths
- **External Links:** Use full URLs for university resources and external sites

### Directory Traversal
- Course directories contain project subdirectories
- Projects reference course-specific templates via `_templates/` subdirectories
- All projects can reference root-level `BIO.md`
- All courses can reference reusable templates in `docs/templates/`
- All materials can reference brand guidelines in `docs/_branding/`
- All stakeholders can reference decisions in `docs/decisions/`

---

## 10. RECOMMENDATIONS FOR MAINTENANCE

### When Adding New Courses
1. Create directory: `[CODE]-[Descriptive-Title]` (matching capitalization)
2. Add `README.md` following the standard template
3. Create project subdirectory if applicable: `project-[name]/`
4. Include 5-stage workflow files if multi-phase project
5. Create `archive/` subdirectory for future versions

### When Updating Materials
1. Use `archive/` subdirectories to preserve past versions
2. Update `README.md` with current course structure (no specific dates)
3. Maintain consistent file naming and capitalization
4. Use descriptive file names that indicate purpose and stage

### Git Commit Messages
- Include directory/file names: "Update FIN-321 project templates"
- Reference specific changes: "Add course outline section to BUS-620 README"
- Include session ID for traceability

---

## 11. QUICK REFERENCE: COMMON PATHS

| Item | Path |
|------|------|
| Instructor Bio | `/BIO.md` |
| Course READMEs | `/[Course-Directory]/README.md` |
| Brand Assets & Design System | `/docs/_branding/` |
| Reusable Assignment Templates | `/docs/templates/` |
| Professional Portfolio Templates | `/docs/templates/bio-and-resume/` |
| Strategic Decision Memos | `/docs/decisions/` |
| Excel Model Templates (course-specific) | `/[Course-Directory]/_templates/excel/` |
| Project Archives | `/[Course-Directory]/archive/` |
| Design Tokens | `/docs/_branding/design.json` |
| Documentation Hub | `/docs/` |

---

## 12. CONCLUSION

This repository is organized to balance:
- **Clarity** – Descriptive names and consistent structure
- **Scalability** – Easy to add new courses and projects
- **Maintainability** – Version control and clear workflows
- **Discoverability** – Logical hierarchy and cross-linking

The centralization of documentation, templates, and brand guidelines under `/docs/` creates a unified hub for all supporting materials, while course directories remain focused on course-specific content. The use of `_` prefix for system/organizational directories, descriptive course names, and standardized project workflows ensures that the repository remains navigable and professional as it grows.

---

**Document Version:** 2.0
**Last Updated:** February 18, 2026
**Author:** Adam W. Stauffer
**Update Notes:** Reorganized supporting directories (_memos → docs/decisions, _templates → docs/templates, _branding → docs/_branding, bio-and-resume → docs/templates/bio-and-resume)
