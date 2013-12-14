import time
from SimpleCV import *

camera = Camera(3,{'brightness': 0.5})
while True:
   img = camera.getImage()
   img.drawText('X')
#   bina = img.binarize()
#   bina.show()
   gain = camera.getProperty("gain")
   brightness = camera.getProperty("brightness")
   saturation = camera.getProperty("saturation")
   contrast = camera.getProperty("contrast")
   print( "gain", gain, "brightness", brightness, "saturation", saturation, "contrast", contrast)
   img.show()
   time.sleep(0.1)
