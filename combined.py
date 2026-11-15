import qrcode
import os

# 1. Read your exact turtle dragon script safely
if os.path.exists("dragon.py"):
    with open("dragon.py", "r") as f:
        dragon_code = f.read()
else:
    dragon_code = "# Turtle drawing code placeholder"

# 2. Build index.html so GitHub Pages loads it automatically at the root URL
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Turtle Dragon Animation</title>
    <script src="https://cdn.jsdelivr.net/npm/skulpt@1.2.0/dist/skulpt.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/skulpt@1.2.0/dist/skulpt-stdlib.js"></script>
    <style>
        body {{
            background: #0b0e14;
            color: white;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            font-family: sans-serif;
        }}
        #canvas-container {{
            border: 2px solid #1f2937;
            border-radius: 12px;
            background: #111827;
            padding: 10px;
        }}
        .link-btn {{
            marginTop: 20px;
            padding: 10px 20px;
            background: #3b82f6;
            color: white;
            text-decoration: none;
            borderRadius: 6px;
            fontWeight: bold;
        }}
    </style>
</head>
<body>
    <h2>Live Turtle Dragon Animation</h2>
    <div id="canvas-container">
        <div id="turtle_canvas"></div>
    </div>
    <a class="link-btn" href="https://jaivardhankotwal-ui.github.io/snai-portfolio/" target="_blank">Visit My Portfolio</a>

    <script type="text/javascript">
        function outf(text) {{}}
        function builtinRead(x) {{
            if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
                throw "File not found: '" + x + "'";
            return Sk.builtinFiles["files"][x];
        }}
        function runPythonCode() {{
            var prog = `{dragon_code}`;
            Sk.pre = "output";
            Sk.configure({{ output: outf, read: builtinRead }});
            (Sk.TurtleGraphics || (Sk.TurtleGraphics = {{}})).target = 'turtle_canvas';
            Sk.TurtleGraphics.width = 400;
            Sk.TurtleGraphics.height = 400;
            Sk.misceval.asyncToPromise(function() {{
                return Sk.importMainWithBody("<stdin>", false, prog, true);
            }}).catch(function(err) {{
                console.error(err.toString());
            }});
        }}
        window.onload = runPythonCode;
    </script>
</body>
</html>
"""

# Save as index.html so GitHub Pages serves it directly by default
with open("index.html", "w") as f:
    f.write(html_content)

# 3. Generate QR code pointing directly to the root GitHub Pages URL
repo_root_url = "https://jaivardhankotwal-ui.github.io/Diwali_worksheet_13b/"
img = qrcode.make(repo_root_url)
img.save("dragon_qr.png")

print("Success! index.html and dragon_qr.png generated successfully.")

# 4. Run local turtle window too
import dragon