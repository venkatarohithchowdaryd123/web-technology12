"""Additional CSS programs (imported by generate.py). Every page is scoped inside <div class="w">."""
from urllib.parse import quote

def svg(c1, c2, label="", w=400, h=260):
    s = (f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}'>"
         f"<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='{c1}'/>"
         f"<stop offset='1' stop-color='{c2}'/></linearGradient></defs><rect width='100%' height='100%' fill='url(#g)'/>"
         f"<text x='50%' y='52%' font-family='Arial' font-size='34' fill='white' text-anchor='middle'>{label}</text></svg>")
    return "data:image/svg+xml," + quote(s)

def img(c1, c2, label="", cls="", w=400, h=260):
    return f'<img class="{cls}" src="{svg(c1, c2, label, w, h)}" alt="{label}">'

def bg(c1, c2, label=""):
    return "url(\"" + svg(c1, c2, label) + "\")"

css_extra = []
def add(slug, title, desc, body, css="", js=""):
    css_extra.append(dict(slug=slug, title=title, desc=desc, body=f'<div class="w">{body}</div>', css=css, js=js))

# ---------------- Basics ----------------
add("inline-internal-external-css", "Inline, Internal and External CSS",
    "The three ways to apply CSS: the style attribute, a <style> block, and a linked stylesheet.",
    '''<p style="color:#c0392b;font-weight:bold;">1. Inline CSS: written in the style attribute of this paragraph.</p>
<p class="internal">2. Internal CSS: written in the &lt;style&gt; block in this page's &lt;head&gt;.</p>
<p>3. External CSS: this page is linked to <code>assets/style.css</code>, which styles the button below.</p>
<a class="btn" href="#">Styled by external CSS</a>''',
    ".w .internal{background:#fff3cd;padding:10px;border-left:6px solid #e6a800;border-radius:6px;}")

add("css-selectors", "CSS Selectors",
    "Element, class, ID, attribute, grouping and pseudo-class selectors.",
    '''<p>Plain paragraph (element selector).</p>
<p class="note">Class selector paragraph.</p>
<p id="special">ID selector paragraph.</p>
<h3>Heading grouped</h3><h4>Heading grouped</h4>
<input type="text" placeholder="attribute selector: type=text"><input type="email" placeholder="type=email">
<ul><li>Item 1</li><li>Item 2</li><li>Item 3 (last-child)</li></ul>''',
    """.w p{color:#4a1010;}
.w .note{background:#ffe3e3;padding:6px;}
.w #special{background:#ff6b6b;color:#fff;padding:6px;}
.w h3,.w h4{color:#c0392b;}
.w input[type="text"]{border:2px solid #c0392b;padding:6px;margin:4px;}
.w input[type="email"]{border:2px dashed #c0392b;padding:6px;margin:4px;}
.w li:last-child{font-weight:bold;color:#c0392b;}""")

add("colors-backgrounds-borders", "CSS Colors, Backgrounds and Borders",
    "Named, hex, rgb, hsl and rgba colors with backgrounds and different border styles.",
    '''<div class="row"><div class="s c1">named: tomato</div><div class="s c2">hex: #ff6b6b</div><div class="s c3">rgb(46,204,113)</div>
<div class="s c4">hsl(280,60%,55%)</div><div class="s c5">rgba(0,0,0,.6)</div></div>
<div class="row"><div class="b b1">solid</div><div class="b b2">dashed</div><div class="b b3">dotted</div><div class="b b4">double</div><div class="b b5">mixed sides</div></div>''',
    """.w .row{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:14px;}
.w .s{padding:20px;color:#fff;border-radius:8px;}
.w .c1{background:tomato}.w .c2{background:#ff6b6b}.w .c3{background:rgb(46,204,113)}.w .c4{background:hsl(280,60%,55%)}.w .c5{background:rgba(0,0,0,.6)}
.w .b{padding:16px;background:#fff;color:#4a1010;}
.w .b1{border:3px solid #c0392b}.w .b2{border:3px dashed #c0392b}.w .b3{border:4px dotted #27ae60}.w .b4{border:6px double #8e44ad}
.w .b5{border-top:5px solid red;border-right:5px solid blue;border-bottom:5px solid green;border-left:5px solid orange;}""")

add("font-text-formatting", "Font Properties and Text Formatting",
    "font-family, size, weight, style, letter/word spacing, alignment, decoration and transform.",
    '''<p class="f1">Serif, italic, 22px</p><p class="f2">MONOSPACE with letter-spacing</p>
<p class="f3">Text transform: capitalize each word</p><p class="f4">Underline, overline and line-through</p>
<p class="f5">Centered text with wide word-spacing and generous line-height that makes long lines easier to read.</p>''',
    """.w .f1{font-family:Georgia,serif;font-style:italic;font-size:22px;}
.w .f2{font-family:'Courier New',monospace;letter-spacing:4px;font-weight:bold;}
.w .f3{text-transform:capitalize;font-variant:small-caps;}
.w .f4{text-decoration:underline overline;text-decoration-color:#c0392b;}
.w .f4::after{content:' line-through';text-decoration:line-through;}
.w .f5{text-align:center;word-spacing:8px;line-height:2;text-shadow:1px 1px 2px #999;}""")

add("width-height-sizing", "Width, Height and Sizing",
    "width, height, min/max-width, percentages, viewport units and box-sizing.",
    '''<div class="a">width:200px; height:60px</div><div class="b">width:50%</div>
<div class="c">max-width:300px; width:100% (shrinks on small screens)</div>
<div class="d">min-height:80px (grows with content)<br>extra line<br>extra line</div>
<div class="e content">content-box: 200px + padding + border</div><div class="e border">border-box: exactly 200px</div>''',
    """.w div{background:#ff6b6b;color:#fff;margin:8px 0;padding:8px;}
.w .a{width:200px;height:60px}.w .b{width:50%}.w .c{max-width:300px;width:100%}.w .d{min-height:80px;background:#c0392b}
.w .e{width:200px;border:8px solid #4a1010;padding:16px;background:#ffb3b3;color:#4a1010}
.w .content{box-sizing:content-box}.w .border{box-sizing:border-box}""")

