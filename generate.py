import os

ROOT = os.path.dirname(os.path.abspath(__file__))

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def page(title, desc, body, css="", js="", depth=1, home_label="Home", back_href="index.html", back_label="Back to Programs"):
    up = "../" * depth
    style_href = f"{up}assets/style.css" if depth else "assets/style.css"
    home_href = f"{up}index.html" if depth else "index.html"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Practical Programs</title>
<link rel="stylesheet" href="{style_href}">
<style>
{css}
</style>
</head>
<body>
<header class="site-header">
  <a class="brand" href="{home_href}">HTML · CSS · JS Programs</a>
  <nav class="crumbs">
    <a href="{home_href}">{home_label}</a>
    <a href="{back_href}">{back_label}</a>
  </nav>
</header>
<main>
  <h1 class="page-title">{title}</h1>
  <p class="subtitle">{desc}</p>
  <div class="program-box">
{body}
  </div>
  <footer class="page-nav">
    <a href="{home_href}">Home</a>
    <a class="secondary" href="{back_href}">{back_label}</a>
  </footer>
</main>
<script>
{js}
</script>
</body>
</html>
"""

def category_index(title, desc, programs, cat_dir):
    items = "\n".join(
        f'    <li><a href="{p["slug"]}.html">{p["title"]}</a></li>' for p in programs
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Practical Programs</title>
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<header class="site-header">
  <a class="brand" href="../index.html">HTML · CSS · JS Programs</a>
  <nav class="crumbs"><a href="../index.html">Home</a></nav>
</header>
<main>
  <h1 class="page-title">{title}</h1>
  <p class="subtitle">{desc} &mdash; {len(programs)} programs</p>
  <ul class="program-list">
{items}
  </ul>
  <footer class="page-nav">
    <a href="../index.html">Home</a>
  </footer>
</main>
</body>
</html>
"""

