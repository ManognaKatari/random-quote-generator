import qrcode
data = "https://manognakatari.github.io/random-quote-generator/" 
# Create QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
# Generate and save the image
img = qr.make_image(fill="black", back_color="white")
img.save("my_qr_code.png")

print("QR code with URL generated and saved as my_qr_code.png")