add("css-media-queries", "Responsive Page with CSS Media Queries",
    "Resize the window: colour and layout change at breakpoints.",
    '<div class="bp"><p class="label"></p><div class="cols"><div>One</div><div>Two</div><div>Three</div></div></div>',
    """.w .bp{padding:14px;border-radius:10px;background:#ffe3e3;}
.w .cols{display:grid;grid-template-columns:1fr;gap:10px;}.w .cols div{background:#ff6b6b;color:#fff;padding:20px;text-align:center;border-radius:8px;}
.w .label::before{content:'Mobile: below 600px (1 column)';font-weight:bold;}
@media(min-width:600px){.w .bp{background:#d5f5e3}.w .cols{grid-template-columns:1fr 1fr}.w .label::before{content:'Tablet: 600px+ (2 columns)'}}
@media(min-width:900px){.w .bp{background:#fdebd0}.w .cols{grid-template-columns:repeat(3,1fr)}.w .label::before{content:'Desktop: 900px+ (3 columns)'}}""")

add("responsive-navigation-menu", "Responsive Navigation Menu",
    "Menu collapses into a hamburger toggle on small screens (pure HTML + CSS checkbox).",
    '''<div class="rn"><span class="logo">MyBrand</span><input type="checkbox" id="tg"><label for="tg" class="burger">&#9776;</label>
<ul class="links"><li><a href="#">Home</a></li><li><a href="#">About</a></li><li><a href="#">Services</a></li><li><a href="#">Contact</a></li></ul></div>
<p>Make the window narrower than 700px and use the &#9776; button.</p>''',
    """.w .rn{background:#c0392b;color:#fff;padding:10px 16px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;border-radius:8px;}
.w .rn a{color:#fff;text-decoration:none;padding:8px 12px;display:block;}.w .rn a:hover{background:rgba(255,255,255,.2);border-radius:6px;}
.w .links{list-style:none;margin:0;padding:0;display:flex;}.w #tg,.w .burger{display:none;}
@media(max-width:700px){.w .burger{display:block;cursor:pointer;font-size:26px}.w .links{display:none;flex-direction:column;width:100%}.w #tg:checked~.links{display:flex}}""")

add("css-personal-portfolio", "Personal Portfolio (CSS)",
    "A styled one-page portfolio card layout: profile, skills and projects.",
    f'''<div class="pf"><div class="top">{img("#c0392b","#ff6b6b","Photo","av",120,120)}<div><h2>Your Name</h2><p>Web Developer &amp; Student</p></div></div>
<h3>Skills</h3><div class="tags"><span>HTML</span><span>CSS</span><span>JavaScript</span></div>
<h3>Projects</h3><div class="pj"><div>Calculator</div><div>To-Do List</div><div>Landing Page</div></div></div>''',
    """.w .pf{background:#fff;border-radius:14px;padding:20px;box-shadow:0 6px 20px rgba(0,0,0,.15);color:#4a1010}
.w .top{display:flex;gap:16px;align-items:center}.w .av{width:90px;height:90px;border-radius:50%;object-fit:cover}.w .top h2{margin:0}.w .top p{margin:0}
.w .tags span{background:#ff6b6b;color:#fff;padding:4px 12px;border-radius:20px;margin-right:6px}
.w .pj{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px}.w .pj div{background:#ffe3e3;padding:18px;border-radius:8px;text-align:center}""")

add("student-profile-page", "College / Student Profile Page",
    "Student profile with details table and academic progress bars.",
    f'''<div class="sp"><div class="side">{img("#8e44ad","#3498db","Student","ph",140,140)}<h3>Student Name</h3><p>B.Sc Computer Science</p></div>
<div class="det"><h3>Details</h3><table><tr><th>Register No.</th><td>2026CS001</td></tr><tr><th>Class</th><td>II Year - A</td></tr><tr><th>Email</th><td>student@college.edu</td></tr></table>
<h3>Progress</h3><label>HTML</label><div class="bar"><i style="width:90%"></i></div><label>CSS</label><div class="bar"><i style="width:75%"></i></div><label>JavaScript</label><div class="bar"><i style="width:60%"></i></div></div></div>''',
    """.w .sp{display:grid;grid-template-columns:200px 1fr;gap:18px}.w .side{text-align:center;background:#ffe3e3;border-radius:12px;padding:16px}.w .ph{border-radius:50%;width:110px;height:110px}
.w table{border-collapse:collapse;width:100%}.w th,.w td{border:1px solid #ffb3b3;padding:6px 10px;text-align:left}.w th{background:#ffe3e3}
.w .bar{background:#fdd5d5;border-radius:8px;height:14px;overflow:hidden}.w .bar i{display:block;height:100%;background:#c0392b}
@media(max-width:600px){.w .sp{grid-template-columns:1fr}}""")

add("website-homepage", "Complete Website Homepage",
    "Hero, features, and footer built only with HTML and CSS.",
    '''<div class="hp"><div class="nv"><b>SiteName</b><span>Home &middot; About &middot; Contact</span></div>
<div class="he"><h2>Build Beautiful Websites</h2><p>Learn HTML, CSS and JavaScript step by step.</p><a href="#" class="cta">Get Started</a></div>
<div class="ft"><div><h3>Fast</h3><p>Lightweight pages.</p></div><div><h3>Responsive</h3><p>Fits any screen.</p></div><div><h3>Modern</h3><p>Flexbox &amp; Grid.</p></div></div>
<div class="fo">&copy; 2026 SiteName</div></div>''',
    """.w .hp{border-radius:12px;overflow:hidden;background:#fff;color:#4a1010}.w .nv{display:flex;justify-content:space-between;padding:12px 18px;background:#4a1010;color:#fff}
.w .he{padding:50px 20px;text-align:center;background:linear-gradient(135deg,#c0392b,#ff6b6b);color:#fff}.w .cta{display:inline-block;background:#fff;color:#c0392b;padding:10px 22px;border-radius:30px;text-decoration:none;font-weight:bold}
.w .ft{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:14px;padding:20px;text-align:center}.w .fo{background:#4a1010;color:#fff;text-align:center;padding:10px}""")

# ---------------- Selectors ----------------
add("inheritance-specificity", "CSS Inheritance and Specificity",
    "Child elements inherit some properties; higher-specificity selectors win.",
    '''<div class="parent">Parent text (color and font are inherited)<p>Child paragraph inherits colour and font.</p>
<p class="c">Class rule beats element rule.</p><p class="c" id="i">ID rule beats class rule.</p><p class="c" style="color:green">Inline style beats ID (!important beats all).</p></div>''',
    """.w .parent{color:#8e44ad;font-family:Georgia,serif;font-size:18px;border:2px solid #8e44ad;padding:10px}
.w p{color:#4a1010}.w .c{color:#e67e22}.w #i{color:#c0392b}""")