# ---------------------------------------------------------------
# HTML PROGRAMS
# ---------------------------------------------------------------
html_programs = [
dict(slug="basic-page", title="Headings, Paragraphs & Line Breaks",
     desc="Demonstrates the six heading levels, paragraphs, and manual line breaks.",
     body="""
    <h1>Heading Level 1</h1>
    <h2>Heading Level 2</h2>
    <h3>Heading Level 3</h3>
    <h4>Heading Level 4</h4>
    <h5>Heading Level 5</h5>
    <h6>Heading Level 6</h6>
    <p>This is a normal paragraph of text used to demonstrate how the
    <code>&lt;p&gt;</code> element wraps content and adds spacing automatically.</p>
    <p>Here is a second paragraph.<br>
    This line was forced onto a new line using the <code>&lt;br&gt;</code> tag,<br>
    and so was this one.</p>
"""),
dict(slug="lists", title="Ordered, Unordered & Description Lists",
     desc="Shows the three core HTML list types.",
     body="""
    <h3>Unordered List</h3>
    <ul>
      <li>HTML</li>
      <li>CSS</li>
      <li>JavaScript</li>
    </ul>
    <h3>Ordered List</h3>
    <ol>
      <li>Plan the page</li>
      <li>Write the markup</li>
      <li>Style with CSS</li>
      <li>Add JavaScript behaviour</li>
    </ol>
    <h3>Description List</h3>
    <dl>
      <dt>HTML</dt><dd>HyperText Markup Language — structures content.</dd>
      <dt>CSS</dt><dd>Cascading Style Sheets — styles content.</dd>
      <dt>JS</dt><dd>JavaScript — adds interactivity.</dd>
    </dl>
"""),
dict(slug="tables", title="Tables with Rows, Columns, Borders & Merged Cells",
     desc="A table demonstrating colspan and rowspan.",
     body="""
    <table class="demo-table" border="1">
      <tr><th colspan="3">Semester Marks</th></tr>
      <tr><th>Subject</th><th>Internal</th><th>External</th></tr>
      <tr><td>HTML</td><td>18</td><td>72</td></tr>
      <tr><td>CSS</td><td>19</td><td>75</td></tr>
      <tr><td rowspan="2">JavaScript</td><td>20</td><td>78</td></tr>
      <tr><td>(Practical)</td><td>25/25</td></tr>
    </table>
"""),
dict(slug="images-links", title="Images and Hyperlinks",
     desc="Demonstrates embedding an image and different types of hyperlinks.",
     body="""
    <img src="https://picsum.photos/seed/practical/320/180" alt="Random demo image" style="border-radius:10px;max-width:100%;">
    <p><a href="https://developer.mozilla.org" target="_blank" rel="noopener">External link (opens in new tab)</a></p>
    <p><a href="#bottom">Internal link (jumps to bottom of this page)</a></p>
    <p><a href="mailto:student@example.com">Email link</a></p>
    <p id="bottom">You have reached the bottom of the page via the internal link above.</p>
"""),
dict(slug="registration-form", title="Student Registration Form",
     desc="A registration form built with common HTML form elements.",
     body="""
    <form class="demo-form" onsubmit="return false;">
      <label>Full Name<input type="text" required></label>
      <label>Email<input type="email" required></label>
      <label>Date of Birth<input type="date"></label>
      <label>Gender
        <select>
          <option>Male</option><option>Female</option><option>Other</option>
        </select>
      </label>
      <label>Course
        <input list="courses"><datalist id="courses">
          <option value="B.Sc Computer Science">
          <option value="B.Tech IT">
        </datalist>
      </label>
      <label><input type="checkbox"> I agree to the terms and conditions</label>
      <label><input type="radio" name="mode" checked> Regular</label>
      <label><input type="radio" name="mode"> Distance</label>
      <button class="btn" type="submit">Register</button>
    </form>
"""),
dict(slug="audio-video", title="Audio and Video Elements",
     desc="Embeds native HTML5 audio and video players with controls.",
     body="""
    <h3>Video</h3>
    <video controls width="100%" style="border-radius:10px;max-width:480px;" poster="https://picsum.photos/seed/video/480/270">
      <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <h3>Audio</h3>
    <audio controls>
      <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3" type="audio/mpeg">
      Your browser does not support the audio tag.
    </audio>
"""),
dict(slug="iframe", title="Frames / Iframes",
     desc="Embeds another web page inside the current page using an iframe.",
     body="""
    <iframe src="https://en.wikipedia.org/wiki/HTML" title="Wikipedia HTML article"
      width="100%" height="360" style="border:1px solid #2b3050;border-radius:10px;"></iframe>
"""),
dict(slug="semantic-elements", title="Semantic Elements",
     desc="Demonstrates header, nav, section, article, and footer.",
     body="""
    <div class="demo-area">
      <header><strong>Page Header</strong> — site title / logo area</header>
      <nav>Nav: <a href="#">Home</a> | <a href="#">About</a> | <a href="#">Contact</a></nav>
      <section>
        <h3>Section: Blog</h3>
        <article>
          <h4>Article 1</h4>
          <p>Semantic elements describe the meaning of content, not just its appearance.</p>
        </article>
        <article>
          <h4>Article 2</h4>
          <p>They improve accessibility and SEO.</p>
        </article>
      </section>
      <footer>&copy; 2026 Practical Programs Footer</footer>
    </div>
"""),
dict(slug="input-types", title="HTML5 Input Types",
     desc="Showcases email, date, number, password, and other HTML5 inputs.",
     body="""
    <form class="demo-form" onsubmit="return false;">
      <label>Email<input type="email" placeholder="you@example.com"></label>
      <label>Date<input type="date"></label>
      <label>Number<input type="number" min="0" max="10"></label>
      <label>Password<input type="password"></label>
      <label>Range<input type="range" min="0" max="100"></label>
      <label>Color<input type="color"></label>
      <label>Search<input type="search" placeholder="Search..."></label>
      <label>Tel<input type="tel" placeholder="+91 9876543210"></label>
      <label>URL<input type="url" placeholder="https://example.com"></label>
    </form>
"""),
dict(slug="timetable", title="College Timetable",
     desc="A weekly timetable rendered with an HTML table.",
     body="""
    <table class="demo-table">
      <tr><th>Day</th><th>9-10</th><th>10-11</th><th>11-12</th><th>1-2</th></tr>
      <tr><td>Mon</td><td>Maths</td><td>Physics</td><td>CS Lab</td><td>English</td></tr>
      <tr><td>Tue</td><td>CS</td><td>Maths</td><td>Chemistry</td><td>Library</td></tr>
      <tr><td>Wed</td><td>Physics Lab</td><td colspan="2">CS Lab (2 hrs)</td><td>Maths</td></tr>
      <tr><td>Thu</td><td>English</td><td>CS</td><td>Physics</td><td>Sports</td></tr>
      <tr><td>Fri</td><td>Maths</td><td>Chemistry</td><td>CS</td><td>Seminar</td></tr>
    </table>
"""),
dict(slug="internal-external-css", title="Internal & External CSS",
     desc="Demonstrates styling using an internal &lt;style&gt; block plus the shared external stylesheet.",
     css="""
    .internal-demo { color: var(--accent-2); border: 2px dashed var(--accent); padding: 14px; border-radius: 10px; }
""",
     body="""
    <p>This whole site already uses an <strong>external</strong> stylesheet (<code>assets/style.css</code>).</p>
    <div class="internal-demo">This box is styled by an <strong>internal</strong> &lt;style&gt; block defined inside this page's &lt;head&gt;.</div>
    <p style="margin-top:14px;">This sentence uses <strong>inline</strong> CSS: <span style="color:orange;font-weight:bold;">orange bold text</span>.</p>
"""),
dict(slug="css-selectors-demo", title="Selectors, Colors, Fonts, Margins, Padding, Borders",
     desc="A single page combining several fundamental CSS properties.",
     css="""
    .box1 { color:#fff;background:#7c5cff;font-family:Georgia,serif;margin:14px 0;padding:16px;border:4px solid #35d0ba;border-radius:8px; }
    .box2 { font-family:'Courier New',monospace;font-weight:bold;margin:14px 0;padding:10px 30px;border:2px dotted #ff7676; }
""",
     body="""
    <div class="box1">Styled with class selector: custom color, font, margin, padding, border.</div>
    <div class="box2" id="uniqueBox">Styled with an ID selector layered on a class selector.</div>
"""),
dict(slug="media-query-demo", title="Responsive Page with Media Queries",
     desc="Layout changes from 3 columns to 1 column as the viewport shrinks. Resize the browser to see it react.",
     css="""
    .grid3 { display:grid; grid-template-columns: repeat(3, 1fr); gap:14px; }
    .grid3 div { background:var(--bg-soft); border:1px solid var(--border); padding:20px; border-radius:10px; text-align:center; }
    @media (max-width: 700px) {
      .grid3 { grid-template-columns: 1fr; }
      .grid3 div { background:#2a1e3e; }
    }
""",
     body="""
    <div class="grid3">
      <div>Column 1</div><div>Column 2</div><div>Column 3</div>
    </div>
    <p style="margin-top:12px;">Below 700px width the grid collapses to a single column and the boxes change colour.</p>
"""),
dict(slug="bootstrap-demo", title="Bootstrap Components",
     desc="A few Bootstrap components loaded from the CDN: buttons, alert, and a card.",
     body="""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.3/css/bootstrap.min.css">
    <div style="background:#fff;color:#111;padding:20px;border-radius:10px;">
      <button class="btn btn-primary me-2">Primary</button>
      <button class="btn btn-success me-2">Success</button>
      <button class="btn btn-danger">Danger</button>
      <div class="alert alert-info mt-3" role="alert">This is a Bootstrap alert component.</div>
      <div class="card mt-3" style="width: 18rem;">
        <div class="card-body">
          <h5 class="card-title">Bootstrap Card</h5>
          <p class="card-text">Cards are a flexible content container.</p>
        </div>
      </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.3/js/bootstrap.bundle.min.js"></script>
"""),
dict(slug="portfolio", title="Simple Personal Portfolio",
     desc="A minimal one-page personal portfolio built with HTML and CSS.",
     css="""
    .portfolio-hero { text-align:center; padding:20px; }
    .portfolio-hero img { width:110px; height:110px; border-radius:50%; border:3px solid var(--accent-2); }
    .skills span { display:inline-block; background:var(--bg-soft); border:1px solid var(--border); padding:6px 14px; border-radius:999px; margin:4px; }
""",
     body="""
    <div class="portfolio-hero">
      <img src="https://i.pravatar.cc/150?img=12" alt="avatar">
      <h2>Jane Student</h2>
      <p>Aspiring Web Developer</p>
    </div>
    <h3>About</h3>
    <p>I am a student learning HTML, CSS, and JavaScript through hands-on practice.</p>
    <h3>Skills</h3>
    <div class="skills"><span>HTML5</span><span>CSS3</span><span>JavaScript</span><span>Responsive Design</span></div>
    <h3>Contact</h3>
    <p>Email: jane@example.com</p>
"""),
]

