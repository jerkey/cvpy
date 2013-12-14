import time
from SimpleCV import *

camera = Camera(4,{'gain': 9})
while True:
   img = camera.getImage()
   img.drawText('X')
#   bina = img.binarize()
#   bina.show()
   img.show()
   time.sleep(0.01)