add("universal-element-class-id-attribute-grouping", "Universal, Element, Class, ID, Attribute and Grouping Selectors",
    "Each selector type applied to a small sample page.",
    '''<div class="u"><h3>Element selector (h3)</h3><p class="hi">Class selector .hi</p><p id="only">ID selector #only</p>
<a href="https://example.com">Attribute: href starts with https</a> <a href="#local">Local link</a><h4>Grouped h4</h4><h5>Grouped h5</h5></div>''',
    """.w .u *{border:1px dotted #ffb3b3;padding:4px;margin:4px}
.w h3{color:#c0392b}.w .hi{background:#fff3cd}.w #only{background:#d5f5e3;font-weight:bold}
.w a[href^="https"]{color:#c0392b;font-weight:bold}.w h4,.w h5{color:#8e44ad;text-decoration:underline}""")

add("combinator-selectors", "Combinator Selectors",
    "Descendant, child (>), adjacent sibling (+) and general sibling (~) selectors.",
    '''<div class="box"><p>Direct child p (child &gt;)</p><section><p>Nested p (descendant only)</p></section><h4>Heading</h4>
<p>p right after h4 (adjacent +)</p><p>Later sibling p (general ~)</p></div>''',
    """.w .box p{border-left:4px solid #ff6b6b;padding-left:8px}
.w .box>p{background:#ffe3e3}
.w h4+p{background:#fff3cd;font-weight:bold}
.w h4~p{color:#c0392b}""")

# ---------------- Visual properties ----------------
add("background-images-position", "Background Images and Positioning",
    "background-image, size, repeat, position and attachment.",
    f'''<div class="g g1">no-repeat, top-left</div><div class="g g2">repeat pattern</div><div class="g g3">cover, centered</div>''',
    f""".w .g{{height:120px;margin:10px 0;color:#fff;font-weight:bold;border:2px solid #4a1010}}
.w .g1{{background:{bg("#e67e22","#f1c40f","IMG")} no-repeat top left;background-size:100px}}
.w .g2{{background:{bg("#16a085","#2ecc71","")} repeat;background-size:40px}}
.w .g3{{background:{bg("#8e44ad","#3498db","Cover")} center/cover no-repeat}}""")

add("opacity-transparency", "Opacity and Transparency",
    "opacity affects the whole element, rgba only the colour.",
    '''<div class="r"><div class="o o1">opacity:1</div><div class="o o2">opacity:.6</div><div class="o o3">opacity:.3</div><div class="o o4">rgba bg only<br><b>text stays solid</b></div></div>''',
    """.w .r{display:flex;gap:10px;flex-wrap:wrap;background:repeating-linear-gradient(45deg,#ccc,#ccc 10px,#fff 10px,#fff 20px);padding:14px}
.w .o{padding:24px;color:#fff;background:#c0392b;border-radius:8px}.w .o2{opacity:.6}.w .o3{opacity:.3}.w .o4{background:rgba(192,57,43,.4);color:#000}
.w .o:hover{opacity:1}""")

add("overflow-properties", "Overflow Properties",
    "visible, hidden, scroll and auto.",
    '''<div class="r"><div class="ov v">visible: text spills out of the box and is still shown outside its border.</div><div class="ov h">hidden: extra text is clipped and cannot be seen at all.</div>
<div class="ov s">scroll: always shows scrollbars so you can read more text inside.</div><div class="ov a">auto: scrollbar appears only when needed to read the extra text.</div></div>''',
    """.w .r{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:22px}
.w .ov{height:70px;border:2px solid #c0392b;padding:6px;background:#ffe3e3;font-size:.9rem}
.w .v{overflow:visible}.w .h{overflow:hidden}.w .s{overflow:scroll}.w .a{overflow:auto}""")

add("z-index-stacking", "z-index and Stacking Order",
    "Higher z-index values stack above lower ones. Hover a box to raise it.",
    '<div class="st"><div class="z z1">z-index: 1</div><div class="z z2">z-index: 3</div><div class="z z3">z-index: 2</div></div>',
    """.w .st{position:relative;height:200px}.w .z{position:absolute;width:140px;height:110px;color:#fff;padding:10px;border-radius:8px;box-shadow:0 4px 10px rgba(0,0,0,.3)}
.w .z1{background:#e74c3c;top:10px;left:10px;z-index:1}.w .z2{background:#3498db;top:40px;left:70px;z-index:3}.w .z3{background:#2ecc71;top:70px;left:130px;z-index:2}
.w .z:hover{z-index:10}""")

add("display-properties", "CSS Display Properties",
    "block, inline, inline-block and none.",
    '''<span class="d1">inline A</span><span class="d1">inline B (width ignored)</span>
<div class="d2">block (full width)</div><span class="d3">inline-block 1</span><span class="d3">inline-block 2</span>
<div class="d4">display:none (you cannot see me)</div><p>A hidden div sits above this line.</p>''',
    """.w .d1{display:inline;background:#ffe3e3;width:300px;height:80px}
.w .d2{display:block;background:#ff6b6b;color:#fff;padding:8px;margin:8px 0}
.w .d3{display:inline-block;width:150px;height:50px;background:#c0392b;color:#fff;margin:4px;text-align:center;line-height:50px}
.w .d4{display:none}""")

add("visibility-hiding-elements", "Visibility and Hiding Elements",
    "visibility:hidden keeps the space; display:none removes it; opacity:0 is invisible but clickable.",
    '''<div class="v v1">Visible</div><div class="v v2">visibility:hidden (space kept)</div><div class="v v3">display:none (no space)</div><div class="v v4">opacity:0 (still takes space)</div><div class="v v5">Last box</div>''',
    """.w .v{padding:12px;background:#ff6b6b;color:#fff;margin:6px 0}.w .v2{visibility:hidden}.w .v3{display:none}.w .v4{opacity:0}""")

add("image-hover-effect", "Image Hover Effect",
    "Zoom and caption overlay when hovering images.",
    f'''<div class="row"><figure class="fg">{img("#e67e22","#f39c12","Sunset")}<figcaption>Sunset</figcaption></figure><figure class="fg">{img("#16a085","#1abc9c","Forest")}<figcaption>Forest</figcaption></figure></div>''',
    """.w .row{display:flex;gap:14px;flex-wrap:wrap}.w .fg{position:relative;overflow:hidden;margin:0;width:260px;border-radius:10px}
.w .fg img{width:100%;display:block;transition:transform .5s}.w .fg:hover img{transform:scale(1.2) rotate(2deg)}
.w figcaption{position:absolute;inset:auto 0 0 0;background:rgba(0,0,0,.6);color:#fff;padding:10px;transform:translateY(100%);transition:transform .4s}
.w .fg:hover figcaption{transform:translateY(0)}""")