# ---------------------------------------------------------------
# CSS PROGRAMS
# ---------------------------------------------------------------
css_programs = [
dict(slug="box-model", title="CSS Box Model", desc="Visualising content, padding, border, and margin.",
     css=".boxdemo{width:180px;padding:20px;border:8px solid #7c5cff;margin:30px;background:#35d0ba;color:#04261f;}",
     body='<div class="boxdemo">Content area</div><p>Padding (teal inside border), border (purple), and margin (gap around the box) are all visible above.</p>'),
dict(slug="positioning", title="CSS Positioning", desc="static, relative, absolute, fixed, and sticky positioning compared.",
     css="""
.pos-wrap{position:relative;height:260px;background:var(--bg-soft);border:1px solid var(--border);border-radius:10px;overflow:auto;}
.pos-static{position:static;background:#444;padding:8px;}
.pos-relative{position:relative;top:10px;left:20px;background:#7c5cff;padding:8px;}
.pos-absolute{position:absolute;top:10px;right:10px;background:#35d0ba;color:#04261f;padding:8px;}
.pos-fixed{position:fixed;bottom:16px;right:16px;background:#ff7676;padding:8px;border-radius:8px;z-index:99;}
.pos-sticky{position:sticky;top:0;background:#e6b800;color:#332900;padding:8px;}
""",
     body="""
<div class="pos-wrap">
  <div class="pos-static">static (normal flow)</div>
  <div class="pos-relative">relative (shifted from normal spot)</div>
  <div class="pos-absolute">absolute (relative to wrapper)</div>
  <div class="pos-sticky">sticky (sticks while you scroll this box)</div>
  <p>Scroll inside this box to see the sticky element stay near the top.</p>
  <p style="height:200px;">Extra height to allow scrolling…</p>
</div>
<div class="pos-fixed">fixed (stuck to viewport)</div>
"""),
dict(slug="float-clear", title="Float and Clear", desc="Text wrapping around a floated box, cleared afterwards.",
     css=".float-box{float:left;width:120px;height:120px;background:#7c5cff;margin:0 14px 10px 0;border-radius:10px;}.clearfix{clear:both;}",
     body='<div class="float-box"></div><p>This paragraph text wraps around the floated purple box on the left, the classic use of the <code>float</code> property before Flexbox/Grid existed.</p><div class="clearfix"></div><p>This paragraph appears cleanly below because of <code>clear: both</code>.</p>'),
dict(slug="navbar", title="Styled Navigation Bar", desc="A horizontal navigation bar styled purely with CSS.",
     css="""
.navbar{display:flex;background:var(--bg-soft);border-radius:10px;overflow:hidden;}
.navbar a{flex:1;text-align:center;padding:14px;color:var(--text);text-decoration:none;border-right:1px solid var(--border);}
.navbar a:last-child{border-right:none;}
.navbar a:hover{background:var(--accent);color:#fff;}
""",
     body='<nav class="navbar"><a href="#">Home</a><a href="#">About</a><a href="#">Services</a><a href="#">Contact</a></nav>'),
dict(slug="pseudo-classes", title="Pseudo-classes", desc=":hover, :active, :focus, and :visited demonstrated interactively.",
     css="""
.pc-link:visited{color:#c48bff;}
.pc-btn{padding:10px 20px;border-radius:8px;border:2px solid var(--accent-2);background:transparent;color:var(--text);cursor:pointer;}
.pc-btn:hover{background:var(--accent-2);color:#04261f;}
.pc-btn:active{transform:scale(0.95);}
.pc-input:focus{outline:3px solid var(--accent);}
""",
     body='<p><a class="pc-link" href="#">Hover, then click me (:visited changes my colour)</a></p><button class="pc-btn">Hover / Click Me</button><br><br><input class="pc-input" placeholder="Click to focus me">'),
dict(slug="pseudo-elements", title="Pseudo-elements", desc="::before, ::after, ::first-letter, and ::first-line.",
     css="""
.pe-quote::before{content:"\\201C";color:var(--accent-2);font-size:1.4em;}
.pe-quote::after{content:"\\201D";color:var(--accent-2);font-size:1.4em;}
.pe-para::first-letter{font-size:2.2em;color:var(--accent);font-weight:bold;}
.pe-para::first-line{color:var(--accent-2);}
""",
     body='<p class="pe-quote">Design is not just what it looks like, design is how it works.</p><p class="pe-para">This paragraph demonstrates first-letter and first-line styling. The very first line is coloured differently from the rest of the paragraph, which continues in the normal text colour after the first line wraps.</p>'),
dict(slug="lists-tables-css", title="Styling Lists and Tables", desc="Custom list markers and a fully styled table.",
     css="""
.cl-list{list-style:none;padding-left:0;}
.cl-list li{padding:8px 0 8px 28px;border-bottom:1px solid var(--border);position:relative;}
.cl-list li::before{content:"\\2714";color:var(--accent-2);position:absolute;left:0;}
.cl-table{width:100%;border-collapse:collapse;}
.cl-table th{background:var(--accent);color:#fff;padding:10px;}
.cl-table td{padding:10px;border-bottom:1px solid var(--border);}
.cl-table tr:nth-child(even){background:var(--bg-soft);}
""",
     body="""
<ul class="cl-list"><li>Checklist item one</li><li>Checklist item two</li><li>Checklist item three</li></ul>
<table class="cl-table"><tr><th>Item</th><th>Qty</th></tr><tr><td>Pens</td><td>10</td></tr><tr><td>Books</td><td>5</td></tr><tr><td>Files</td><td>3</td></tr></table>
"""),
dict(slug="styled-registration-form", title="Styled Registration Form", desc="A registration form fully styled with CSS.",
     body="""
<form class="demo-form" onsubmit="return false;">
  <label>Name<input type="text" required></label>
  <label>Email<input type="email" required></label>
  <label>Password<input type="password" required></label>
  <button class="btn" type="submit">Create Account</button>
</form>
"""),
dict(slug="flexbox", title="CSS Flexbox", desc="Row/column direction, justify-content, and align-items.",
     css=".flex-demo{display:flex;justify-content:space-around;align-items:center;height:140px;background:var(--bg-soft);border-radius:10px;}.flex-demo div{background:var(--accent);padding:16px 22px;border-radius:8px;}",
     body='<div class="flex-demo"><div>Item 1</div><div>Item 2</div><div>Item 3</div></div>'),
dict(slug="grid-layout", title="CSS Grid Layout", desc="A responsive grid using grid-template-columns.",
     css=".grid-demo{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;}.grid-demo div{background:var(--accent-2);color:#04261f;padding:20px;text-align:center;border-radius:8px;}",
     body='<div class="grid-demo"><div>1</div><div>2</div><div>3</div><div>4</div><div>5</div><div>6</div><div>7</div><div>8</div></div>'),
dict(slug="transitions-transforms", title="Transitions & Transformations", desc="Hover to see smooth transitions and 2D transforms.",
     css=".tt-box{width:100px;height:100px;background:var(--accent);border-radius:10px;transition:all 0.4s ease;}.tt-box:hover{transform:rotate(20deg) scale(1.2);background:var(--accent-2);}",
     body='<div class="tt-box"></div><p>Hover over the box to see it rotate and scale smoothly.</p>'),
dict(slug="animations", title="CSS Keyframe Animations", desc="An infinite bouncing animation using @keyframes.",
     css="""
@keyframes bounce{0%,100%{transform:translateY(0);}50%{transform:translateY(-30px);}}
.bounce-ball{width:50px;height:50px;border-radius:50%;background:var(--accent-2);animation:bounce 1s infinite ease-in-out;}
""",
     body='<div class="bounce-ball"></div>'),
dict(slug="login-page", title="Login Page", desc="A centred login card styled with HTML and CSS.",
     css=".login-card{max-width:320px;margin:0 auto;background:var(--bg-soft);padding:30px;border-radius:14px;border:1px solid var(--border);}",
     body="""
<div class="login-card">
  <h2 style="text-align:center;">Sign In</h2>
  <form class="demo-form" onsubmit="return false;">
    <label>Username<input type="text"></label>
    <label>Password<input type="password"></label>
    <button class="btn" style="width:100%;" type="submit">Login</button>
  </form>
</div>
"""),
dict(slug="product-card", title="Product Card Layout", desc="An e-commerce style product card.",
     css="""
.pcard{max-width:260px;background:var(--bg-soft);border:1px solid var(--border);border-radius:12px;overflow:hidden;}
.pcard img{width:100%;display:block;}
.pcard .pbody{padding:16px;}
.pcard .price{color:var(--accent-2);font-weight:bold;font-size:1.2rem;}
""",
     body="""
<div class="pcard">
  <img src="https://picsum.photos/seed/shoe/300/200" alt="product">
  <div class="pbody">
    <h3>Running Shoes</h3>
    <p class="price">₹2,499</p>
    <button class="btn">Add to Cart</button>
  </div>
</div>
"""),
dict(slug="photo-gallery", title="Responsive Photo Gallery", desc="A responsive gallery built with CSS Grid.",
     css=".gallery{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;}.gallery img{width:100%;height:120px;object-fit:cover;border-radius:8px;}",
     body='<div class="gallery">'+ "".join(f'<img src="https://picsum.photos/seed/g{i}/300/200" alt="photo {i}">' for i in range(1,9)) +'</div>'),
dict(slug="gradients", title="Linear & Radial Gradients", desc="Two boxes demonstrating gradient backgrounds.",
     css=".grad1{height:120px;border-radius:10px;background:linear-gradient(90deg,#7c5cff,#35d0ba);margin-bottom:14px;}.grad2{height:120px;border-radius:10px;background:radial-gradient(circle,#ff7676,#2b0a0a);}",
     body='<div class="grad1"></div><div class="grad2"></div>'),
dict(slug="shadows", title="Box Shadow & Text Shadow", desc="Demonstrates elevation via box-shadow and text-shadow.",
     css=".shadow-box{width:160px;height:100px;background:var(--bg-soft);border-radius:10px;box-shadow:0 12px 30px rgba(124,92,255,0.5);}.shadow-text{font-size:2rem;text-shadow:2px 2px 6px #000;color:var(--accent-2);}",
     body='<div class="shadow-box"></div><p class="shadow-text">Shadowed Text</p>'),
dict(slug="border-radius-shapes", title="Shapes with Border Radius", desc="Circle, ellipse, and rounded rectangle using border-radius.",
     css=".shape{display:inline-block;width:100px;height:100px;background:var(--accent);margin-right:14px;}.circle{border-radius:50%;}.rounded{border-radius:20px;}.pill{width:160px;height:60px;border-radius:999px;background:var(--accent-2);}",
     body='<div class="shape circle"></div><div class="shape rounded"></div><div class="shape pill"></div>'),
dict(slug="css-variables", title="CSS Custom Properties", desc="Reusable CSS variables changed live with JavaScript.",
     css=":root{--theme-color:#7c5cff;}.var-box{background:var(--theme-color);padding:20px;border-radius:10px;color:#fff;transition:background 0.3s;}",
     js="""
function changeTheme(color){document.documentElement.style.setProperty('--theme-color', color);}
""",
     body="""
<div class="var-box" id="varBox">This box uses a CSS variable for its background.</div>
<div style="margin-top:12px;">
  <button class="btn" onclick="changeTheme('#35d0ba')">Teal</button>
  <button class="btn" onclick="changeTheme('#ff7676')">Red</button>
  <button class="btn" onclick="changeTheme('#e6b800')">Gold</button>
</div>
"""),
dict(slug="sticky-header", title="Sticky Header", desc="A header that sticks to the top while scrolling a container.",
     css=".sticky-wrap{height:260px;overflow-y:auto;border:1px solid var(--border);border-radius:10px;}.sticky-hd{position:sticky;top:0;background:var(--accent);padding:12px;color:#fff;}",
     body='<div class="sticky-wrap"><div class="sticky-hd">I stick to the top</div><p style="padding:14px;">'+ "Scroll down inside this box. " * 40 +'</p></div>'),
dict(slug="dropdown-menu", title="Dropdown Menu", desc="A pure-CSS dropdown menu revealed on hover.",
     css="""
.dropdown{position:relative;display:inline-block;}
.dropdown-content{display:none;position:absolute;background:var(--bg-soft);border:1px solid var(--border);border-radius:8px;min-width:160px;overflow:hidden;}
.dropdown-content a{display:block;padding:10px 14px;color:var(--text);text-decoration:none;}
.dropdown-content a:hover{background:var(--accent);}
.dropdown:hover .dropdown-content{display:block;}
""",
     body='<div class="dropdown"><button class="btn">Hover Me</button><div class="dropdown-content"><a href="#">Option 1</a><a href="#">Option 2</a><a href="#">Option 3</a></div></div>'),
dict(slug="dark-mode", title="Dark Mode Toggle", desc="Switch between light and dark themes using CSS variables.",
     css="""
.dm-wrap{--dm-bg:#1e2338;--dm-text:#eef0f8;background:var(--dm-bg);color:var(--dm-text);padding:24px;border-radius:12px;transition:0.3s;}
.dm-wrap.light{--dm-bg:#f4f4f8;--dm-text:#111;}
""",
     js="function toggleDark(){document.getElementById('dmWrap').classList.toggle('light');}",
     body='<div class="dm-wrap" id="dmWrap"><p>This panel switches theme.</p><button class="btn" onclick="toggleDark()">Toggle Light / Dark</button></div>'),
]

