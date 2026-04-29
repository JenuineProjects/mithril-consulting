import os

STYLE = """<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;600;700&display=swap');
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Inter', sans-serif; background: #0a0a14; color: #e8ecf4; line-height: 1.8; padding: 2rem; }
.container { max-width: 900px; margin: 0 auto; }
.back-link { display: inline-flex; align-items: center; gap: 0.5rem; color: #ef4444; text-decoration: none; font-size: 0.85rem; font-weight: 500; margin-bottom: 2rem; padding: 0.5rem 1rem; border: 1px solid #1e2038; border-radius: 6px; transition: all 0.3s; }
.back-link:hover { border-color: #ef4444; background: rgba(239,68,68,0.06); }
h1 { font-family: 'Playfair Display', serif; font-size: 2.4rem; font-weight: 700; margin-bottom: 0.5rem; }
h2 { font-family: 'Playfair Display', serif; font-size: 1.6rem; font-weight: 600; margin-top: 2.5rem; margin-bottom: 1rem; color: #e8ecf4; border-bottom: 1px solid #1e2038; padding-bottom: 0.5rem; }
h3 { font-size: 1.15rem; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.75rem; color: #b8c4d8; }
h4 { font-size: 1rem; font-weight: 600; margin-top: 1rem; margin-bottom: 0.5rem; }
p { color: #8892a8; margin-bottom: 1rem; }
strong { color: #e8ecf4; }
em { color: #b8c4d8; }
blockquote { border-left: 3px solid #ef4444; padding: 0.75rem 1.25rem; margin: 1rem 0; background: rgba(239,68,68,0.05); border-radius: 0 8px 8px 0; color: #8892a8; font-size: 0.92rem; }
ul, ol { margin: 0.75rem 0 1rem 1.5rem; color: #8892a8; }
li { margin-bottom: 0.4rem; }
table { width: 100%; border-collapse: collapse; margin: 1rem 0 1.5rem; font-size: 0.88rem; }
th { background: #161628; color: #ef4444; text-align: left; padding: 0.75rem 1rem; border: 1px solid #1e2038; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; font-size: 0.75rem; }
td { padding: 0.65rem 1rem; border: 1px solid #1e2038; color: #8892a8; }
tr:hover td { background: rgba(239,68,68,0.03); }
hr { border: none; border-top: 1px solid #1e2038; margin: 2rem 0; }
.meta { color: #585f72; font-size: 0.88rem; margin-bottom: 2rem; line-height: 1.6; }
.divider { width: 60px; height: 3px; background: linear-gradient(90deg, #ef4444, #f59e0b); border-radius: 2px; margin: 1.5rem 0; }
a { color: #ef4444; }
code { background: #161628; padding: 0.15rem 0.4rem; border-radius: 3px; font-size: 0.88em; color: #b8c4d8; }
pre { background: #0c0c1a; border: 1px solid #1e2038; border-radius: 6px; padding: 1rem; overflow-x: auto; margin: 1rem 0; }
pre code { background: none; padding: 0; color: #b8c4d8; font-size: 0.85rem; line-height: 1.6; }
</style>"""

PAGES = [
    ("aragorn-review-1-saruman.html",  "Aragorn's Review of Saruman — Iteration 12"),
    ("aragorn-review-2-galadriel.html","Aragorn's Review of Galadriel — Iteration 12"),
    ("aragorn-review-3-gimli.html",    "Aragorn's Review of Gimli — Iteration 12"),
    ("aragorn-review-4-pippin.html",   "Aragorn's Review of Pippin — Iteration 12"),
]

for outname, title in PAGES:
    body_path = os.path.join("reports", "__body_" + outname)
    with open(body_path, encoding="utf-8") as f:
        body = f.read()
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Mithril Consulting</title>
{STYLE}
</head>
<body>
<div class="container">
<a href="../index.html" class="back-link">&larr; Back to Portfolio</a>
<div class="divider"></div>
{body}
</div>
</body>
</html>
"""
    out_path = os.path.join("reports", outname)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    os.remove(body_path)
    print("Wrote", out_path)