add("css-tooltip", "CSS Tooltip",
    "Tooltip shown on hover using data-tip and ::after.",
    '<p>Hover over the <span class="tip" data-tip="I am a tooltip!">highlighted word</span> or the <button class="tip btn" data-tip="Button tooltip">button</button>.</p>',
    """.w .tip{position:relative;border-bottom:2px dotted #c0392b;cursor:help}
.w .tip::after{content:attr(data-tip);position:absolute;bottom:130%;left:50%;transform:translateX(-50%);background:#4a1010;color:#fff;padding:6px 10px;border-radius:6px;white-space:nowrap;font-size:.8rem;opacity:0;pointer-events:none;transition:.25s}
.w .tip::before{content:'';position:absolute;bottom:110%;left:50%;transform:translateX(-50%);border:6px solid transparent;border-top-color:#4a1010;opacity:0;transition:.25s}
.w .tip:hover::after,.w .tip:hover::before{opacity:1}""")

add("button-hover-animation", "CSS-only Button Hover Animation",
    "Sliding fill, grow and glow effects on hover.",
    '<button class="b b1">Slide fill</button> <button class="b b2">Grow</button> <button class="b b3">Glow</button>',
    """.w .b{padding:12px 26px;border:2px solid #c0392b;background:transparent;color:#c0392b;font-size:1rem;border-radius:8px;cursor:pointer;transition:.3s;position:relative;overflow:hidden;z-index:0}
.w .b1::before{content:'';position:absolute;inset:0;background:#c0392b;transform:translateX(-101%);transition:transform .35s;z-index:-1}
.w .b1:hover::before{transform:translateX(0)}.w .b1:hover{color:#fff}
.w .b2:hover{transform:scale(1.15);background:#ff6b6b;color:#fff}
.w .b3:hover{box-shadow:0 0 18px 4px #ff6b6b;background:#ffe3e3}""")

add("css-filters", "CSS Filters",
    "blur, grayscale, brightness, contrast, sepia and hue-rotate.",
    f'''<div class="row">{"".join(f'<figure><div class="p {c}">{img("#e67e22","#8e44ad","Photo",w=160,h=110)}</div><figcaption>{t}</figcaption></figure>' for c,t in [("f0","original"),("f1","blur(3px)"),("f2","grayscale(1)"),("f3","brightness(1.6)"),("f4","contrast(2)"),("f5","sepia(1)"),("f6","hue-rotate(120deg)")])}</div>''',
    """.w .row{display:flex;flex-wrap:wrap;gap:10px}.w figure{margin:0;text-align:center}.w img{width:150px;border-radius:8px}
.w .f1 img{filter:blur(3px)}.w .f2 img{filter:grayscale(1)}.w .f3 img{filter:brightness(1.6)}.w .f4 img{filter:contrast(2)}.w .f5 img{filter:sepia(1)}.w .f6 img{filter:hue-rotate(120deg)}""")

add("object-fit-position", "object-fit and object-position",
    "How an image fills a fixed-size box: fill, contain, cover, and object-position.",
    f'''<div class="row">{"".join(f'<figure><img class="{c}" src="{svg("#2980b9","#e74c3c","Wide image",600,200)}"><figcaption>{t}</figcaption></figure>' for c,t in [("a","fill (stretched)"),("b","contain"),("c","cover"),("d","cover + position left")])}</div>''',
    """.w .row{display:flex;flex-wrap:wrap;gap:12px}.w figure{margin:0;text-align:center}.w img{width:150px;height:150px;border:2px solid #4a1010;background:#eee}
.w .a{object-fit:fill}.w .b{object-fit:contain}.w .c{object-fit:cover}.w .d{object-fit:cover;object-position:left center}""")

# ---------------- Layouts ----------------
add("responsive-image-gallery", "Responsive Image Gallery (Flexbox)",
    "Images wrap and resize automatically; hover to enlarge.",
    '<div class="gl">' + "".join(img(a, b, f"Pic {i}", w=300, h=200) for i, (a, b) in enumerate([("#e74c3c","#f39c12"),("#1abc9c","#3498db"),("#9b59b6","#e84393"),("#2c3e50","#3498db"),("#27ae60","#f1c40f"),("#d35400","#c0392b")], 1)) + '</div>',
    """.w .gl{display:flex;flex-wrap:wrap;gap:10px}.w .gl img{flex:1 1 200px;max-width:100%;height:150px;object-fit:cover;border-radius:8px;transition:transform .3s}.w .gl img:hover{transform:scale(1.05)}""")

add("flexbox-card-layout", "Card-based Layout using Flexbox",
    "Cards that wrap and share the row equally.",
    '<div class="cs">' + "".join(f'<div class="cd"><h3>Card {i}</h3><p>Short description of card {i}.</p><a href="#" class="btn">Read</a></div>' for i in range(1, 5)) + '</div>',
    """.w .cs{display:flex;flex-wrap:wrap;gap:14px}.w .cd{flex:1 1 200px;background:#fff;color:#4a1010;padding:16px;border-radius:12px;box-shadow:0 4px 12px rgba(0,0,0,.15)}.w .cd h3{margin-top:0}""")

add("grid-dashboard-layout", "Dashboard Layout using CSS Grid",
    "Sidebar, header, stat tiles and content in a grid.",
    '''<div class="db"><div class="hd">Dashboard</div><div class="sd">Menu<br>Home<br>Reports<br>Users</div>
<div class="t">Users<b>1,240</b></div><div class="t">Sales<b>&#8377;54k</b></div><div class="t">Orders<b>320</b></div><div class="ct">Main content / chart area</div></div>''',
    """.w .db{display:grid;grid-template-columns:130px repeat(3,1fr);grid-template-rows:50px auto 160px;gap:10px}
.w .db>div{padding:12px;border-radius:8px;color:#fff}.w .hd{grid-column:1/-1;background:#4a1010;line-height:26px}.w .sd{grid-row:2/4;background:#c0392b}
.w .t{background:#ff6b6b}.w .t b{display:block;font-size:1.6rem}.w .ct{grid-column:2/-1;background:#ffb3b3;color:#4a1010}
@media(max-width:600px){.w .db{grid-template-columns:1fr 1fr}.w .sd{grid-row:auto;grid-column:1/-1}.w .ct{grid-column:1/-1}}""")

add("two-column-grid-layout", "Two-Column Layout using CSS Grid",
    "Main content plus sidebar that stacks on small screens.",
    '<div class="tc"><article><h3>Main Article</h3><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore.</p></article><aside><h3>Sidebar</h3><p>Links, ads or related posts.</p></aside></div>',
    """.w .tc{display:grid;grid-template-columns:2fr 1fr;gap:16px}.w article{background:#ffe3e3;padding:14px;border-radius:8px}.w aside{background:#fff3cd;padding:14px;border-radius:8px}
@media(max-width:600px){.w .tc{grid-template-columns:1fr}}""")