# ---------------------------------------------------------------
# JAVASCRIPT PROGRAMS
# ---------------------------------------------------------------
js_programs = [
dict(slug="hello-world", title="Hello World", desc="Displays 'Hello, World!' using JavaScript.",
     body='<button class="btn" onclick="run()">Run</button><div class="output-box" id="out"></div>',
     js="function run(){document.getElementById('out').textContent='Hello, World!';}"),
dict(slug="arithmetic", title="Arithmetic Operations", desc="Performs +, -, *, /, % on two numbers entered by the user.",
     body="""
<form class="demo-form" onsubmit="return false;">
  <label>Number A<input id="a" type="number" value="8"></label>
  <label>Number B<input id="b" type="number" value="3"></label>
  <button class="btn" onclick="calc()">Calculate</button>
</form>
<div class="output-box" id="out"></div>
""",
     js="""
function calc(){
  const a=Number(document.getElementById('a').value);
  const b=Number(document.getElementById('b').value);
  document.getElementById('out').textContent =
    `Sum: ${a+b}\\nDifference: ${a-b}\\nProduct: ${a*b}\\nQuotient: ${(a/b).toFixed(2)}\\nRemainder: ${a%b}`;
}
"""),
dict(slug="largest-of-three", title="Largest of Three Numbers", desc="Finds the largest of three user-supplied numbers.",
     body="""
<form class="demo-form" onsubmit="return false;">
  <label>A<input id="a" type="number" value="4"></label>
  <label>B<input id="b" type="number" value="9"></label>
  <label>C<input id="c" type="number" value="7"></label>
  <button class="btn" onclick="findLargest()">Find Largest</button>
</form>
<div class="output-box" id="out"></div>
""",
     js="""
function findLargest(){
  const a=Number(document.getElementById('a').value);
  const b=Number(document.getElementById('b').value);
  const c=Number(document.getElementById('c').value);
  document.getElementById('out').textContent = 'Largest: ' + Math.max(a,b,c);
}
"""),
dict(slug="factorial", title="Factorial of a Number", desc="Calculates n! using a loop.",
     body='<form class="demo-form" onsubmit="return false;"><label>Number<input id="n" type="number" value="5"></label><button class="btn" onclick="fact()">Calculate</button></form><div class="output-box" id="out"></div>',
     js="""
function fact(){
  let n=Number(document.getElementById('n').value), result=1;
  for(let i=2;i<=n;i++) result*=i;
  document.getElementById('out').textContent = `${n}! = ${result}`;
}
"""),
dict(slug="fibonacci", title="Fibonacci Series", desc="Generates the Fibonacci sequence up to N terms.",
     body='<form class="demo-form" onsubmit="return false;"><label>Terms<input id="n" type="number" value="10"></label><button class="btn" onclick="fib()">Generate</button></form><div class="output-box" id="out"></div>',
     js="""
function fib(){
  const n=Number(document.getElementById('n').value);
  let seq=[0,1];
  for(let i=2;i<n;i++) seq.push(seq[i-1]+seq[i-2]);
  document.getElementById('out').textContent = seq.slice(0,n).join(', ');
}
"""),
dict(slug="prime-check", title="Prime Number Check", desc="Checks whether a given number is prime.",
     body='<form class="demo-form" onsubmit="return false;"><label>Number<input id="n" type="number" value="29"></label><button class="btn" onclick="check()">Check</button></form><div class="output-box" id="out"></div>',
     js="""
function check(){
  const n=Number(document.getElementById('n').value);
  let isPrime = n>1;
  for(let i=2;i*i<=n;i++){ if(n%i===0){isPrime=false;break;} }
  document.getElementById('out').textContent = `${n} is ${isPrime?'a PRIME':'NOT a prime'} number.`;
}
"""),
dict(slug="palindrome-number", title="Palindrome Number Check", desc="Checks whether a number reads the same backwards.",
     body='<form class="demo-form" onsubmit="return false;"><label>Number<input id="n" type="number" value="12321"></label><button class="btn" onclick="check()">Check</button></form><div class="output-box" id="out"></div>',
     js="""
function check(){
  const raw = document.getElementById('n').value;
  const reversed = raw.split('').reverse().join('');
  document.getElementById('out').textContent = raw === reversed ? `${raw} IS a palindrome.` : `${raw} is NOT a palindrome.`;
}
"""),
dict(slug="array-stats", title="Array Largest, Smallest, Sum & Average", desc="Analyses a comma-separated list of numbers.",
     body='<form class="demo-form" onsubmit="return false;"><label>Numbers (comma separated)<input id="arr" value="4,9,1,7,15,3"></label><button class="btn" onclick="stats()">Analyse</button></form><div class="output-box" id="out"></div>',
     js="""
function stats(){
  const nums = document.getElementById('arr').value.split(',').map(Number);
  const sum = nums.reduce((a,b)=>a+b,0);
  document.getElementById('out').textContent =
    `Array: [${nums.join(', ')}]\\nLargest: ${Math.max(...nums)}\\nSmallest: ${Math.min(...nums)}\\nSum: ${sum}\\nAverage: ${(sum/nums.length).toFixed(2)}`;
}
"""),
dict(slug="string-methods", title="String Methods Demo", desc="Demonstrates common string methods: upper, lower, slice, split, replace, includes.",
     body='<form class="demo-form" onsubmit="return false;"><label>Enter text<input id="s" value="Hello JavaScript World"></label><button class="btn" onclick="demo()">Run Methods</button></form><div class="output-box" id="out"></div>',
     js="""
function demo(){
  const s = document.getElementById('s').value;
  document.getElementById('out').textContent =
`Original: ${s}
Uppercase: ${s.toUpperCase()}
Lowercase: ${s.toLowerCase()}
Length: ${s.length}
Reversed: ${s.split('').reverse().join('')}
Includes "Java": ${s.includes('Java')}
Replace "World" -> "Students": ${s.replace('World','Students')}
Words: ${s.split(' ').length}`;
}
"""),
dict(slug="es6-features", title="ES6: let/const, Template Literals, Destructuring", desc="Demonstrates modern JavaScript syntax.",
     body='<button class="btn" onclick="run()">Run Demo</button><div class="output-box" id="out"></div>',
     js="""
function run(){
  const person = {name:'Asha', age:20, city:'Chennai'};
  const {name, age, city} = person;
  const greeting = `Hi, I'm ${name}, age ${age}, from ${city}.`;
  let arr = [1,2,3];
  const [first, ...rest] = arr;
  document.getElementById('out').textContent =
`${greeting}
Destructured array -> first: ${first}, rest: [${rest.join(', ')}]
Spread merge: ${JSON.stringify([...arr, 4, 5])}`;
}
"""),
dict(slug="classes-inheritance", title="Classes, Objects & Inheritance", desc="Demonstrates ES6 classes with an inheriting subclass.",
     body='<button class="btn" onclick="run()">Run Demo</button><div class="output-box" id="out"></div>',
     js="""
class Animal{
  constructor(name){ this.name = name; }
  speak(){ return `${this.name} makes a sound.`; }
}
class Dog extends Animal{
  speak(){ return `${this.name} barks.`; }
}
function run(){
  const a = new Animal('Generic Animal');
  const d = new Dog('Rex');
  document.getElementById('out').textContent = a.speak() + '\\n' + d.speak();
}
"""),
dict(slug="promises-async", title="Callbacks, Promises & Async/Await", desc="Simulates an asynchronous operation three different ways.",
     body='<button class="btn" onclick="run()">Run Async Demo</button><div class="output-box" id="out"></div>',
     js="""
function delay(ms){ return new Promise(resolve => setTimeout(resolve, ms)); }
async function run(){
  const out = document.getElementById('out');
  out.textContent = 'Starting...';
  await delay(600);
  out.textContent += '\\nStep 1 done (after 0.6s, via async/await)';
  await delay(600);
  out.textContent += '\\nStep 2 done (after another 0.6s)';
  out.textContent += '\\nAll async steps finished!';
}
"""),
dict(slug="fetch-api", title="Fetch API Demo", desc="Fetches live data from a public API and displays it.",
     body='<button class="btn" onclick="load()">Fetch a Random Joke</button><div class="output-box" id="out">Click the button to fetch data…</div>',
     js="""
async function load(){
  const out = document.getElementById('out');
  out.textContent = 'Loading...';
  try{
    const res = await fetch('https://official-joke-api.appspot.com/random_joke');
    const data = await res.json();
    out.textContent = `${data.setup}\\n\\n${data.punchline}`;
  }catch(e){
    out.textContent = 'Could not fetch data (no network in this sandbox). This code works in a normal browser with internet access.';
  }
}
"""),
dict(slug="change-text-bg-color", title="Change Text & Background Color", desc="DOM manipulation: change element text and background colour.",
     body="""
<div class="demo-area" id="target">Click a button below to change me!</div>
<div style="margin-top:12px;">
  <button class="btn" onclick="document.getElementById('target').textContent='Text changed by JavaScript!'">Change Text</button>
  <button class="btn" onclick="document.getElementById('target').style.background='#35d0ba'">Teal Background</button>
  <button class="btn" onclick="document.getElementById('target').style.background='#ff7676'">Red Background</button>
</div>
"""),
dict(slug="show-hide-element", title="Show / Hide Element", desc="Toggles the visibility of an element using a button click event.",
     body="""
<button class="btn" onclick="toggle()">Show / Hide</button>
<div class="demo-area" id="box">I can be hidden and shown again.</div>
""",
     js="function toggle(){const b=document.getElementById('box'); b.style.display = (b.style.display==='none') ? 'block' : 'none';}"),
dict(slug="counter-app", title="Counter App", desc="Increment/decrement counter demonstrating click events and DOM updates.",
     body="""
<div class="demo-area" style="text-align:center;">
  <h2 id="count">0</h2>
  <button class="btn" onclick="change(-1)">-</button>
  <button class="btn" onclick="change(1)">+</button>
  <button class="btn" onclick="change(0)">Reset</button>
</div>
""",
     js="""
let count = 0;
function change(delta){
  count = delta === 0 ? 0 : count + delta;
  document.getElementById('count').textContent = count;
}
"""),
dict(slug="digital-clock", title="Digital Clock", desc="A live, continuously updating digital clock.",
     body='<div class="demo-area" style="text-align:center;font-size:2.4rem;letter-spacing:2px;" id="clock">--:--:--</div>',
     js="""
function tick(){
  const now = new Date();
  document.getElementById('clock').textContent = now.toLocaleTimeString();
}
tick();
setInterval(tick, 1000);
"""),
dict(slug="calculator", title="Simple Calculator", desc="A working on-screen calculator built with HTML, CSS, and JavaScript.",
     css="""
.calc{max-width:280px;margin:0 auto;background:var(--bg-soft);padding:14px;border-radius:12px;}
.calc input{width:100%;padding:12px;font-size:1.4rem;text-align:right;border-radius:8px;border:1px solid var(--border);background:#0b0d18;color:var(--text);margin-bottom:10px;}
.calc .row{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;}
.calc button{padding:14px 0;border:none;border-radius:8px;background:var(--accent);color:#fff;font-size:1.1rem;cursor:pointer;}
.calc button.op{background:var(--accent-2);color:#04261f;}
""",
     body="""
<div class="calc">
  <input id="calcScreen" readonly value="0">
  <div class="row">
    <button onclick="press('7')">7</button><button onclick="press('8')">8</button><button onclick="press('9')">9</button><button class="op" onclick="press('/')">÷</button>
    <button onclick="press('4')">4</button><button onclick="press('5')">5</button><button onclick="press('6')">6</button><button class="op" onclick="press('*')">×</button>
    <button onclick="press('1')">1</button><button onclick="press('2')">2</button><button onclick="press('3')">3</button><button class="op" onclick="press('-')">-</button>
    <button onclick="press('0')">0</button><button onclick="press('.')">.</button><button class="op" onclick="calcEval()">=</button><button class="op" onclick="press('+')">+</button>
    <button onclick="clearCalc()" style="grid-column:span 4;background:#ff7676;">Clear</button>
  </div>
</div>
""",
     js="""
let expr = '';
function press(v){ expr += v; document.getElementById('calcScreen').value = expr; }
function clearCalc(){ expr=''; document.getElementById('calcScreen').value = '0'; }
function calcEval(){
  try{ expr = String(Function('"use strict";return ('+expr+')')()); }
  catch(e){ expr = 'Error'; }
  document.getElementById('calcScreen').value = expr;
}
"""),
dict(slug="number-guessing-game", title="Number Guessing Game", desc="Guess a random number between 1 and 100.",
     body="""
<div class="demo-area">
  <p>I'm thinking of a number between 1 and 100.</p>
  <input id="guess" type="number" min="1" max="100">
  <button class="btn" onclick="guess()">Guess</button>
  <button class="btn" onclick="reset()">New Game</button>
  <div class="output-box" id="out">Attempts: 0</div>
</div>
""",
     js="""
let target = Math.floor(Math.random()*100)+1;
let attempts = 0;
function guess(){
  const g = Number(document.getElementById('guess').value);
  attempts++;
  const out = document.getElementById('out');
  if(g === target) out.textContent = `Correct! The number was ${target}. Attempts: ${attempts}`;
  else if(g < target) out.textContent = `Too low. Try again. Attempts: ${attempts}`;
  else out.textContent = `Too high. Try again. Attempts: ${attempts}`;
}
function reset(){ target = Math.floor(Math.random()*100)+1; attempts = 0; document.getElementById('out').textContent = 'Attempts: 0'; }
"""),
dict(slug="form-validation", title="Form Validation", desc="Validates name, email, phone, and password fields with JavaScript.",
     body="""
<form class="demo-form" id="valForm" onsubmit="return validate();">
  <label>Name<input id="fname" type="text"></label>
  <label>Email<input id="femail" type="text"></label>
  <label>Phone (10 digits)<input id="fphone" type="text"></label>
  <label>Password (min 6 chars)<input id="fpass" type="password"></label>
  <button class="btn" type="submit">Submit</button>
</form>
<div class="output-box" id="out"></div>
""",
     js="""
function validate(){
  const name = document.getElementById('fname').value.trim();
  const email = document.getElementById('femail').value.trim();
  const phone = document.getElementById('fphone').value.trim();
  const pass = document.getElementById('fpass').value;
  const errors = [];
  if(name.length < 2) errors.push('Name must be at least 2 characters.');
  if(!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) errors.push('Enter a valid email address.');
  if(!/^\\d{10}$/.test(phone)) errors.push('Phone number must be exactly 10 digits.');
  if(pass.length < 6) errors.push('Password must be at least 6 characters.');
  document.getElementById('out').textContent = errors.length ? errors.join('\\n') : 'All fields are valid! Form would now submit.';
  return false;
}
"""),
dict(slug="todo-list", title="To-Do List", desc="Add, complete, and remove tasks — a classic DOM manipulation mini project.",
     body="""
<div class="demo-area">
  <input id="todoInput" placeholder="Add a new task...">
  <button class="btn" onclick="addTodo()">Add</button>
  <ul id="todoList" style="list-style:none;padding:0;margin-top:14px;"></ul>
</div>
""",
     js="""
function addTodo(){
  const input = document.getElementById('todoInput');
  const text = input.value.trim();
  if(!text) return;
  const li = document.createElement('li');
  li.style.cssText = 'background:var(--bg-soft);padding:10px;margin-bottom:6px;border-radius:8px;display:flex;justify-content:space-between;align-items:center;';
  const span = document.createElement('span');
  span.textContent = text;
  span.style.cursor='pointer';
  span.onclick = () => span.style.textDecoration = span.style.textDecoration === 'line-through' ? 'none' : 'line-through';
  const del = document.createElement('button');
  del.textContent = '✕';
  del.style.cssText = 'background:#ff7676;border:none;border-radius:6px;color:#fff;cursor:pointer;padding:4px 10px;';
  del.onclick = () => li.remove();
  li.appendChild(span); li.appendChild(del);
  document.getElementById('todoList').appendChild(li);
  input.value = '';
}
"""),
dict(slug="quiz-app", title="Simple Quiz Application", desc="A short multiple-choice quiz with automatic scoring.",
     body="""
<div class="demo-area" id="quizArea"></div>
<button class="btn" onclick="submitQuiz()">Submit Quiz</button>
<div class="output-box" id="out"></div>
""",
     js="""
const questions = [
  {q:'Which tag creates a hyperlink?', options:['<link>','<a>','<href>'], answer:1},
  {q:'Which property changes text colour in CSS?', options:['font-color','text-color','color'], answer:2},
  {q:'Which keyword declares a constant in JS?', options:['let','const','var'], answer:1}
];
function renderQuiz(){
  const area = document.getElementById('quizArea');
  area.innerHTML = questions.map((item,i) => `
    <p><strong>Q${i+1}. ${item.q}</strong></p>
    ${item.options.map((opt,j)=>`<label><input type="radio" name="q${i}" value="${j}"> ${opt}</label>`).join('')}
  `).join('<hr style="border-color:var(--border);margin:14px 0;">');
}
function submitQuiz(){
  let score = 0;
  questions.forEach((item,i)=>{
    const chosen = document.querySelector(`input[name="q${i}"]:checked`);
    if(chosen && Number(chosen.value) === item.answer) score++;
  });
  document.getElementById('out').textContent = `You scored ${score} out of ${questions.length}.`;
}
renderQuiz();
"""),
dict(slug="stopwatch", title="Stopwatch", desc="Start, pause, and reset a running stopwatch.",
     body="""
<div class="demo-area" style="text-align:center;">
  <h2 id="swDisplay">00:00.0</h2>
  <button class="btn" onclick="startSW()">Start</button>
  <button class="btn" onclick="pauseSW()">Pause</button>
  <button class="btn" onclick="resetSW()">Reset</button>
</div>
""",
     js="""
let swInterval, swElapsed = 0, swRunning = false;
function render(){
  const mins = Math.floor(swElapsed/60000);
  const secs = Math.floor((swElapsed%60000)/1000);
  const tenths = Math.floor((swElapsed%1000)/100);
  document.getElementById('swDisplay').textContent =
    `${String(mins).padStart(2,'0')}:${String(secs).padStart(2,'0')}.${tenths}`;
}
function startSW(){
  if(swRunning) return;
  swRunning = true;
  const start = Date.now() - swElapsed;
  swInterval = setInterval(()=>{ swElapsed = Date.now()-start; render(); }, 100);
}
function pauseSW(){ swRunning=false; clearInterval(swInterval); }
function resetSW(){ pauseSW(); swElapsed=0; render(); }
"""),
dict(slug="countdown-timer", title="Countdown Timer", desc="Counts down from a user-specified number of seconds.",
     body="""
<div class="demo-area" style="text-align:center;">
  <label>Seconds<input id="ctSeconds" type="number" value="30" style="width:80px;"></label>
  <h2 id="ctDisplay">00:30</h2>
  <button class="btn" onclick="startCT()">Start</button>
  <button class="btn" onclick="stopCT()">Stop</button>
</div>
""",
     js="""
let ctInterval, ctRemaining;
function render(){
  const m = Math.floor(ctRemaining/60), s = ctRemaining%60;
  document.getElementById('ctDisplay').textContent = `${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
}
function startCT(){
  clearInterval(ctInterval);
  ctRemaining = Number(document.getElementById('ctSeconds').value);
  render();
  ctInterval = setInterval(()=>{
    ctRemaining--;
    if(ctRemaining < 0){ clearInterval(ctInterval); document.getElementById('ctDisplay').textContent='Time Up!'; return; }
    render();
  }, 1000);
}
function stopCT(){ clearInterval(ctInterval); }
"""),
dict(slug="localstorage-notes", title="Web Storage: Sticky Notes", desc="Saves and retrieves notes using localStorage so they persist after refresh.",
     body="""
<div class="demo-area">
  <textarea id="noteInput" rows="4" style="width:100%;padding:10px;border-radius:8px;background:#0b0d18;color:var(--text);border:1px solid var(--border);" placeholder="Write a note..."></textarea>
  <button class="btn" onclick="saveNote()">Save to localStorage</button>
  <button class="btn" onclick="clearNote()">Clear Storage</button>
  <div class="output-box" id="out"></div>
</div>
""",
     js="""
function saveNote(){
  const text = document.getElementById('noteInput').value;
  localStorage.setItem('practicalNote', text);
  document.getElementById('out').textContent = 'Saved! Reload this page and it will still be here.';
}
function clearNote(){
  localStorage.removeItem('practicalNote');
  document.getElementById('noteInput').value = '';
  document.getElementById('out').textContent = 'Storage cleared.';
}
window.addEventListener('DOMContentLoaded', () => {
  const saved = localStorage.getItem('practicalNote');
  if(saved){ document.getElementById('noteInput').value = saved; document.getElementById('out').textContent = 'Loaded a previously saved note from localStorage.'; }
});
"""),
dict(slug="browser-objects", title="Browser Objects (window, navigator, location)", desc="Demonstrates common BOM (Browser Object Model) properties.",
     body='<button class="btn" onclick="run()">Show Browser Info</button><div class="output-box" id="out"></div>',
     js="""
function run(){
  document.getElementById('out').textContent =
`Window size: ${window.innerWidth} x ${window.innerHeight}
Browser: ${navigator.userAgent}
Platform: ${navigator.platform}
Current URL: ${location.href}
Cookies enabled: ${navigator.cookieEnabled}`;
}
"""),
dict(slug="regex-email-validation", title="Regular Expressions: Email Validation", desc="Validates an email address format using a regular expression.",
     body='<form class="demo-form" onsubmit="return false;"><label>Email<input id="email" value="student@example.com"></label><button class="btn" onclick="check()">Validate</button></form><div class="output-box" id="out"></div>',
     js="""
function check(){
  const email = document.getElementById('email').value;
  const pattern = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
  document.getElementById('out').textContent = pattern.test(email) ? 'Valid email address.' : 'Invalid email address.';
}
"""),
]

