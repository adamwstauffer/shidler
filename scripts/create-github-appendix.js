/**
 * BUS-314 Appendix: GitHub & AI Tools Setup Guide
 * Matches the existing BUS314_AI_Ratios_Project.pptx design system
 */

const path = require("path");
const globalPath = require("child_process").execSync("npm root -g").toString().trim();
const pptxgen = require(path.join(globalPath, "pptxgenjs"));
const React = require(path.join(globalPath, "react"));
const ReactDOMServer = require(path.join(globalPath, "react-dom/server"));
const sharp = require(path.join(globalPath, "sharp"));

// === Icon imports ===
const { FaGithub, FaLaptopCode, FaTerminal, FaCodeBranch, FaCloudUploadAlt,
        FaCheckCircle, FaRobot, FaComments, FaFileCode, FaExclamationTriangle,
        FaUserPlus, FaKey, FaFolderOpen, FaSearch, FaClipboardCheck,
        FaSyncAlt, FaLightbulb, FaLink } = require(path.join(globalPath, "react-icons/fa"));

// === Design tokens (from existing deck) ===
const C = {
  bgDark: "1E2530",
  bgLight: "FAF9F7",
  bgCard: "F5F5F3",
  gold: "B8975C",
  charcoal: "36454F",
  darkText: "1E2530",
  bodyText: "5A6B7A",
  mutedText: "8A9BAD",
  blueGray: "6B8FA3",
  white: "FFFFFF",
  black: "000000",
  silver: "C0C0C0",
  red: "CC4444",
  green: "1B5E40",
  greenLight: "EBF5EE",
};

const FONT = "Open Sans";

// === Icon helper ===
function renderIconSvg(IconComponent, color, size) {
  return ReactDOMServer.renderToStaticMarkup(
    React.createElement(IconComponent, { color, size: String(size) })
  );
}

async function iconToBase64Png(IconComponent, color = "#FFFFFF", size = 256) {
  const svg = renderIconSvg(IconComponent, color, size);
  const pngBuffer = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + pngBuffer.toString("base64");
}

// === Reusable shape builders ===
function addTopGoldLine(slide) {
  slide.addShape("rect", {
    x: 0, y: 0, w: 10, h: 0.04,
    fill: { color: C.gold },
  });
}

function addBottomBar(slide) {
  slide.addShape("rect", {
    x: 0, y: 5.15, w: 10, h: 0.475,
    fill: { color: C.charcoal },
  });
  slide.addText("BUS-314  |  Appendix: GitHub & AI Setup Guide  |  Shidler College of Business", {
    x: 0.5, y: 5.2, w: 9, h: 0.35,
    fontSize: 9, fontFace: FONT, color: C.mutedText,
    align: "center", valign: "middle",
  });
}

function addSectionBadge(slide, text, x, y) {
  slide.addShape("rect", {
    x, y, w: text.length * 0.09 + 0.3, h: 0.3,
    fill: { color: C.charcoal },
    rectRadius: 0.02,
  });
  slide.addText(text, {
    x, y, w: text.length * 0.09 + 0.3, h: 0.3,
    fontSize: 9, fontFace: FONT, color: C.gold,
    bold: true, align: "center", valign: "middle",
    charSpacing: 3, margin: 0,
  });
}

function addNumberCircle(slide, num, x, y, size = 0.4) {
  slide.addShape("oval", {
    x, y, w: size, h: size,
    fill: { color: C.gold },
  });
  slide.addText(String(num), {
    x, y, w: size, h: size,
    fontSize: 14, fontFace: FONT, color: C.white,
    bold: true, align: "center", valign: "middle", margin: 0,
  });
}