add("three-column-flexbox-layout", "Three-Column Layout using Flexbox",
    "Left sidebar, centre content and right sidebar.",
    '<div class="th"><div class="l">Left (20%)</div><div class="m">Centre content grows to fill remaining space.</div><div class="r">Right (20%)</div></div>',
    """.w .th{display:flex;gap:10px}.w .th>div{padding:20px;border-radius:8px;color:#fff}.w .l,.w .r{flex:0 0 20%;background:#c0392b}.w .m{flex:1;background:#ff6b6b}
@media(max-width:600px){.w .th{flex-direction:column}.w .l,.w .r{flex-basis:auto}}""")

add("fixed-sidebar", "Webpage with a Fixed Sidebar",
    "A sidebar that stays fixed while the page scrolls (wide screens).",
    '<div class="fx"><ul class="sb"><li><a href="#s1">Section 1</a></li><li><a href="#s2">Section 2</a></li><li><a href="#s3">Section 3</a></li></ul><div class="ctn"><h3 id="s1">Section 1</h3><p>Scroll the page &ndash; the sidebar stays in place.</p><div class="sp"></div><h3 id="s2">Section 2</h3><div class="sp"></div><h3 id="s3">Section 3</h3><div class="sp"></div></div></div>',
    """.w .sb{list-style:none;margin:0;padding:10px;background:#4a1010;border-radius:8px}.w .sb a{color:#fff;text-decoration:none;display:block;padding:8px}
.w .sp{height:300px;background:repeating-linear-gradient(#fff0f0,#fff0f0 20px,#ffe3e3 20px,#ffe3e3 40px)}
@media(min-width:900px){.w .sb{position:fixed;top:110px;left:12px;width:150px;z-index:20}.w .ctn{margin-left:0}}""")

add("responsive-footer", "Responsive Footer",
    "Footer columns rearrange from four to two to one column.",
    '<div class="ff"><div><h4>About</h4><p>Short text about us.</p></div><div><h4>Links</h4><p>Home<br>Courses<br>Contact</p></div><div><h4>Follow</h4><p>Twitter<br>GitHub</p></div><div><h4>Contact</h4><p>info@site.com</p></div></div><div class="cp">&copy; 2026 Practical Programs</div>',
    """.w .ff{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;background:#4a1010;color:#fff;padding:20px;border-radius:10px 10px 0 0}.w .ff h4{margin:0 0 6px;color:#ffb3b3}
.w .cp{background:#330a0a;color:#ffc9c9;text-align:center;padding:8px;border-radius:0 0 10px 10px}
@media(max-width:800px){.w .ff{grid-template-columns:1fr 1fr}}@media(max-width:480px){.w .ff{grid-template-columns:1fr}}""")

add("responsive-login-signup", "Responsive Login and Signup Page",
    "Two forms side by side that stack on small screens.",
    '''<div class="ls"><form onsubmit="return false"><h3>Login</h3><input placeholder="Email"><input type="password" placeholder="Password"><button>Login</button></form>
<form onsubmit="return false"><h3>Sign Up</h3><input placeholder="Name"><input placeholder="Email"><input type="password" placeholder="Password"><button>Create account</button></form></div>''',
    """.w .ls{display:grid;grid-template-columns:1fr 1fr;gap:16px}.w form{background:#fff;padding:18px;border-radius:12px;box-shadow:0 4px 12px rgba(0,0,0,.15)}
.w form h3{margin-top:0;color:#c0392b}.w input{display:block;width:100%;padding:10px;margin:8px 0;border:1px solid #ffb3b3;border-radius:6px}
.w button{width:100%;padding:10px;background:#c0392b;color:#fff;border:0;border-radius:6px;cursor:pointer}.w button:hover{background:#ff6b6b}
@media(max-width:600px){.w .ls{grid-template-columns:1fr}}""")

add("responsive-contact-form", "Responsive Contact Form",
    "Two-column fields that become one column on mobile.",
    '''<form class="cf" onsubmit="return false"><div class="g"><label>First name<input></label><label>Last name<input></label><label>Email<input type="email"></label><label>Phone<input type="tel"></label>
<label class="full">Message<textarea rows="4"></textarea></label></div><button>Send message</button></form>''',
    """.w .cf{background:#fff;padding:18px;border-radius:12px;color:#4a1010}.w .g{display:grid;grid-template-columns:1fr 1fr;gap:12px}.w .full{grid-column:1/-1}
.w label{font-size:.9rem;font-weight:600}.w input,.w textarea{width:100%;padding:10px;border:1px solid #ffb3b3;border-radius:6px;margin-top:4px;font:inherit}
.w button{margin-top:14px;padding:10px 26px;background:#c0392b;color:#fff;border:0;border-radius:6px}@media(max-width:560px){.w .g{grid-template-columns:1fr}}""")

add("responsive-college-homepage", "Responsive College Website Homepage",
    "Banner, departments, notices and footer that adapt to screen size.",
    '''<div class="cl"><div class="bn"><h2>ABC College of Arts &amp; Science</h2><p>Excellence in Education</p></div>
<div class="dp"><div>Computer Science</div><div>Commerce</div><div>Mathematics</div><div>English</div></div>
<div class="nt"><h3>Notices</h3><ul><li>Semester exams start next month</li><li>Lab records due Friday</li><li>Sports day registrations open</li></ul></div></div>''',
    """.w .cl{background:#fff;border-radius:12px;overflow:hidden;color:#4a1010}.w .bn{background:linear-gradient(135deg,#8e44ad,#3498db);color:#fff;padding:40px 20px;text-align:center}
.w .dp{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:16px}.w .dp div{background:#ffe3e3;padding:20px 8px;text-align:center;border-radius:8px;font-weight:bold}
.w .nt{padding:0 16px 16px}@media(max-width:700px){.w .dp{grid-template-columns:1fr 1fr}}""")