from extra_css import css_extra
from extra_js import js_extra, js_overrides
css_programs += css_extra
js_programs += js_extra
for _p in js_programs:
    _p.update(js_overrides.get(_p['slug'], {}))

def build_category(programs, cat_key, cat_title, cat_desc):
    for p in programs:
        css = p.get("css", "")
        js = p.get("js", "")
        html = page(p["title"], p["desc"], p["body"], css=css, js=js, depth=1,
                    back_href="index.html", back_label=f"Back to {cat_title}")
        write(f"{cat_key}/{p['slug']}.html", html)
    write(f"{cat_key}/index.html", category_index(cat_title, cat_desc, programs, cat_key))

build_category(html_programs, "html", "HTML Programs", "Core HTML structure, forms, media, and semantic markup exercises.")
build_category(css_programs, "css", "CSS Programs", "Styling, layout (Flexbox/Grid), positioning, and visual effects exercises.")
build_category(js_programs, "javascript", "JavaScript Programs", "Programming basics, DOM manipulation, events, forms, storage, and mini-projects.")

# ---------------------------------------------------------------
# MAIN DASHBOARD
# ---------------------------------------------------------------
total = len(html_programs) + len(css_programs) + len(js_programs)
index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HTML, CSS & JavaScript Practical Programs</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site-header">
  <a class="brand" href="index.html">HTML · CSS · JS Programs</a>
  <nav class="crumbs">
    <a href="html/index.html">HTML</a>
    <a href="css/index.html">CSS</a>
    <a href="javascript/index.html">JavaScript</a>
  </nav>
