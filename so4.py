import time
from SimpleCV import *

camera = Camera(3,{'gain': 0, 'auto': 0})
while True:
   img = camera.getImage()
   img.drawText('X')
#   bina = img.binarize()
#   bina.show()
   img.show()
   time.sleep(0.01)