add("restaurant-webpage", "Restaurant Webpage",
    "Menu cards, opening hours and reservation button.",
    f'''<div class="rs"><div class="rh"><h2>&#127869; Spice Garden</h2><p>Authentic flavours since 1998</p></div><div class="mn">
{"".join(f'<div class="it">{img(a,b,n,w=200,h=120)}<h4>{n}</h4><p>&#8377;{p}</p></div>' for n,p,a,b in [("Biryani",220,"#d35400","#f39c12"),("Paneer Tikka",180,"#c0392b","#e67e22"),("Masala Dosa",120,"#b7950b","#f1c40f"),("Gulab Jamun",80,"#7b241c","#e74c3c")])}</div>
<div class="hr">Open daily 11 AM &ndash; 11 PM <a class="btn" href="#">Reserve a table</a></div></div>''',
    """.w .rs{background:#fffaf0;border-radius:12px;overflow:hidden;color:#4a2c0a}.w .rh{background:#7b241c;color:#fff;text-align:center;padding:26px}.w .rh h2{margin:0}
.w .mn{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;padding:16px}.w .it{background:#fff;border-radius:10px;overflow:hidden;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,.15)}
.w .it img{width:100%;display:block}.w .it h4{margin:8px 0 0}.w .it p{margin:2px 0 10px;color:#c0392b;font-weight:bold}.w .hr{text-align:center;padding:14px;background:#f5e6cc}""")

add("online-shopping-webpage", "Online Shopping Webpage",
    "Product grid with price, rating and Add to Cart buttons.",
    '<div class="sh">' + "".join(f'<div class="pd"><span class="bd">{t}</span>{img(a,b,n,w=200,h=140)}<h4>{n}</h4><p class="st">&#9733;&#9733;&#9733;&#9733;&#9734;</p><p class="pr">&#8377;{p}</p><button>Add to Cart</button></div>' for n,p,t,a,b in [("Headphones",1499,"-20%","#34495e","#3498db"),("Smart Watch",2999,"New","#16a085","#1abc9c"),("Backpack",999,"-10%","#8e44ad","#9b59b6"),("Sneakers",2499,"Hot","#c0392b","#e74c3c")]) + '</div>',
    """.w .sh{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:14px}.w .pd{position:relative;background:#fff;padding:10px;border-radius:12px;text-align:center;box-shadow:0 3px 10px rgba(0,0,0,.15);color:#4a1010}
.w .pd img{width:100%;border-radius:8px}.w .pd h4{margin:8px 0 0}.w .st{color:#f39c12;margin:2px 0}.w .pr{font-weight:bold;margin:2px 0 8px}
.w .bd{position:absolute;top:16px;left:16px;background:#e74c3c;color:#fff;padding:2px 8px;border-radius:12px;font-size:.75rem;z-index:1}
.w .pd button{background:#c0392b;color:#fff;border:0;padding:8px 14px;border-radius:6px;cursor:pointer}.w .pd button:hover{background:#ff6b6b}""")

add("travel-website-homepage", "Travel Website Homepage",
    "Hero search bar with destination cards.",
    f'''<div class="tv"><div class="hr"><h2>Explore the World</h2><div class="sr"><input placeholder="Where to?"><button>Search</button></div></div><div class="ds">
{"".join(f'<div class="d">{img(a,b,n,w=240,h=150)}<div class="lb">{n}</div></div>' for n,a,b in [("Goa","#0097a7","#f9a825"),("Ooty","#2e7d32","#a5d6a7"),("Jaipur","#c62828","#ff8a65"),("Kerala","#00695c","#26a69a")])}</div></div>''',
    """.w .tv{background:#fff;border-radius:12px;overflow:hidden}.w .hr{padding:44px 16px;text-align:center;color:#fff;background:linear-gradient(135deg,#0097a7,#6a1b9a)}
.w .sr{display:flex;max-width:400px;margin:12px auto 0}.w .sr input{flex:1;padding:10px;border:0;border-radius:24px 0 0 24px}.w .sr button{padding:10px 20px;border:0;background:#f9a825;border-radius:0 24px 24px 0;cursor:pointer}
.w .ds{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;padding:14px}.w .d{position:relative;overflow:hidden;border-radius:10px}.w .d img{width:100%;display:block;transition:.4s}.w .d:hover img{transform:scale(1.12)}
.w .lb{position:absolute;bottom:0;left:0;right:0;background:rgba(0,0,0,.55);color:#fff;padding:8px;text-align:center}""")

add("news-blog-grid-layout", "News / Blog Webpage Layout using CSS Grid",
    "A featured story spanning two columns with smaller article cards.",
    '<div class="nb">' + f'<article class="ft">{img("#2c3e50","#e74c3c","Top Story",w=500,h=220)}<h3>Featured: Big headline goes here</h3></article>' + "".join(f'<article>{img(a,b,f"News {i}",w=240,h=130)}<h4>Article headline {i}</h4><p>Short summary of the story.</p></article>' for i, (a, b) in enumerate([("#16a085","#2980b9"),("#8e44ad","#c0392b"),("#f39c12","#d35400"),("#27ae60","#2c3e50")], 1)) + '</div>',
    """.w .nb{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.w article{background:#fff;padding:10px;border-radius:10px;box-shadow:0 2px 8px rgba(0,0,0,.15);color:#4a1010}
.w article img{width:100%;border-radius:6px}.w article h3,.w article h4{margin:8px 0 4px}.w article p{margin:0;font-size:.9rem}.w .ft{grid-column:1/-1}
@media(max-width:700px){.w .nb{grid-template-columns:1fr}}""")

add("portfolio-multiple-sections", "Portfolio Website with Multiple Sections",
    "About, Skills, Projects and Contact sections with anchor navigation.",
    '''<div class="pm"><div class="nv"><a href="#ab">About</a><a href="#sk">Skills</a><a href="#pj">Projects</a><a href="#ct">Contact</a></div>
<section id="ab"><h3>About</h3><p>I am a student learning web development.</p></section><section id="sk"><h3>Skills</h3><p>HTML &bull; CSS &bull; JavaScript</p></section>
<section id="pj"><h3>Projects</h3><p>Calculator, To-Do List, Quiz App.</p></section><section id="ct"><h3>Contact</h3><p>me@example.com</p></section></div>''',
    """.w .pm{background:#fff;border-radius:12px;overflow:hidden;color:#4a1010}.w .nv{display:flex;background:#4a1010;position:sticky;top:0}.w .nv a{color:#fff;padding:12px 16px;text-decoration:none}.w .nv a:hover{background:#c0392b}
.w section{padding:30px 20px;border-bottom:1px solid #ffe3e3}.w section:nth-of-type(even){background:#fff0f0}.w section h3{margin-top:0}
html{scroll-behavior:smooth}""")