</header>
<main>
  <div class="hero">
    <h1>HTML · CSS · JavaScript</h1>
    <p class="subtitle">Practical Programs Dashboard &mdash; {total} working programs across three sections</p>
  </div>

  <section class="globe-section">
    <div class="globe-wrap">
      <canvas id="globe" aria-label="Rotatable globe: click HTML, CSS or JavaScript to open that section"></canvas>
      <p class="globe-hint">Drag the globe to rotate it, then click a marker to open that section.</p>
      <div class="globe-links">
        <a class="btn" href="html/index.html" data-globe-target="HTML">HTML</a>
        <a class="btn" href="css/index.html" data-globe-target="CSS">CSS</a>
        <a class="btn" href="javascript/index.html" data-globe-target="JavaScript">JavaScript</a>
      </div>
    </div>
  </section>

  <div class="card-grid">
    <div class="card">
      <h2>HTML Programs</h2>
      <p>{len(html_programs)} programs covering structure, forms, media, and semantic markup.</p>
      <a class="btn" href="html/index.html">View HTML Programs</a>
    </div>
    <div class="card">
      <h2>CSS Programs</h2>
      <p>{len(css_programs)} programs covering styling, layout, positioning, and effects.</p>
      <a class="btn" href="css/index.html">View CSS Programs</a>
    </div>
    <div class="card">
      <h2>JavaScript Programs</h2>
      <p>{len(js_programs)} programs covering logic, DOM, events, forms, and storage.</p>
      <a class="btn" href="javascript/index.html">View JavaScript Programs</a>
    </div>
  </div>
