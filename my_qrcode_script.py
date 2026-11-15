import qrcode

# Generate a QR code pointing directly to your live HTML/CSS portfolio
img = qrcode.make("https://jaivardhankotwal-ui.github.io/snai-portfolio/")

# Save the generated QR code as an image file
img.save("portfolio_qr.png")