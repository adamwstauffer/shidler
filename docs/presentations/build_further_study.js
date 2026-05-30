const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const { FaBook, FaLandmark, FaBitcoin, FaRobot, FaCode, FaPlay } = require("react-icons/fa");

// ---- Brand tokens (docs/_branding/design.json) ----
const GREEN = "024731";
const GREEN_700 = "012E1F";
const GREEN_300 = "4DA78F";
const GREEN_100 = "B3D9CF";
const GREEN_50 = "E6F2EF";
const SILVER = "B2B2B2";
const BLACK = "1A1A1A";
const MUTE = "555555";
const WHITE = "FFFFFF";

const FACE = "Open Sans";

const makeShadow = () => ({ type: "outer", color: "000000", blur: 9, offset: 3, angle: 135, opacity: 0.28 });

async function iconPng(IconComponent, color, size = 256) {
  const svg = ReactDOMServer.renderToStaticMarkup(
    React.createElement(IconComponent, { color, size: String(size) })
  );
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}

(async () => {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE"; // 13.3 x 7.5
  pres.author = "Adam W. Stauffer";
  pres.title = "Further Study — Recommended Resources";

  const topics = [
    {
      icon: FaBook, tag: "GOOD READS", format: "BOOK",
      cover: "C:/GitHub/shidler/docs/presentations/assets/investment-biker.jpg", // experimental: book cover
      railTitle: "Investment Biker",
      author: "Jim Rogers",
      overview:
        "Part travelogue, part macro masterclass: Jim Rogers rides 100,000+ miles across six continents, sizing up each country's economy from the ground — borders, black markets, currencies, and street-level commerce.",
      why:
        "Teaches you to read a market from what you actually observe, not just headline statistics. A vivid first lesson in global macro, country risk, and contrarian thinking.",
      bio:
        "Co-founded the Quantum Fund with George Soros, retired at 37, and became a legendary commodities investor and global adventurer.",
      primaryLabel: "READ",
      primaryLinks: ["Investment Biker — Jim Rogers (1994)"],
      further: ["Adventure Capitalist (the follow-up, by car)", "Hot Commodities"],
    },
    {
      icon: FaBook, tag: "GOOD READS", format: "BOOK",
      cover: "C:/GitHub/shidler/docs/presentations/assets/soros-alchemy.jpg",
      railTitle: "The Alchemy of Finance",
      author: "George Soros",
      overview:
        "Soros lays out his theory of reflexivity: market participants' biased perceptions feed back into and reshape the very fundamentals they are trying to predict, fueling self-reinforcing boom-and-bust cycles — illustrated with a real-time trading diary.",
      why:
        "A foundational challenge to efficient-market thinking. Prices are not passive reflections of value but active forces that bend reality — sharpening how you reason about bubbles, feedback loops, and reflexive risk.",
      bio:
        "Co-founded the Quantum Fund with Jim Rogers and became one of history's most successful speculators — famously \"broke the Bank of England\" in 1992 — and later a major philanthropist.",
      primaryLabel: "READ",
      primaryLinks: ["The Alchemy of Finance — George Soros (1987)"],
      further: ["Foreword by Paul A. Volcker", "Pairs with Investment Biker — same Quantum Fund founders"],
    },
    {
      icon: FaLandmark, tag: "ECONOMICS", format: "VIDEO · ~30 MIN",
      image: "C:/GitHub/shidler/docs/presentations/assets/PHe0bXAIuk0.jpg", // experimental: video thumbnail
      railTitle: "How the Economic Machine Works",
      author: "Ray Dalio",
      overview:
        "A 30-minute animated explainer that builds the whole economy up from a single transaction, then reduces it to three forces: productivity growth plus a short-term and a long-term debt cycle.",
      why:
        "The clearest mental model for why economies expand, overheat, and deleverage — and a working vocabulary (credit, spending, deleveraging) for almost any macro headline.",
      bio:
        "Founder of Bridgewater Associates, the world's largest hedge fund, and one of the most influential macro thinkers alive.",
      primaryLabel: "WATCH",
      primaryLinks: ["youtu.be/PHe0bXAIuk0"],
      further: ["Book: Principles", "Pairs with The Changing World Order (next)"],
    },
    {
      icon: FaLandmark, tag: "ECONOMICS", format: "VIDEO",
      image: "C:/GitHub/shidler/docs/presentations/assets/xguam0TKMw8.jpg",
      railTitle: "The Changing World Order",
      author: "Ray Dalio",
      overview:
        "Dalio zooms out across 500 years to study how empires and reserve currencies rise and fall — the recurring pattern of debt, internal conflict, and shifting power — and where the US and China sit in that cycle today.",
      why:
        "Frames today's events — debt, inflation, US–China rivalry — inside a repeatable historical arc, so you can read geopolitics as cycles rather than noise.",
      bio:
        "Founder of Bridgewater Associates, the world's largest hedge fund, and one of the most influential macro thinkers alive.",
      primaryLabel: "WATCH",
      primaryLinks: ["youtu.be/xguam0TKMw8"],
      further: ["Book: Principles for Dealing with the Changing World Order", "Pairs with the Economic Machine (prev)"],
    },
    {
      icon: FaBitcoin, tag: "ECONOMICS & CRYPTO", format: "VIDEO",
      image: "C:/GitHub/shidler/docs/presentations/assets/I6IraYngzgo.jpg",
      railTitle: "The Everything Code",
      author: "Raoul Pal",
      overview:
        "Raoul Pal and Julien Bittel lay out a framework tying global liquidity, demographics, and technology adoption to asset prices — a bridge between traditional macro and digital assets.",
      why:
        "Explains why liquidity cycles drive risk markets and offers a lens for thinking about crypto alongside stocks and bonds rather than in isolation.",
      bio:
        "Former Goldman Sachs and GLG hedge-fund manager; co-founder of Real Vision and CEO of Global Macro Investor.",
      primaryLabel: "WATCH",
      primaryLinks: ["youtu.be/I6IraYngzgo"],
      further: ["Real Vision interviews", "Global Macro Investor research"],
    },
    {
      icon: FaRobot, tag: "ARTIFICIAL INTELLIGENCE", format: "VIDEO",
      image: "C:/GitHub/shidler/docs/presentations/assets/MFzxIT88zfg.jpg",
      railTitle: "Build It With AI, Then Attack It",
      author: "Nate Jones",
      overview:
        "A hands-on demo: Jones builds a slide deck with one AI, then sets a second AI to adversarially critique and \"attack\" it — surfacing weaknesses the first pass missed.",
      why:
        "A practical, repeatable template for raising the quality of any AI output: generate, then stress-test. Directly applicable to how you'll use AI on your own projects.",
      bio:
        "AI product strategist and educator known for accessible, applied breakdowns of real AI workflows.",
      primaryLabel: "WATCH",
      primaryLinks: ["youtu.be/MFzxIT88zfg"],
      further: ["Nate's channel & newsletter on applied AI workflows"],
    },
    {
      icon: FaCode, tag: "TOOLS & PROCESS", format: "GITHUB REPO",
      avatar: "C:/GitHub/shidler/docs/presentations/assets/garrytan.jpg",
      railTitle: "gstack",
      author: "Garry Tan",
      overview:
        "An open-source collection of ~23 specialized AI tools that turn Claude Code into a virtual engineering team — letting a solo builder ship at the pace of a much larger team.",
      why:
        "Shows that structured tooling, not just raw prompting, multiplies what you can build with AI. A concrete starting point for your own workflow.",
      bio:
        "Garry Tan — President & CEO of Y Combinator; early Palantir engineer and co-founder of Posterous (acquired by Twitter).",
      primaryLabel: "EXPLORE",
      primaryLinks: ["github.com/garrytan/gstack"],
      further: ["Pair with Karpathy's skills (next)", "Adapt the tools to your own projects"],
    },
    {
      icon: FaCode, tag: "TOOLS & PROCESS", format: "GITHUB REPO",
      avatar: "C:/GitHub/shidler/docs/presentations/assets/karpathy.jpg",
      railTitle: "Karpathy's AI Skills",
      author: "Andrej Karpathy",
      overview:
        "A set of reusable AI \"skills\" that distill disciplined working principles — think before editing, simplicity first, surgical changes, goal-driven verification — into instructions an AI agent follows. The same principles shape this course's own CLAUDE.md.",
      why:
        "Process beats raw effort. Codifying how you work makes AI output more consistent, reviewable, and professional.",
      bio:
        "Andrej Karpathy — founding member of OpenAI, former Sr. Director of AI at Tesla, and a leading AI educator.",
      primaryLabel: "EXPLORE",
      primaryLinks: ["github.com/multica-ai/andrej-karpathy-skills"],
      further: ["Read the CLAUDE.md guidelines", "Apply the principles to your own repo"],
    },
  ];

  // Pre-render icons
  const railIcons = [];
  for (const t of topics) railIcons.push(await iconPng(t.icon, "#" + GREEN));

  // Title-slide category chips (fixed set, independent of topic count)
  const chips = [
    { icon: FaBook, label: "Good Reads" },
    { icon: FaLandmark, label: "Economics" },
    { icon: FaBitcoin, label: "Econ & Crypto" },
    { icon: FaRobot, label: "AI" },
    { icon: FaCode, label: "Tools & Process" },
  ];
  const chipIcons = [];
  for (const c of chips) chipIcons.push(await iconPng(c.icon, "#" + GREEN));
  const playIcon = await iconPng(FaPlay, "#" + WHITE);

  // Precompute aspect ratios for any portrait cover images
  for (const t of topics) {
    if (t.cover) {
      const m = await sharp(t.cover).metadata();
      t._coverAR = m.width / m.height; // width / height
    }
  }

  // ===================== TITLE SLIDE =====================
  {
    const s = pres.addSlide();
    s.background = { color: GREEN };
    // subtle darker block on right for depth
    s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 13.3, h: 7.5, fill: { color: GREEN } });

    s.addText("FURTHER STUDY", {
      x: 0.9, y: 1.7, w: 11.5, h: 1.1, margin: 0,
      fontFace: FACE, fontSize: 54, bold: true, color: WHITE, charSpacing: 1,
    });
    s.addText("Recommended reads, videos & repos — go deeper on your own", {
      x: 0.92, y: 2.85, w: 11.5, h: 0.6, margin: 0,
      fontFace: FACE, fontSize: 19, color: GREEN_100,
    });

    // topic chips row
    const chipW = 2.3, step = 2.5, startX = 0.5;
    for (let i = 0; i < chips.length; i++) {
      const xi = startX + i * step;
      const cd = 0.95, circleX = xi + (chipW - cd) / 2, circleY = 4.55;
      s.addShape(pres.shapes.OVAL, { x: circleX, y: circleY, w: cd, h: cd, fill: { color: WHITE } });
      s.addImage({ data: chipIcons[i], x: circleX + 0.26, y: circleY + 0.26, w: 0.43, h: 0.43 });
      s.addText(chips[i].label, {
        x: xi, y: circleY + cd + 0.12, w: chipW, h: 0.4, margin: 0, align: "center",
        fontFace: FACE, fontSize: 12.5, bold: true, color: WHITE,
      });
    }

    s.addText("Shidler College of Business  ·  University of Hawaiʻi at Mānoa  ·  Adam W. Stauffer", {
      x: 0.9, y: 6.75, w: 11.5, h: 0.4, margin: 0,
      fontFace: FACE, fontSize: 11, italic: true, color: GREEN_300,
    });
  }

  // ===================== TOPIC SLIDES =====================
  const RAIL_W = 4.4;
  const CX = 4.85;            // content left x
  const CW = 7.95;            // content width

  function sectionHeader(s, y, text) {
    s.addText(text, {
      x: CX, y, w: CW, h: 0.32, margin: 0,
      fontFace: FACE, fontSize: 13, bold: true, color: GREEN, charSpacing: 1,
    });
  }
  function body(s, y, h, text, color = BLACK, size = 12) {
    s.addText(text, {
      x: CX, y, w: CW, h, margin: 0, valign: "top",
      fontFace: FACE, fontSize: size, color, lineSpacingMultiple: 1.05,
    });
  }

  topics.forEach((t, idx) => {
    const s = pres.addSlide();
    s.background = { color: WHITE };

    // ---- Left green rail ----
    s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: RAIL_W, h: 7.5, fill: { color: GREEN } });

    let tagY = 2.62, titleY = 3.0;
    if (t.image) {
      // ---- Experimental: video thumbnail hero (16:9) with play badge ----
      const tw = 3.7, th = tw * 9 / 16, tx = (RAIL_W - tw) / 2, ty = 0.55;
      s.addShape(pres.shapes.RECTANGLE, {
        x: tx - 0.06, y: ty - 0.06, w: tw + 0.12, h: th + 0.12,
        fill: { color: WHITE }, shadow: makeShadow(),
      });
      s.addImage({ path: t.image, x: tx, y: ty, w: tw, h: th, sizing: { type: "cover", w: tw, h: th } });
      // play badge
      const pd = 0.78, pcx = RAIL_W / 2 - pd / 2, pcy = ty + th / 2 - pd / 2;
      s.addShape(pres.shapes.OVAL, { x: pcx - 0.05, y: pcy - 0.05, w: pd + 0.1, h: pd + 0.1, fill: { color: WHITE } });
      s.addShape(pres.shapes.OVAL, { x: pcx, y: pcy, w: pd, h: pd, fill: { color: GREEN } });
      s.addImage({ data: playIcon, x: pcx + 0.3, y: pcy + 0.25, w: 0.24, h: 0.28 });
      tagY = 2.82; titleY = 3.2;
    } else if (t.cover) {
      // ---- Experimental: portrait book cover ----
      const ch = 2.35, cw = ch * t._coverAR, cx = (RAIL_W - cw) / 2, cy = 0.55;
      s.addShape(pres.shapes.RECTANGLE, {
        x: cx - 0.05, y: cy - 0.05, w: cw + 0.1, h: ch + 0.1,
        fill: { color: WHITE }, shadow: makeShadow(),
      });
      s.addImage({ path: t.cover, x: cx, y: cy, w: cw, h: ch });
      tagY = 3.05; titleY = 3.43;
    } else if (t.avatar) {
      // ---- Circular author avatar (GitHub repos) ----
      const ad = 1.95, ax = (RAIL_W - ad) / 2, ay = 0.78;
      s.addShape(pres.shapes.OVAL, {
        x: ax - 0.07, y: ay - 0.07, w: ad + 0.14, h: ad + 0.14,
        fill: { color: WHITE }, shadow: makeShadow(),
      });
      s.addImage({ path: t.avatar, x: ax, y: ay, w: ad, h: ad, rounding: true });
      tagY = 3.05; titleY = 3.43;
    } else {
      // icon circle
      const cd = 1.5, circleX = (RAIL_W - cd) / 2, circleY = 0.85;
      s.addShape(pres.shapes.OVAL, { x: circleX, y: circleY, w: cd, h: cd, fill: { color: WHITE } });
      s.addImage({ data: railIcons[idx], x: circleX + 0.42, y: circleY + 0.42, w: 0.66, h: 0.66 });
    }

    // category tag
    s.addText(t.tag, {
      x: 0.35, y: tagY, w: RAIL_W - 0.7, h: 0.32, margin: 0, align: "center",
      fontFace: FACE, fontSize: 12, bold: true, color: GREEN_100, charSpacing: 1.5,
    });
    // rail title
    s.addText(t.railTitle, {
      x: 0.35, y: titleY, w: RAIL_W - 0.7, h: 1.5, margin: 0, align: "center", valign: "top",
      fontFace: FACE, fontSize: 25, bold: true, color: WHITE, lineSpacingMultiple: 0.98,
    });
    // author
    s.addText(t.author, {
      x: 0.35, y: 4.75, w: RAIL_W - 0.7, h: 0.5, margin: 0, align: "center",
      fontFace: FACE, fontSize: 14, italic: true, color: GREEN_100,
    });

    // format pill
    const pillW = 2.4, pillX = (RAIL_W - pillW) / 2;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: pillX, y: 6.45, w: pillW, h: 0.46, fill: { color: GREEN_700 }, rectRadius: 0.23,
    });
    s.addText(t.format, {
      x: pillX, y: 6.45, w: pillW, h: 0.46, margin: 0, align: "center", valign: "middle",
      fontFace: FACE, fontSize: 11.5, bold: true, color: WHITE, charSpacing: 1.5,
    });

    // ---- Right content ----
    sectionHeader(s, 0.7, "OVERVIEW");
    body(s, 1.04, 1.25, t.overview);

    sectionHeader(s, 2.42, "WHY IT MATTERS");
    body(s, 2.76, 1.1, t.why);

    sectionHeader(s, 4.0, "ABOUT THE AUTHOR");
    body(s, 4.34, 0.9, t.bio, MUTE);

    // ---- Resource box (bottom-right) ----
    const boxY = 5.35, boxH = 1.78;
    s.addShape(pres.shapes.RECTANGLE, { x: CX, y: boxY, w: CW, h: boxH, fill: { color: GREEN_50 } });
    s.addShape(pres.shapes.RECTANGLE, { x: CX, y: boxY, w: 0.09, h: boxH, fill: { color: GREEN } });

    const colGap = 0.35;
    const leftColX = CX + 0.3;
    const leftColW = CW * 0.5 - 0.45;
    const rightColX = CX + CW * 0.5 + 0.1;
    const rightColW = CW * 0.5 - 0.4;

    // divider between columns
    s.addShape(pres.shapes.LINE, {
      x: CX + CW * 0.5, y: boxY + 0.25, w: 0, h: boxH - 0.5,
      line: { color: GREEN_100, width: 1 },
    });

    s.addText(t.primaryLabel, {
      x: leftColX, y: boxY + 0.22, w: leftColW, h: 0.3, margin: 0,
      fontFace: FACE, fontSize: 11, bold: true, color: GREEN, charSpacing: 1.5,
    });
    s.addText(
      t.primaryLinks.map((l, j) => ({ text: l, options: { breakLine: j < t.primaryLinks.length - 1, bullet: false } })),
      {
        x: leftColX, y: boxY + 0.56, w: leftColW, h: boxH - 0.75, margin: 0, valign: "top",
        fontFace: FACE, fontSize: 11, bold: true, color: GREEN_700, lineSpacingMultiple: 1.15,
      }
    );

    s.addText("GO FURTHER", {
      x: rightColX, y: boxY + 0.22, w: rightColW, h: 0.3, margin: 0,
      fontFace: FACE, fontSize: 11, bold: true, color: GREEN, charSpacing: 1.5,
    });
    s.addText(
      t.further.map((l, j) => ({ text: l, options: { bullet: { code: "2022" }, breakLine: true } })),
      {
        x: rightColX, y: boxY + 0.56, w: rightColW, h: boxH - 0.75, margin: 0, valign: "top",
        fontFace: FACE, fontSize: 11, color: BLACK, lineSpacingMultiple: 1.1, paraSpaceAfter: 3,
      }
    );

    // slide number / footer tag on rail bottom edge
    s.addText(`${idx + 1} / ${topics.length}`, {
      x: 0.35, y: 7.05, w: RAIL_W - 0.7, h: 0.3, margin: 0, align: "center",
      fontFace: FACE, fontSize: 10, color: GREEN_300,
    });
  });

  await pres.writeFile({ fileName: "C:/GitHub/shidler/docs/presentations/Further_Study_Resources.pptx" });
  console.log("written " + (topics.length + 1) + " slides");
})();