// === Build presentation ===
async function build() {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9";
  pres.author = "Adam W. Stauffer";
  pres.title = "BUS-314 Appendix: GitHub & AI Tools Setup Guide";

  // Pre-render icons
  const icons = {
    github: await iconToBase64Png(FaGithub, "#FFFFFF", 256),
    githubDark: await iconToBase64Png(FaGithub, "#1E2530", 256),
    laptop: await iconToBase64Png(FaLaptopCode, "#B8975C", 256),
    terminal: await iconToBase64Png(FaTerminal, "#B8975C", 256),
    branch: await iconToBase64Png(FaCodeBranch, "#B8975C", 256),
    upload: await iconToBase64Png(FaCloudUploadAlt, "#B8975C", 256),
    check: await iconToBase64Png(FaCheckCircle, "#1B5E40", 256),
    robot: await iconToBase64Png(FaRobot, "#B8975C", 256),
    comments: await iconToBase64Png(FaComments, "#B8975C", 256),
    fileCode: await iconToBase64Png(FaFileCode, "#B8975C", 256),
    warning: await iconToBase64Png(FaExclamationTriangle, "#CC4444", 256),
    userPlus: await iconToBase64Png(FaUserPlus, "#B8975C", 256),
    key: await iconToBase64Png(FaKey, "#B8975C", 256),
    folder: await iconToBase64Png(FaFolderOpen, "#B8975C", 256),
    search: await iconToBase64Png(FaSearch, "#B8975C", 256),
    clipboard: await iconToBase64Png(FaClipboardCheck, "#1B5E40", 256),
    sync: await iconToBase64Png(FaSyncAlt, "#B8975C", 256),
    lightbulb: await iconToBase64Png(FaLightbulb, "#B8975C", 256),
    link: await iconToBase64Png(FaLink, "#B8975C", 256),
  };

  // =========================================================
  // SLIDE A-1: Section Divider — APPENDIX
  // =========================================================
  {
    const slide = pres.addSlide();
    slide.background = { color: C.bgDark };
    addTopGoldLine(slide);

    slide.addText("APPENDIX", {
      x: 0.8, y: 0.6, w: 8.4, h: 0.4,
      fontSize: 14, fontFace: FONT, color: C.gold,
      bold: true, charSpacing: 6, margin: 0,
    });

    slide.addText("GitHub & AI Tools\nSetup Guide", {
      x: 0.8, y: 1.2, w: 8.4, h: 2.0,
      fontSize: 40, fontFace: FONT, color: C.white,
      bold: true, lineSpacingMultiple: 1.1, margin: 0,
    });

    slide.addShape("rect", {
      x: 0.8, y: 3.4, w: 2.0, h: 0.04,
      fill: { color: C.gold },
    });

    slide.addText(
      "Everything you need to create a GitHub account, install Git,\ncommit your work, and use AI tools for this project.", {
      x: 0.8, y: 3.65, w: 7.0, h: 0.8,
      fontSize: 14, fontFace: FONT, color: C.mutedText,
      lineSpacingMultiple: 1.4, margin: 0,
    });

    // Icon
    slide.addImage({ data: icons.github, x: 7.8, y: 3.5, w: 1.2, h: 1.2 });

    // Bottom info
    slide.addText("BUS-314  |  Shidler College of Business  |  University of Hawai\u02BBi at M\u0101noa", {
      x: 0.5, y: 5.1, w: 9, h: 0.35,
      fontSize: 10, fontFace: FONT, color: C.bodyText,
      align: "center", valign: "middle",
    });
  }

  // =========================================================
  // SLIDE A-2: What Is GitHub & Why It Matters
  // =========================================================
  {
    const slide = pres.addSlide();
    slide.background = { color: C.bgLight };
    addTopGoldLine(slide);
    addBottomBar(slide);

    slide.addText("What Is GitHub & Why Does It Matter?", {
      x: 0.8, y: 0.35, w: 8.4, h: 0.5,
      fontSize: 28, fontFace: FONT, color: C.darkText,
      bold: true, margin: 0,
    });

    slide.addText(
      "GitHub is a cloud platform for version control. Think of it as Google Docs for code and documents " +
      "\u2014 every change is tracked, reversible, and visible to your instructor.", {
      x: 0.8, y: 0.95, w: 8.4, h: 0.6,
      fontSize: 13, fontFace: FONT, color: C.bodyText,
      lineSpacingMultiple: 1.3, margin: 0,
    });

    // Three cards
    const cards = [
      { icon: icons.sync, title: "Version History", body: "Every save (commit) is permanent. You can always go back to a previous version if something breaks." },
      { icon: icons.folder, title: "Portfolio Artifact", body: "Your GitHub profile becomes a professional portfolio. Employers and grad schools check GitHub." },
      { icon: icons.clipboard, title: "Submission & Grading", body: "All stage deliverables are submitted by committing to GitHub. Your commit history IS your audit trail." },
    ];

    cards.forEach((card, i) => {
      const x = 0.8 + i * 2.9;
      const y = 1.85;
      slide.addShape("rect", {
        x, y, w: 2.6, h: 2.85,
        fill: { color: C.white },
        shadow: { type: "outer", blur: 6, offset: 2, angle: 135, color: C.black, opacity: 0.08 },
      });
      slide.addImage({ data: card.icon, x: x + 0.9, y: y + 0.25, w: 0.5, h: 0.5 });
      slide.addText(card.title, {
        x: x + 0.15, y: y + 0.9, w: 2.3, h: 0.35,
        fontSize: 14, fontFace: FONT, color: C.darkText,
        bold: true, align: "center", margin: 0,
      });
      slide.addText(card.body, {
        x: x + 0.15, y: y + 1.3, w: 2.3, h: 1.3,
        fontSize: 11, fontFace: FONT, color: C.bodyText,
        lineSpacingMultiple: 1.4, align: "center", valign: "top", margin: 0,
      });
    });
  }

  // =========================================================
  // SLIDE A-3: Step 1 — Create a GitHub Account
  // =========================================================
  {
    const slide = pres.addSlide();
    slide.background = { color: C.bgLight };
    addTopGoldLine(slide);
    addBottomBar(slide);
    addSectionBadge(slide, "STEP 1 OF 4", 0.8, 0.3);

    slide.addText("Create a GitHub Account", {
      x: 0.8, y: 0.7, w: 8.4, h: 0.5,
      fontSize: 28, fontFace: FONT, color: C.darkText,
      bold: true, margin: 0,
    });

    // Left column - steps
    const steps = [
      { num: 1, text: "Go to github.com and click Sign Up" },
      { num: 2, text: "Use your @hawaii.edu email (gets free GitHub Pro)" },
      { num: 3, text: "Choose a professional username (e.g., firstname-lastname)" },
      { num: 4, text: "Verify your email address" },
      { num: 5, text: "Share your GitHub username with the instructor" },
    ];

    steps.forEach((step, i) => {
      const y = 1.4 + i * 0.6;
      addNumberCircle(slide, step.num, 0.8, y);
      slide.addText(step.text, {
        x: 1.4, y: y, w: 4.2, h: 0.4,
        fontSize: 13, fontFace: FONT, color: C.darkText,
        valign: "middle", margin: 0,
      });
    });

    // Right column - tips card
    slide.addShape("rect", {
      x: 6.0, y: 1.4, w: 3.4, h: 3.2,
      fill: { color: C.white },
      shadow: { type: "outer", blur: 6, offset: 2, angle: 135, color: C.black, opacity: 0.08 },
    });
    slide.addImage({ data: icons.lightbulb, x: 6.25, y: 1.6, w: 0.35, h: 0.35 });
    slide.addText("Pro Tips", {
      x: 6.7, y: 1.6, w: 2.5, h: 0.35,
      fontSize: 14, fontFace: FONT, color: C.gold, bold: true, valign: "middle", margin: 0,
    });
    slide.addText([
      { text: "Username matters", options: { bold: true, breakLine: true, fontSize: 11, color: C.darkText } },
      { text: "Employers see it. Avoid gamer tags or joke names.\n\n", options: { breakLine: true, fontSize: 10, color: C.bodyText } },
      { text: "Student Developer Pack", options: { bold: true, breakLine: true, fontSize: 11, color: C.darkText } },
      { text: "education.github.com \u2014 free Pro features, Copilot access, and more with your .edu email.\n\n", options: { breakLine: true, fontSize: 10, color: C.bodyText } },
      { text: "Profile photo", options: { bold: true, breakLine: true, fontSize: 11, color: C.darkText } },
      { text: "Optional but professional. Headshot or avatar helps your instructor identify you.", options: { fontSize: 10, color: C.bodyText } },
    ], {
      x: 6.25, y: 2.1, w: 2.95, h: 2.3,
      valign: "top", margin: 0,
    });
  }

  // =========================================================
  // SLIDE A-4: Step 2 — Install Git on Your Computer
  // =========================================================
  {
    const slide = pres.addSlide();
    slide.background = { color: C.bgLight };
    addTopGoldLine(slide);
    addBottomBar(slide);
    addSectionBadge(slide, "STEP 2 OF 4", 0.8, 0.3);

    slide.addText("Install Git on Your Computer", {
      x: 0.8, y: 0.7, w: 8.4, h: 0.5,
      fontSize: 28, fontFace: FONT, color: C.darkText,
      bold: true, margin: 0,
    });

    slide.addText(
      "Git is the software that tracks changes. GitHub is the website that hosts your repository. You need both.", {
      x: 0.8, y: 1.25, w: 8.4, h: 0.4,
      fontSize: 12, fontFace: FONT, color: C.bodyText, margin: 0,
    });

    // Two columns: Windows / Mac
    const colData = [
      {
        title: "Windows",
        steps: [
          "Download from git-scm.com/download/win",
          "Run installer \u2014 accept all defaults",
          "Open Git Bash (installed automatically)",
          "Type:  git --version  to confirm",
        ],
      },
      {
        title: "Mac",
        steps: [
          "Open Terminal (Applications \u2192 Utilities)",
          "Type:  git --version",
          "If not installed, macOS will prompt you",
          "Click Install to add Xcode Command Line Tools",
        ],
      },
    ];

    colData.forEach((col, i) => {
      const x = 0.8 + i * 4.6;
      slide.addShape("rect", {
        x, y: 1.85, w: 4.2, h: 1.95,
        fill: { color: C.white },
        shadow: { type: "outer", blur: 4, offset: 2, angle: 135, color: C.black, opacity: 0.06 },
      });
      slide.addText(col.title, {
        x: x + 0.2, y: 1.95, w: 3.8, h: 0.35,
        fontSize: 15, fontFace: FONT, color: C.darkText, bold: true, margin: 0,
      });
      col.steps.forEach((step, j) => {
        slide.addText(step, {
          x: x + 0.2, y: 2.35 + j * 0.35, w: 3.8, h: 0.35,
          fontSize: 11, fontFace: FONT, color: C.bodyText,
          valign: "middle", margin: 0,
          bullet: { code: "2022" },
        });
      });
    });

    // Configure Git card
    slide.addShape("rect", {
      x: 0.8, y: 4.05, w: 8.4, h: 0.9,
      fill: { color: C.charcoal },
      rectRadius: 0.04,
    });
    slide.addImage({ data: icons.terminal, x: 1.05, y: 4.2, w: 0.4, h: 0.4 });
    slide.addText("First-Time Setup (run these two commands once):", {
      x: 1.6, y: 4.1, w: 4.0, h: 0.3,
      fontSize: 11, fontFace: FONT, color: C.gold, bold: true, margin: 0,
    });
    slide.addText('git config --global user.name "Your Name"\ngit config --global user.email "your@hawaii.edu"', {
      x: 1.6, y: 4.4, w: 7.0, h: 0.45,
      fontSize: 11, fontFace: "Consolas", color: C.white,
      lineSpacingMultiple: 1.3, margin: 0,
    });
  }

  // =========================================================
  // SLIDE A-5: Step 3 — Clone the Repository & Open It
  // =========================================================
  {
    const slide = pres.addSlide();
    slide.background = { color: C.bgLight };
    addTopGoldLine(slide);
    addBottomBar(slide);
    addSectionBadge(slide, "STEP 3 OF 4", 0.8, 0.3);

    slide.addText("Clone the Repository & Open It", {
      x: 0.8, y: 0.7, w: 8.4, h: 0.5,
      fontSize: 28, fontFace: FONT, color: C.darkText,
      bold: true, margin: 0,
    });

    slide.addText(
      "Cloning downloads a full copy of the project to your computer. You only do this once.", {
      x: 0.8, y: 1.25, w: 8.4, h: 0.35,
      fontSize: 12, fontFace: FONT, color: C.bodyText, margin: 0,
    });

    // Steps
    const cloneSteps = [
      { num: 1, title: "Get the clone URL", body: "On the repository page, click the green Code button \u2192 copy the HTTPS URL" },
      { num: 2, title: "Open your terminal", body: "Git Bash (Windows) or Terminal (Mac). Navigate to where you want the folder." },
      { num: 3, title: "Run the clone command", body: "", isCode: true, code: "git clone https://github.com/instructor/repo-name.git" },
      { num: 4, title: "Open in your editor", body: "Open the new folder in VS Code, or your preferred text editor" },
    ];

    cloneSteps.forEach((step, i) => {
      const y = 1.8 + i * 0.75;
      addNumberCircle(slide, step.num, 0.8, y, 0.35);
      slide.addText(step.title, {
        x: 1.35, y: y - 0.02, w: 3.5, h: 0.3,
        fontSize: 13, fontFace: FONT, color: C.darkText, bold: true, valign: "middle", margin: 0,
      });
      if (step.isCode) {
        slide.addText(step.code, {
          x: 1.35, y: y + 0.28, w: 7.5, h: 0.3,
          fontSize: 11, fontFace: "Consolas", color: C.gold,
          fill: { color: C.charcoal }, valign: "middle", margin: [0, 8, 0, 8],
        });
      } else {
        slide.addText(step.body, {
          x: 1.35, y: y + 0.25, w: 7.5, h: 0.3,
          fontSize: 11, fontFace: FONT, color: C.bodyText, valign: "middle", margin: 0,
        });
      }
    });

    // Tip bar
    slide.addShape("rect", {
      x: 0.8, y: 4.55, w: 8.4, h: 0.45,
      fill: { color: C.greenLight },
      rectRadius: 0.04,
    });
    slide.addImage({ data: icons.check, x: 1.0, y: 4.6, w: 0.3, h: 0.3 });
    slide.addText("After cloning, run  cd repo-name  to enter the project folder before doing anything else.", {
      x: 1.45, y: 4.55, w: 7.5, h: 0.45,
      fontSize: 11, fontFace: FONT, color: C.green, bold: false, valign: "middle", margin: 0,
    });
  }

  // =========================================================
  // SLIDE A-6: Step 4 — The Git Workflow (Add, Commit, Push)
  // =========================================================
  {
    const slide = pres.addSlide();
    slide.background = { color: C.bgLight };
    addTopGoldLine(slide);
    addBottomBar(slide);
    addSectionBadge(slide, "STEP 4 OF 4", 0.8, 0.3);

    slide.addText("The Git Workflow: Add, Commit, Push", {
      x: 0.8, y: 0.7, w: 8.4, h: 0.5,
      fontSize: 28, fontFace: FONT, color: C.darkText,
      bold: true, margin: 0,
    });

    slide.addText(
      "These three commands are all you need. Run them every time you finish work on a deliverable.", {
      x: 0.8, y: 1.2, w: 8.4, h: 0.35,
      fontSize: 12, fontFace: FONT, color: C.bodyText, margin: 0,
    });

    // Three command cards
    const cmds = [
      {
        num: "1", cmd: "git add .", label: "Stage",
        desc: "Tells Git which files to include in the next save. The dot means all changed files.",
      },
      {
        num: "2", cmd: 'git commit -m "Stage 1 memo"', label: "Commit",
        desc: "Creates a permanent snapshot with a descriptive message. This is your save point.",
      },
      {
        num: "3", cmd: "git push", label: "Push",
        desc: "Uploads your commits to GitHub so they are visible online and to your instructor.",
      },
    ];

    cmds.forEach((c, i) => {
      const x = 0.8 + i * 3.0;
      // Card
      slide.addShape("rect", {
        x, y: 1.7, w: 2.7, h: 2.9,
        fill: { color: C.white },
        shadow: { type: "outer", blur: 4, offset: 2, angle: 135, color: C.black, opacity: 0.06 },
      });
      // Number + label
      addNumberCircle(slide, c.num, x + 1.05, 1.85, 0.4);
      slide.addText(c.label, {
        x: x + 0.15, y: 2.35, w: 2.4, h: 0.3,
        fontSize: 15, fontFace: FONT, color: C.darkText,
        bold: true, align: "center", margin: 0,
      });
      // Code box
      slide.addText(c.cmd, {
        x: x + 0.15, y: 2.75, w: 2.4, h: 0.4,
        fontSize: 10, fontFace: "Consolas", color: C.gold,
        fill: { color: C.charcoal }, align: "center", valign: "middle",
        rectRadius: 0.03, margin: 0,
      });
      // Description
      slide.addText(c.desc, {
        x: x + 0.15, y: 3.25, w: 2.4, h: 1.1,
        fontSize: 11, fontFace: FONT, color: C.bodyText,
        lineSpacingMultiple: 1.4, valign: "top", margin: 0,
      });
    });

    // Warning bar
    slide.addShape("rect", {
      x: 0.8, y: 4.72, w: 8.4, h: 0.05,
      fill: { color: C.gold },
    });
  }

  // =========================================================
  // SLIDE A-7: GitHub Desktop Alternative
  // =========================================================
  {
    const slide = pres.addSlide();
    slide.background = { color: C.bgLight };
    addTopGoldLine(slide);
    addBottomBar(slide);

    slide.addText("Prefer a Visual Interface? Use GitHub Desktop", {
      x: 0.8, y: 0.35, w: 8.4, h: 0.5,
      fontSize: 28, fontFace: FONT, color: C.darkText,
      bold: true, margin: 0,
    });

    slide.addText(
      "GitHub Desktop is a free app that does the same thing as the command line but with buttons instead of typing. " +
      "Either approach is fine for this course.", {
      x: 0.8, y: 0.9, w: 8.4, h: 0.5,
      fontSize: 12, fontFace: FONT, color: C.bodyText,
      lineSpacingMultiple: 1.3, margin: 0,
    });

    // Two-column: Install / Workflow
    // Install column
    slide.addShape("rect", {
      x: 0.8, y: 1.6, w: 4.2, h: 3.3,
      fill: { color: C.white },
      shadow: { type: "outer", blur: 4, offset: 2, angle: 135, color: C.black, opacity: 0.06 },
    });
    slide.addText("Install & Connect", {
      x: 1.0, y: 1.75, w: 3.8, h: 0.35,
      fontSize: 15, fontFace: FONT, color: C.darkText, bold: true, margin: 0,
    });
    const installSteps = [
      "Download from desktop.github.com",
      "Sign in with your GitHub account",
      'File \u2192 Clone Repository \u2192 paste URL',
      "Choose where to save on your computer",
    ];
    installSteps.forEach((step, i) => {
      addNumberCircle(slide, i + 1, 1.0, 2.25 + i * 0.55, 0.3);
      slide.addText(step, {
        x: 1.45, y: 2.25 + i * 0.55, w: 3.3, h: 0.3,
        fontSize: 11, fontFace: FONT, color: C.bodyText, valign: "middle", margin: 0,
      });
    });

    // Workflow column
    slide.addShape("rect", {
      x: 5.4, y: 1.6, w: 3.8, h: 3.3,
      fill: { color: C.white },
      shadow: { type: "outer", blur: 4, offset: 2, angle: 135, color: C.black, opacity: 0.06 },
    });
    slide.addText("Daily Workflow", {
      x: 5.6, y: 1.75, w: 3.4, h: 0.35,
      fontSize: 15, fontFace: FONT, color: C.darkText, bold: true, margin: 0,
    });
    const workflowSteps = [
      { label: "Changes tab", desc: "shows modified files" },
      { label: "Summary box", desc: 'type your commit message (e.g., "Stage 2 Excel model")' },
      { label: "Commit button", desc: "saves the snapshot locally" },
      { label: "Push Origin", desc: "uploads to GitHub" },
    ];
    workflowSteps.forEach((step, i) => {
      addNumberCircle(slide, i + 1, 5.6, 2.25 + i * 0.55, 0.3);
      slide.addText([
        { text: step.label + "  ", options: { bold: true, fontSize: 11, color: C.darkText } },
        { text: "\u2014 " + step.desc, options: { fontSize: 11, color: C.bodyText } },
      ], {
        x: 6.05, y: 2.25 + i * 0.55, w: 3.0, h: 0.4,
        valign: "middle", margin: 0,
      });
    });
  }

  // =========================================================
  // SLIDE A-8: Where to Save Each Deliverable
  // =========================================================
  {
    const slide = pres.addSlide();
    slide.background = { color: C.bgLight };
    addTopGoldLine(slide);
    addBottomBar(slide);

    slide.addText("Where to Save Each Deliverable", {
      x: 0.8, y: 0.35, w: 8.4, h: 0.5,
      fontSize: 28, fontFace: FONT, color: C.darkText,
      bold: true, margin: 0,
    });

    slide.addText(
      "Save your files in the right directory, then commit and push. The file naming convention is shown below.", {
      x: 0.8, y: 0.9, w: 8.4, h: 0.35,
      fontSize: 12, fontFace: FONT, color: C.bodyText, margin: 0,
    });

    // Table
    const tableRows = [
      [
        { text: "Stage", options: { bold: true, color: C.white, fill: { color: C.charcoal }, fontSize: 12, fontFace: FONT, align: "center" } },
        { text: "Deliverable", options: { bold: true, color: C.white, fill: { color: C.charcoal }, fontSize: 12, fontFace: FONT } },
        { text: "File Name", options: { bold: true, color: C.white, fill: { color: C.charcoal }, fontSize: 12, fontFace: FONT } },
        { text: "Directory", options: { bold: true, color: C.white, fill: { color: C.charcoal }, fontSize: 12, fontFace: FONT } },
      ],
      [
        { text: "1", options: { align: "center", fontSize: 12, fontFace: FONT, color: C.darkText } },
        { text: "Executive Memo", options: { fontSize: 12, fontFace: FONT, color: C.darkText } },
        { text: "lastname-stage1-memo.md", options: { fontSize: 11, fontFace: "Consolas", color: C.gold } },
        { text: "docs/decisions/", options: { fontSize: 11, fontFace: "Consolas", color: C.bodyText } },
      ],
      [
        { text: "2", options: { align: "center", fontSize: 12, fontFace: FONT, color: C.darkText, fill: { color: C.bgCard } } },
        { text: "Excel Model", options: { fontSize: 12, fontFace: FONT, color: C.darkText, fill: { color: C.bgCard } } },
        { text: "lastname-stage2-model.xlsx", options: { fontSize: 11, fontFace: "Consolas", color: C.gold, fill: { color: C.bgCard } } },
        { text: "docs/templates/excel/", options: { fontSize: 11, fontFace: "Consolas", color: C.bodyText, fill: { color: C.bgCard } } },
      ],
      [
        { text: "3", options: { align: "center", fontSize: 12, fontFace: FONT, color: C.darkText } },
        { text: "Technical Spec", options: { fontSize: 12, fontFace: FONT, color: C.darkText } },
        { text: "lastname-stage3-spec.md", options: { fontSize: 11, fontFace: "Consolas", color: C.gold } },
        { text: "docs/", options: { fontSize: 11, fontFace: "Consolas", color: C.bodyText } },
      ],
      [
        { text: "4", options: { align: "center", fontSize: 12, fontFace: FONT, color: C.darkText, fill: { color: C.bgCard } } },
        { text: "Final Analysis", options: { fontSize: 12, fontFace: FONT, color: C.darkText, fill: { color: C.bgCard } } },
        { text: "lastname-stage4-final.md", options: { fontSize: 11, fontFace: "Consolas", color: C.gold, fill: { color: C.bgCard } } },
        { text: "docs/", options: { fontSize: 11, fontFace: "Consolas", color: C.bodyText, fill: { color: C.bgCard } } },
      ],
      [
        { text: "\u2014", options: { align: "center", fontSize: 12, fontFace: FONT, color: C.mutedText } },
        { text: "Prompt Log", options: { fontSize: 12, fontFace: FONT, color: C.darkText } },
        { text: "prompt-log.md", options: { fontSize: 11, fontFace: "Consolas", color: C.gold } },
        { text: "deliverables/", options: { fontSize: 11, fontFace: "Consolas", color: C.bodyText } },
      ],
    ];

    slide.addTable(tableRows, {
      x: 0.8, y: 1.45, w: 8.4,
      colW: [0.8, 1.8, 3.0, 2.8],
      border: { pt: 0.5, color: C.silver },
      rowH: [0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
    });

    // Commit example
    slide.addShape("rect", {
      x: 0.8, y: 4.15, w: 8.4, h: 0.8,
      fill: { color: C.charcoal },
      rectRadius: 0.04,
    });
    slide.addText("Example: submitting Stage 1", {
      x: 1.05, y: 4.2, w: 4.0, h: 0.25,
      fontSize: 10, fontFace: FONT, color: C.gold, bold: true, margin: 0,
    });
    slide.addText(
      'git add docs/decisions/stauffer-stage1-memo.md\ngit commit -m "Stage 1: executive memo for AAPL ratio analysis"\ngit push', {
      x: 1.05, y: 4.48, w: 7.8, h: 0.45,
      fontSize: 10, fontFace: "Consolas", color: C.white,
      lineSpacingMultiple: 1.3, margin: 0,
    });
  }

  // =========================================================
  // SLIDE A-9: Common Git Mistakes & Fixes
  // =========================================================
  {
    const slide = pres.addSlide();
    slide.background = { color: C.bgLight };
    addTopGoldLine(slide);
    addBottomBar(slide);

    slide.addText("Common Git Mistakes & How to Fix Them", {
      x: 0.8, y: 0.35, w: 8.4, h: 0.5,
      fontSize: 28, fontFace: FONT, color: C.darkText,
      bold: true, margin: 0,
    });

    const mistakes = [
      {
        problem: '"Everything up-to-date" but nothing pushed',
        cause: "You forgot  git add  before committing.",
        fix: "git add .  then  git commit  then  git push",
      },
      {
        problem: '"fatal: not a git repository"',
        cause: "Your terminal is not inside the project folder.",
        fix: "cd repo-name  to navigate into the cloned folder",
      },
      {
        problem: 'Accidentally edited the wrong file',
        cause: "No worries \u2014 Git tracks everything.",
        fix: "git checkout -- filename  reverts to last commit",
      },
      {
        problem: '"rejected \u2014 failed to push"',
        cause: "Someone (or you on another device) pushed first.",
        fix: "git pull  then  git push  to sync and re-upload",
      },
      {
        problem: "Forgot to write a commit message",
        cause: "A text editor opened and you're stuck.",
        fix: "Type your message, then press Esc, type  :wq  and press Enter",
      },
    ];

    mistakes.forEach((m, i) => {
      const y = 1.05 + i * 0.78;
      // Alternating background
      if (i % 2 === 0) {
        slide.addShape("rect", {
          x: 0.8, y, w: 8.4, h: 0.72,
          fill: { color: C.white },
        });
      }
      slide.addText(m.problem, {
        x: 0.95, y: y + 0.02, w: 3.5, h: 0.3,
        fontSize: 12, fontFace: FONT, color: C.darkText, bold: true, margin: 0,
      });
      slide.addText(m.cause, {
        x: 0.95, y: y + 0.32, w: 3.5, h: 0.3,
        fontSize: 10, fontFace: FONT, color: C.bodyText, margin: 0,
      });
      slide.addText("Fix:  " + m.fix, {
        x: 4.8, y: y + 0.05, w: 4.2, h: 0.55,
        fontSize: 11, fontFace: "Consolas", color: C.green, valign: "middle", margin: 0,
      });
    });
  }

  // =========================================================
  // SLIDE A-10: Section Divider — Using AI Tools
  // =========================================================
  {
    const slide = pres.addSlide();
    slide.background = { color: C.bgDark };
    addTopGoldLine(slide);

    slide.addText("PART 2", {
      x: 0.8, y: 0.8, w: 8.4, h: 0.4,
      fontSize: 14, fontFace: FONT, color: C.gold,
      bold: true, charSpacing: 6, margin: 0,
    });

    slide.addText("Using AI Tools\nwith GitHub", {
      x: 0.8, y: 1.4, w: 8.4, h: 1.8,
      fontSize: 40, fontFace: FONT, color: C.white,
      bold: true, lineSpacingMultiple: 1.1, margin: 0,
    });

    slide.addShape("rect", {
      x: 0.8, y: 3.4, w: 2.0, h: 0.04,
      fill: { color: C.gold },
    });

    slide.addText(
      "How to use ChatGPT and Claude as analytical partners\nfor your ratio analysis project.", {
      x: 0.8, y: 3.65, w: 7.0, h: 0.7,
      fontSize: 14, fontFace: FONT, color: C.mutedText,
      lineSpacingMultiple: 1.4, margin: 0,
    });

    slide.addImage({ data: icons.robot, x: 7.8, y: 3.3, w: 1.2, h: 1.2 });

    slide.addText("BUS-314  |  Shidler College of Business  |  University of Hawai\u02BBi at M\u0101noa", {
      x: 0.5, y: 5.1, w: 9, h: 0.35,
      fontSize: 10, fontFace: FONT, color: C.bodyText,
      align: "center", valign: "middle",
    });
  }

  // =========================================================
  // SLIDE A-11: ChatGPT — Getting Started
  // =========================================================
  {
    const slide = pres.addSlide();
    slide.background = { color: C.bgLight };
    addTopGoldLine(slide);
    addBottomBar(slide);

    slide.addText("Using ChatGPT for This Project", {
      x: 0.8, y: 0.35, w: 8.4, h: 0.5,
      fontSize: 28, fontFace: FONT, color: C.darkText,
      bold: true, margin: 0,
    });

    slide.addText("chatgpt.com  |  Free tier is sufficient. GPT-4o is recommended if you have Plus.", {
      x: 0.8, y: 0.9, w: 8.4, h: 0.3,
      fontSize: 11, fontFace: FONT, color: C.bodyText, margin: 0,
    });

    // Left: What it's good at
    slide.addShape("rect", {
      x: 0.8, y: 1.4, w: 4.2, h: 3.4,
      fill: { color: C.white },
      shadow: { type: "outer", blur: 4, offset: 2, angle: 135, color: C.black, opacity: 0.06 },
    });
    slide.addImage({ data: icons.check, x: 1.0, y: 1.55, w: 0.3, h: 0.3 });
    slide.addText("What ChatGPT Does Well", {
      x: 1.4, y: 1.55, w: 3.4, h: 0.3,
      fontSize: 14, fontFace: FONT, color: C.green, bold: true, valign: "middle", margin: 0,
    });
    const goodAt = [
      "Explaining ratio formulas and what they mean",
      "Drafting memo language and executive summaries",
      "Generating Excel formulas from plain English",
      "Reviewing your spec for clarity and completeness",
      "Building structured AI prompts (Stage 4)",
      "Brainstorming strategic recommendations",
    ];
    goodAt.forEach((item, i) => {
      slide.addText(item, {
        x: 1.0, y: 2.0 + i * 0.4, w: 3.8, h: 0.35,
        fontSize: 11, fontFace: FONT, color: C.bodyText,
        valign: "middle", margin: 0,
        bullet: { code: "25AA" },
      });
    });

    // Right: What to watch out for
    slide.addShape("rect", {
      x: 5.4, y: 1.4, w: 3.8, h: 3.4,
      fill: { color: C.white },
      shadow: { type: "outer", blur: 4, offset: 2, angle: 135, color: C.black, opacity: 0.06 },
    });
    slide.addImage({ data: icons.warning, x: 5.6, y: 1.55, w: 0.3, h: 0.3 });
    slide.addText("Watch Out For", {
      x: 6.0, y: 1.55, w: 3.0, h: 0.3,
      fontSize: 14, fontFace: FONT, color: C.red, bold: true, valign: "middle", margin: 0,
    });
    const watchOut = [
      "It can invent financial data that looks real but isn't",
      "Ratio formulas may be subtly wrong \u2014 always verify",
      "It doesn't know YOUR company's specific numbers",
      "Named range conventions must be given to it explicitly",
      "Never paste sensitive personal data into prompts",
    ];
    watchOut.forEach((item, i) => {
      slide.addText(item, {
        x: 5.6, y: 2.0 + i * 0.5, w: 3.4, h: 0.4,
        fontSize: 11, fontFace: FONT, color: C.bodyText,
        lineSpacingMultiple: 1.3, valign: "middle", margin: 0,
        bullet: { code: "25AA" },
      });
    });
  }

  // =========================================================
  // SLIDE A-12: Claude — Getting Started
  // =========================================================
  {
    const slide = pres.addSlide();
    slide.background = { color: C.bgLight };
    addTopGoldLine(slide);
    addBottomBar(slide);

    slide.addText("Using Claude for This Project", {
      x: 0.8, y: 0.35, w: 8.4, h: 0.5,
      fontSize: 28, fontFace: FONT, color: C.darkText,
      bold: true, margin: 0,
    });

    slide.addText("claude.ai  |  Free tier available. Pro gives extended thinking and longer conversations.", {
      x: 0.8, y: 0.9, w: 8.4, h: 0.3,
      fontSize: 11, fontFace: FONT, color: C.bodyText, margin: 0,
    });

    // Claude strengths
    slide.addShape("rect", {
      x: 0.8, y: 1.4, w: 4.2, h: 2.2,
      fill: { color: C.white },
      shadow: { type: "outer", blur: 4, offset: 2, angle: 135, color: C.black, opacity: 0.06 },
    });
    slide.addText("Claude Strengths", {
      x: 1.0, y: 1.5, w: 3.8, h: 0.3,
      fontSize: 14, fontFace: FONT, color: C.darkText, bold: true, margin: 0,
    });
    const claudeStrengths = [
      "Longer context window \u2014 paste entire specs or data sets",
      "Strong at structured document generation (memos, specs)",
      "Careful reasoning for multi-step ratio calculations",
      "Can read uploaded files (PDF, Excel, images)",
    ];
    claudeStrengths.forEach((item, i) => {
      slide.addText(item, {
        x: 1.0, y: 1.9 + i * 0.38, w: 3.8, h: 0.35,
        fontSize: 11, fontFace: FONT, color: C.bodyText,
        valign: "middle", margin: 0,
        bullet: { code: "25AA" },
      });
    });

    // How to use with GitHub
    slide.addShape("rect", {
      x: 5.4, y: 1.4, w: 3.8, h: 2.2,
      fill: { color: C.white },
      shadow: { type: "outer", blur: 4, offset: 2, angle: 135, color: C.black, opacity: 0.06 },
    });
    slide.addText("Using Claude with GitHub", {
      x: 5.6, y: 1.5, w: 3.4, h: 0.3,
      fontSize: 14, fontFace: FONT, color: C.darkText, bold: true, margin: 0,
    });
    const claudeGithub = [
      "Paste your GitHub file links as context",
      "Ask Claude to generate Markdown for your memos",
      "Upload your .xlsx and ask for ratio verification",
      "Use Claude to draft your Stage 4 AI prompt",
    ];
    claudeGithub.forEach((item, i) => {
      slide.addText(item, {
        x: 5.6, y: 1.9 + i * 0.38, w: 3.4, h: 0.35,
        fontSize: 11, fontFace: FONT, color: C.bodyText,
        valign: "middle", margin: 0,
        bullet: { code: "25AA" },
      });
    });

    // Bottom: Example prompt
    slide.addShape("rect", {
      x: 0.8, y: 3.85, w: 8.4, h: 1.1,
      fill: { color: C.charcoal },
      rectRadius: 0.04,
    });
    slide.addImage({ data: icons.comments, x: 1.05, y: 3.95, w: 0.35, h: 0.35 });
    slide.addText("Example Prompt for Stage 1", {
      x: 1.5, y: 3.95, w: 4.0, h: 0.3,
      fontSize: 12, fontFace: FONT, color: C.gold, bold: true, margin: 0,
    });
    slide.addText(
      '"I\'m writing a 300-400 word executive memo for my CFO about Apple Inc. (AAPL). ' +
      'The memo should cover: why ratio analysis matters, the six ratio categories (Performance, Profitability, ' +
      'Efficiency, Leverage, Liquidity, Du Pont), and a preview of my analytical plan. ' +
      'Use professional finance language."', {
      x: 1.05, y: 4.3, w: 7.95, h: 0.6,
      fontSize: 10, fontFace: FONT, color: C.white,
      italic: true, lineSpacingMultiple: 1.3, margin: 0,
    });
  }

  // =========================================================
  // SLIDE A-13: Prompt Engineering Patterns
  // =========================================================
  {
    const slide = pres.addSlide();
    slide.background = { color: C.bgLight };
    addTopGoldLine(slide);
    addBottomBar(slide);

    slide.addText("Prompt Patterns That Work", {
      x: 0.8, y: 0.35, w: 8.4, h: 0.5,
      fontSize: 28, fontFace: FONT, color: C.darkText,
      bold: true, margin: 0,
    });

    slide.addText("Use these templates as starting points. Adapt them to your company and stage.", {
      x: 0.8, y: 0.9, w: 8.4, h: 0.3,
      fontSize: 12, fontFace: FONT, color: C.bodyText, margin: 0,
    });

    // Pattern cards
    const patterns = [
      {
        title: "Give It a Role",
        bad: '"Help me with ratios"',
        good: '"You are an FP&A analyst at Apple. Calculate the current ratio from these balance sheet figures..."',
      },
      {
        title: "Provide the Data",
        bad: '"What is AAPL\'s ROE?"',
        good: '"Net Income: $93.7B. Shareholder Equity: $56.9B. Calculate ROE and explain what it means for Apple."',
      },
      {
        title: "Specify the Output",
        bad: '"Analyze these ratios"',
        good: '"Present results in a Markdown table with columns: Ratio Name, Formula, Value, Interpretation. Use 2 decimal places."',
      },
      {
        title: "Request Verification",
        bad: '"Is this right?"',
        good: '"Cross-check: ROE should equal Profit Margin \u00D7 Asset Turnover \u00D7 Equity Multiplier via Du Pont. Show the math."',
      },
    ];

    patterns.forEach((p, i) => {
      const y = 1.35 + i * 0.9;
      slide.addShape("rect", {
        x: 0.8, y, w: 8.4, h: 0.8,
        fill: { color: C.white },
        shadow: { type: "outer", blur: 3, offset: 1, angle: 135, color: C.black, opacity: 0.05 },
      });
      // Left accent
      slide.addShape("rect", {
        x: 0.8, y, w: 0.06, h: 0.8,
        fill: { color: C.gold },
      });
      slide.addText(p.title, {
        x: 1.05, y: y + 0.03, w: 2.0, h: 0.35,
        fontSize: 13, fontFace: FONT, color: C.darkText, bold: true, valign: "middle", margin: 0,
      });
      slide.addText([
        { text: "Vague:  ", options: { bold: true, fontSize: 10, color: C.red } },
        { text: p.bad, options: { italic: true, fontSize: 10, color: C.mutedText } },
      ], {
        x: 1.05, y: y + 0.38, w: 3.5, h: 0.35, valign: "middle", margin: 0,
      });
      slide.addText([
        { text: "Better:  ", options: { bold: true, fontSize: 10, color: C.green } },
        { text: p.good, options: { fontSize: 10, color: C.bodyText } },
      ], {
        x: 4.6, y: y + 0.05, w: 4.4, h: 0.7, valign: "middle", margin: 0,
        lineSpacingMultiple: 1.3,
      });
    });
  }

  // =========================================================
  // SLIDE A-14: AI + GitHub Workflow Integration
  // =========================================================
  {
    const slide = pres.addSlide();
    slide.background = { color: C.bgLight };
    addTopGoldLine(slide);
    addBottomBar(slide);

    slide.addText("Putting It All Together: AI + GitHub Workflow", {
      x: 0.8, y: 0.35, w: 8.4, h: 0.5,
      fontSize: 28, fontFace: FONT, color: C.darkText,
      bold: true, margin: 0,
    });

    // Pipeline flow
    const flowSteps = [
      { label: "Draft", desc: "Use AI to draft\nmemo or spec", icon: icons.robot },
      { label: "Edit", desc: "Revise in your\ntext editor", icon: icons.fileCode },
      { label: "Save", desc: "Save the .md or\n.xlsx file locally", icon: icons.folder },
      { label: "Commit", desc: "git add + commit\nwith clear message", icon: icons.branch },
      { label: "Push", desc: "git push to upload\nto GitHub", icon: icons.upload },
    ];

    flowSteps.forEach((step, i) => {
      const x = 0.5 + i * 1.9;
      // Card
      slide.addShape("rect", {
        x, y: 1.15, w: 1.6, h: 2.0,
        fill: { color: C.white },
        shadow: { type: "outer", blur: 4, offset: 2, angle: 135, color: C.black, opacity: 0.06 },
      });
      slide.addImage({ data: step.icon, x: x + 0.55, y: 1.3, w: 0.4, h: 0.4 });
      slide.addText(step.label, {
        x: x + 0.1, y: 1.8, w: 1.4, h: 0.3,
        fontSize: 14, fontFace: FONT, color: C.darkText,
        bold: true, align: "center", margin: 0,
      });
      slide.addText(step.desc, {
        x: x + 0.1, y: 2.15, w: 1.4, h: 0.7,
        fontSize: 10, fontFace: FONT, color: C.bodyText,
        lineSpacingMultiple: 1.3, align: "center", valign: "top", margin: 0,
      });
      // Arrow between cards
      if (i < flowSteps.length - 1) {
        slide.addText("\u2192", {
          x: x + 1.6, y: 1.8, w: 0.3, h: 0.4,
          fontSize: 18, fontFace: FONT, color: C.gold,
          bold: true, align: "center", valign: "middle", margin: 0,
        });
      }
    });

    // Prompt log reminder
    slide.addShape("rect", {
      x: 0.8, y: 3.5, w: 8.4, h: 1.35,
      fill: { color: C.white },
      shadow: { type: "outer", blur: 4, offset: 2, angle: 135, color: C.black, opacity: 0.06 },
    });
    slide.addShape("rect", {
      x: 0.8, y: 3.5, w: 0.06, h: 1.35,
      fill: { color: C.gold },
    });
    slide.addImage({ data: icons.lightbulb, x: 1.05, y: 3.6, w: 0.35, h: 0.35 });
    slide.addText("Don\u2019t Forget Your Prompt Log", {
      x: 1.5, y: 3.6, w: 4.0, h: 0.35,
      fontSize: 15, fontFace: FONT, color: C.darkText, bold: true, valign: "middle", margin: 0,
    });
    slide.addText([
      { text: "Every meaningful AI interaction should be logged in ", options: { fontSize: 11, color: C.bodyText } },
      { text: "deliverables/prompt-log.md", options: { fontSize: 11, fontFace: "Consolas", color: C.gold, bold: true } },
      { text: "\n\nFor each entry, record: ", options: { fontSize: 11, color: C.bodyText, breakLine: true } },
      { text: "the prompt you used", options: { fontSize: 11, color: C.darkText, bold: true } },
      { text: ", ", options: { fontSize: 11, color: C.bodyText } },
      { text: "the key output", options: { fontSize: 11, color: C.darkText, bold: true } },
      { text: ", and ", options: { fontSize: 11, color: C.bodyText } },
      { text: "whether you used/modified/rejected it", options: { fontSize: 11, color: C.darkText, bold: true } },
      { text: ".", options: { fontSize: 11, color: C.bodyText } },
    ], {
      x: 1.05, y: 4.0, w: 7.95, h: 0.7,
      valign: "top", margin: 0,
      lineSpacingMultiple: 1.4,
    });
  }

  // =========================================================
  // SLIDE A-15: Quick Reference Cheat Sheet
  // =========================================================
  {
    const slide = pres.addSlide();
    slide.background = { color: C.bgDark };
    addTopGoldLine(slide);

    slide.addText("Quick Reference Cheat Sheet", {
      x: 0.8, y: 0.3, w: 8.4, h: 0.5,
      fontSize: 28, fontFace: FONT, color: C.white,
      bold: true, margin: 0,
    });

    // Git commands column
    slide.addText("Git Commands", {
      x: 0.8, y: 0.95, w: 4.0, h: 0.35,
      fontSize: 14, fontFace: FONT, color: C.gold, bold: true, margin: 0,
    });
    const gitCmds = [
      ["git clone <url>", "Download repository for the first time"],
      ["git status", "See what files have changed"],
      ["git add .", "Stage all changes for commit"],
      ['git commit -m "msg"', "Save a snapshot with a message"],
      ["git push", "Upload commits to GitHub"],
      ["git pull", "Download latest changes from GitHub"],
      ["git log --oneline", "View commit history"],
    ];
    gitCmds.forEach((cmd, i) => {
      const y = 1.4 + i * 0.48;
      slide.addText(cmd[0], {
        x: 0.8, y, w: 3.5, h: 0.25,
        fontSize: 11, fontFace: "Consolas", color: C.gold, margin: 0,
      });
      slide.addText(cmd[1], {
        x: 0.8, y: y + 0.22, w: 3.5, h: 0.22,
        fontSize: 9, fontFace: FONT, color: C.mutedText, margin: 0,
      });
    });

    // Divider line
    slide.addShape("rect", {
      x: 4.8, y: 0.95, w: 0.02, h: 3.8,
      fill: { color: C.bodyText },
    });

    // Useful links column
    slide.addText("Useful Links", {
      x: 5.2, y: 0.95, w: 4.0, h: 0.35,
      fontSize: 14, fontFace: FONT, color: C.gold, bold: true, margin: 0,
    });
    const links = [
      ["github.com", "Create account & view repositories"],
      ["desktop.github.com", "GitHub Desktop (visual Git client)"],
      ["chatgpt.com", "ChatGPT (OpenAI)"],
      ["claude.ai", "Claude (Anthropic)"],
      ["education.github.com", "Student Developer Pack (free Pro)"],
      ["code.visualstudio.com", "VS Code (free text editor)"],
      ["git-scm.com", "Official Git download"],
    ];
    links.forEach((link, i) => {
      const y = 1.4 + i * 0.48;
      slide.addText(link[0], {
        x: 5.2, y, w: 4.0, h: 0.25,
        fontSize: 11, fontFace: FONT, color: C.blueGray, bold: true, margin: 0,
      });
      slide.addText(link[1], {
        x: 5.2, y: y + 0.22, w: 4.0, h: 0.22,
        fontSize: 9, fontFace: FONT, color: C.mutedText, margin: 0,
      });
    });

    // Bottom bar
    slide.addShape("rect", {
      x: 0, y: 5.0, w: 10, h: 0.04,
      fill: { color: C.gold },
    });
    slide.addText("BUS-314  |  Shidler College of Business  |  University of Hawai\u02BBi at M\u0101noa  |  adamstau@hawaii.edu", {
      x: 0.5, y: 5.1, w: 9, h: 0.35,
      fontSize: 10, fontFace: FONT, color: C.bodyText,
      align: "center", valign: "middle",
    });
  }

  // =========================================================
  // Write file
  // =========================================================
  const outPath = path.resolve("docs/presentations/GitHub_AI_Appendix.pptx");
  await pres.writeFile({ fileName: outPath });
  console.log("Created: " + outPath);
}

build().catch(err => { console.error(err); process.exit(1); });
