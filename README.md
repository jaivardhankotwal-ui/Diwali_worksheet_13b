# README

1. What it does. One sentence.
It combines a Python turtle drawing script with the qrcode library to generate a scannable QR code that opens the live wireframe dragon animation on a mobile browser via GitHub Pages.

2. Which two libraries, and what each contributes.
turtle: Renders the coordinate-based wireframe dragon graphics; qrcode: Generates the 2D matrix image code pointing to the hosted live webpage.

3. What someone needs installed before they run it.
Python 3, the qrcode library (pip install qrcode), and git.

4. The exact command to run it.
python3 combined.py

5. What the output looks like. Show it.
Success! index.html and dragon_qr.png generated successfully.

6. What it can't do yet.
It cannot generate the QR code or render the turtle canvas natively without an active internet connection for the Skulpt CDN and GitHub Pages routing.
