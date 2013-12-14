import time
from SimpleCV import *

gain = 1
while True:
   camera = Camera(4,{'gain': gain})
   img = camera.getImage()
   img.drawText('X')
#   bina = img.binarize()
#   bina.show()
   img.show()
   time.sleep(5)
   gain += 1
   del camera
