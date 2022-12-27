import pyqrcode
from PIL import Image, ImageDraw
import png

data = input("Enter data to convert into qrcode: ")
img = pyqrcode.create(data)
#img.save('C:/Users/fhjuh/OneDrive/Pictures/qr/fhj.png')
#print(img.terminal(quiet_zone=1))
img.png("data.png",scale=8)