add("grid-template-areas", "CSS Grid Template Areas",
    "Named areas make the layout readable; it is rearranged in a media query.",
    '<div class="ga"><div class="h">header</div><div class="n">nav</div><div class="m">main</div><div class="a">aside</div><div class="f">footer</div></div>',
    """.w .ga{display:grid;gap:8px;grid-template-areas:"h h h" "n m a" "f f f";grid-template-columns:100px 1fr 100px}.w .ga>div{padding:16px;color:#fff;border-radius:6px;text-align:center}
.w .h{grid-area:h;background:#4a1010}.w .n{grid-area:n;background:#c0392b}.w .m{grid-area:m;background:#ff6b6b;min-height:100px}.w .a{grid-area:a;background:#8e44ad}.w .f{grid-area:f;background:#2c3e50}
@media(max-width:560px){.w .ga{grid-template-areas:"h" "n" "m" "a" "f";grid-template-columns:1fr}}""")

add("flexbox-alignment-ordering", "Flexbox Alignment and Ordering",
    "justify-content, align-items, order and flex-direction.",
    '''<h4>justify-content: space-between; align-items: center</h4><div class="fb a"><div>1</div><div class="tall">2</div><div>3</div></div>
<h4>flex-direction: row-reverse; justify-content:flex-end</h4><div class="fb b"><div>1</div><div>2</div><div>3</div></div>
<h4>order property: 3, 1, 2 becomes 1, 2, 3 visually</h4><div class="fb c"><div style="order:3">A (order 3)</div><div style="order:1">B (order 1)</div><div style="order:2">C (order 2)</div></div>''',
    """.w .fb{display:flex;background:#ffe3e3;padding:8px;gap:8px;border-radius:8px}.w .fb>div{background:#c0392b;color:#fff;padding:14px 20px;border-radius:6px}
.w .a{justify-content:space-between;align-items:center;height:120px}.w .tall{padding:34px 20px}.w .b{flex-direction:row-reverse;justify-content:flex-end}.w .c{justify-content:center}""")

add("grid-media-queries-layout", "Responsive Layout using CSS Grid and Media Queries",
    "auto grid changes from 1 to 2 to 4 columns with screen width.",
    '<div class="gm">' + "".join(f'<div>Box {i}</div>' for i in range(1, 9)) + '</div>',
    """.w .gm{display:grid;grid-template-columns:1fr;gap:10px}.w .gm div{background:#ff6b6b;color:#fff;padding:24px;text-align:center;border-radius:8px}
@media(min-width:500px){.w .gm{grid-template-columns:repeat(2,1fr)}}@media(min-width:900px){.w .gm{grid-template-columns:repeat(4,1fr)}}""")

add("mobile-first-responsive-page", "Mobile-First Responsive Webpage",
    "Base styles are for mobile; min-width media queries add features for bigger screens.",
    '<div class="mf"><div class="nv">Menu (stacked on mobile)</div><div class="cn"><div>Content</div><div>Sidebar (appears at 700px+)</div></div><div class="ft">Footer</div></div>',
    """.w .mf>div{padding:16px;margin-bottom:8px;border-radius:8px;color:#fff}.w .nv{background:#4a1010}.w .cn{background:none;color:inherit;padding:0;display:block}
.w .cn>div{background:#ff6b6b;color:#fff;padding:20px;border-radius:8px;margin-bottom:8px}.w .cn>div+div{background:#8e44ad}.w .ft{background:#2c3e50}
@media(min-width:700px){.w .cn{display:flex;gap:8px}.w .cn>div{flex:1;margin:0}.w .cn>div:first-child{flex:2}.w .nv::after{content:' \\2192 now horizontal-style desktop layout'}}""")

# ---------------- Motion ----------------
add("css-transitions", "CSS Transitions",
    "Smooth change of properties with duration, timing-function and delay.",
    '<div class="tr t1">Width</div><div class="tr t2">Colour + radius</div><div class="tr t3">Delay 0.5s, ease-in-out</div><p>Hover the boxes.</p>',
    """.w .tr{width:150px;padding:14px;margin:8px 0;background:#ff6b6b;color:#fff}
.w .t1{transition:width 1s}.w .t1:hover{width:100%}.w .t2{transition:background 1s,border-radius 1s}.w .t2:hover{background:#8e44ad;border-radius:30px}
.w .t3{transition:transform .8s ease-in-out .5s}.w .t3:hover{transform:translateX(200px)}""")

add("transforms-2d-3d", "2D and 3D CSS Transformations",
    "translate, rotate, scale, skew, plus rotateX/rotateY with perspective.",
    '<div class="r"><div class="x a">rotate</div><div class="x b">scale</div><div class="x c">skew</div><div class="x d">translate</div></div><div class="r p"><div class="x e">rotateY</div><div class="x f">rotateX</div><div class="cube"><span>3D</span></div></div>',
    """.w .r{display:flex;gap:26px;flex-wrap:wrap;padding:20px}.w .p{perspective:500px}.w .x{width:90px;height:90px;background:#c0392b;color:#fff;display:flex;align-items:center;justify-content:center;transition:transform .6s}
.w .a:hover{transform:rotate(45deg)}.w .b:hover{transform:scale(1.4)}.w .c:hover{transform:skew(20deg,10deg)}.w .d:hover{transform:translate(20px,-10px)}
.w .e:hover{transform:rotateY(180deg)}.w .f:hover{transform:rotateX(180deg)}.w .cube{width:90px;height:90px;background:#e67e22;color:#fff;display:flex;align-items:center;justify-content:center;transform:rotateX(35deg) rotateY(35deg);transition:.6s}
.w .cube:hover{transform:rotateX(0) rotateY(0)}""")

add("keyframe-animations", "Keyframe Animations (Multi-step)",
    "Percentage keyframes: a ball moves, changes colour and squashes; text pulses.",
    '<div class="trk"><div class="ball"></div></div><h3 class="pulse">Pulsing text</h3>',
    """.w .trk{height:80px;background:#ffe3e3;border-radius:40px;position:relative}.w .ball{width:60px;height:60px;border-radius:50%;position:absolute;top:10px;animation:go 4s infinite alternate ease-in-out}
@keyframes go{0%{left:10px;background:#e74c3c}25%{background:#f1c40f}50%{background:#2ecc71;transform:scale(1.3)}75%{background:#3498db}100%{left:calc(100% - 70px);background:#9b59b6}}
.w .pulse{color:#c0392b;animation:pl 1.5s infinite}@keyframes pl{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(1.15)}}""")

