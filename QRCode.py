import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Install in Terminal
# (1) pip install qrcode
# (2) pip install pyzbar
# (3) pip install pillow

# Input Link and File Path Location
link = input("Enter Link for QRCode: ")
QRfileName = input("Enter File Name for QRCode (Ex: dot.png): ")

# Make, Save, Show the QR code
currentQR = qrcode.make(link)
currentQR.save(QRfileName, scale=8)
currentQR.show(QRfileName) # OR Input "start QRfileName.png" in terminal