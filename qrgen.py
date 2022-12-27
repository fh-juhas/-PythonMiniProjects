import pyqrcode
from PIL import Image, ImageDraw
import png

data = 'https://www.facebook.com/fhjuhas.cse'
img = pyqrcode.create(data)
#img.save('C:/Users/fhjuh/OneDrive/Pictures/qr/fhj.png')
#print(img.terminal(quiet_zone=1))
img.png("fhj_fb.png",scale=8)