</main>
<script src="assets/globe.js"></script>
</body>
</html>
"""
write("index.html", index_html)

readme = f"""# HTML, CSS & JavaScript – Practical Programs

**Student Name:** _____________________
**Register Number:** _____________________
**Class / Section:** _____________________
**Subject:** Web Development / Internet Programming Lab
**Assignment:** HTML, CSS & JavaScript Practical Programs Website

## Total programs completed: {total}

- HTML Programs: {len(html_programs)}
- CSS Programs: {len(css_programs)}
- JavaScript Programs: {len(js_programs)}

## How to run

Open `index.html` in any browser. From the dashboard, use the three cards to
navigate to the HTML, CSS, and JavaScript program listing pages. Every
program page has **Home** and **Back to Programs** links at the bottom.

## Project structure

```
project/
├── index.html              (dashboard)
├── html/                   (HTML program pages + index.html listing)
├── css/                    (CSS program pages + index.html listing)
├── javascript/             (JavaScript program pages + index.html listing)
└── assets/style.css        (shared stylesheet used by every page)
```

## Coverage

Every question in the assignment list is implemented as its own HTML file:
15 HTML questions, 75 CSS questions and 65 JavaScript questions (155 in total).
Each question has its own page (the count is one higher than the question list
because `browser-objects` is an extra Browser Object Model demo).

## Notes

All pages are generated from `generate.py` (with `extra_css.py` and `extra_js.py`),
so any new program only needs one more entry in a list.
"""
write("README.md", readme)

print("Generated", total, "program pages + 4 index pages + README.")
