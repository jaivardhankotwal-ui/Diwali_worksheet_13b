# SNAI Diwali Assignment - v0.3: Live Turtle Dragon QR Code Integration

* **Project Overview:**
  This repository contains the final v0.3 implementation for the university SNAI Diwali assignment[cite: 1]. It dynamically combines a Python turtle graphics script (`dragon.py`)[cite: 1, 3] with the `qrcode` library[cite: 1], packaging the turtle drawing into an interactive HTML canvas runner (`index.html`) powered by Skulpt. This enables scanning the generated QR code (`dragon_qr.png`)[cite: 1] to render the exact same wireframe dragon animation live on mobile browsers via GitHub Pages[cite: 1].

* **Key Files:**
  * `dragon.py`: Contains the core coordinate-based turtle wireframe drawing script[cite: 1, 3].
  * `combined.py` / `v03_combined.py`: The integration script that reads the turtle code, wraps it into a web-hosted HTML runner, and generates the scannable QR code.
  * `index.html`: The root deployment file that executes the turtle drawing inside a browser canvas environment.
  * `dragon_qr.png`: The scannable QR code linking directly to the live turtle animation[cite: 1].