add("loading-spinner", "Loading Spinner Animation",
    "Ring spinner, dots loader and progress bar using only CSS.",
    '<div class="row"><div class="sp"></div><div class="dots"><i></i><i></i><i></i></div><div class="pb"><i></i></div></div>',
    """.w .row{display:flex;gap:40px;align-items:center;flex-wrap:wrap;padding:20px}.w .sp{width:56px;height:56px;border:6px solid #ffe3e3;border-top-color:#c0392b;border-radius:50%;animation:spin 1s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}.w .dots{display:flex;gap:8px}.w .dots i{width:16px;height:16px;background:#c0392b;border-radius:50%;animation:bn .8s infinite alternate}
.w .dots i:nth-child(2){animation-delay:.2s}.w .dots i:nth-child(3){animation-delay:.4s}@keyframes bn{to{transform:translateY(-16px);opacity:.3}}
.w .pb{width:200px;height:12px;background:#ffe3e3;border-radius:6px;overflow:hidden}.w .pb i{display:block;height:100%;width:40%;background:#c0392b;animation:ld 1.4s infinite}@keyframes ld{from{margin-left:-40%}to{margin-left:100%}}""")

add("sliding-image-card-animation", "Sliding Image / Card Animation",
    "Cards slide in from the sides on load and an image strip scrolls continuously.",
    f'''<div class="cs"><div class="c c1">Slide from left</div><div class="c c2">Slide from right</div><div class="c c3">Slide from bottom</div></div>
<div class="vw"><div class="strip">{"".join(img(a,b,str(i),w=140,h=90) for i,(a,b) in enumerate([("#e74c3c","#f39c12"),("#16a085","#3498db"),("#8e44ad","#e84393"),("#2c3e50","#27ae60")]*2,1))}</div></div>''',
    """.w .cs{display:flex;gap:10px;flex-wrap:wrap;overflow:hidden}.w .c{flex:1 1 150px;background:#c0392b;color:#fff;padding:26px;border-radius:8px;text-align:center}
.w .c1{animation:fl 1s both}.w .c2{animation:fr 1s .3s both}.w .c3{animation:fb 1s .6s both}
@keyframes fl{from{transform:translateX(-120%);opacity:0}}@keyframes fr{from{transform:translateX(120%);opacity:0}}@keyframes fb{from{transform:translateY(100px);opacity:0}}
.w .vw{overflow:hidden;margin-top:16px;border-radius:8px}.w .strip{display:flex;width:max-content;gap:6px;animation:sc 12s linear infinite}.w .strip img{width:140px;height:90px}@keyframes sc{to{transform:translateX(-50%)}}""")

add("css-only-modal-popup", "CSS-only Modal / Popup",
    "A modal opened and closed with the checkbox hack, no JavaScript.",
    '''<label for="m" class="btn">Open modal</label><input type="checkbox" id="m" hidden><div class="ov"><div class="md"><h3>Hello!</h3><p>This modal uses only CSS.</p><label for="m" class="btn">Close</label></div></div>''',
    """.w .ov{position:fixed;inset:0;background:rgba(0,0,0,.6);display:flex;align-items:center;justify-content:center;opacity:0;visibility:hidden;transition:.3s;z-index:100}
.w #m:checked~.ov{opacity:1;visibility:visible}.w .md{background:#fff;color:#4a1010;padding:24px;border-radius:12px;max-width:320px;transform:scale(.8);transition:.3s;text-align:center}
.w #m:checked~.ov .md{transform:scale(1)}.w label.btn{cursor:pointer;display:inline-block}""")

# ---------------- Typography & functions ----------------
add("responsive-typography", "Responsive Typography",
    "Font sizes that scale with the viewport using vw/rem and media queries.",
    '<h2 class="t1">Fluid heading (vw based)</h2><p class="t2">Body text uses rem and switches size at 700px. Resize the window to see it.</p>',
    """.w .t1{font-size:calc(1rem + 3vw);line-height:1.2}.w .t2{font-size:1rem}@media(min-width:700px){.w .t2{font-size:1.3rem;line-height:1.7}}""")

add("clamp-min-max-functions", "clamp(), min() and max() Functions",
    "Values that stay within limits while the window is resized.",
    '<h3 class="a">clamp(1.2rem, 4vw, 2.4rem)</h3><div class="b">width: min(90%, 400px)</div><div class="c">width: max(50%, 250px)</div>',
    """.w .a{font-size:clamp(1.2rem,4vw,2.4rem)}.w div{background:#ff6b6b;color:#fff;padding:12px;margin:8px 0}.w .b{width:min(90%,400px)}.w .c{width:max(50%,250px)}""")

add("calc-function", "CSS calc() Function",
    "Mix units in a calculation: percentages with pixels.",
    '<div class="a">width: calc(100% - 100px)</div><div class="b">width: calc(50% + 2rem)</div><div class="row"><div class="s">calc(33.33% - 10px)</div><div class="s">calc(33.33% - 10px)</div><div class="s">calc(33.33% - 10px)</div></div>',
    """.w div{background:#c0392b;color:#fff;padding:12px;margin:8px 0}.w .a{width:calc(100% - 100px)}.w .b{width:calc(50% + 2rem)}
.w .row{display:flex;gap:15px;background:none;padding:0}.w .s{margin:0;width:calc(33.33% - 10px);background:#ff6b6b}""")

add("complete-responsive-website", "Complete Responsive Website (HTML5, CSS3, Flexbox, Grid, Media Queries)",
    "Semantic layout with a Flexbox navbar, Grid content, and media queries.",
    '''<div class="cw"><header><b>MySite</b><nav><a href="#">Home</a><a href="#">Blog</a><a href="#">Contact</a></nav></header>
<section class="hero2"><h2>Welcome</h2><p>A fully responsive site.</p></section>
<section class="gr"><article>Feature One</article><article>Feature Two</article><article>Feature Three</article></section>
<section class="ab"><div>Main text about the site.</div><aside>Sidebar</aside></section><footer>&copy; 2026 MySite</footer></div>''',
    """.w .cw{background:#fff;border-radius:12px;overflow:hidden;color:#4a1010}.w header{display:flex;justify-content:space-between;align-items:center;padding:12px 18px;background:#4a1010;color:#fff;flex-wrap:wrap}
.w header nav{display:flex;gap:14px}.w header a{color:#fff;text-decoration:none}.w .hero2{padding:40px;text-align:center;background:linear-gradient(135deg,#c0392b,#ff6b6b);color:#fff}
.w .gr{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;padding:16px}.w .gr article{background:#ffe3e3;padding:24px;border-radius:8px;text-align:center}
.w .ab{display:grid;grid-template-columns:3fr 1fr;gap:12px;padding:0 16px 16px}.w .ab div,.w .ab aside{background:#fff0f0;padding:16px;border-radius:8px}
.w .cw footer{background:#4a1010;color:#fff;text-align:center;padding:10px}
@media(max-width:700px){.w .gr,.w .ab{grid-template-columns:1fr}.w header{flex-direction:column;gap:6px}}""")
