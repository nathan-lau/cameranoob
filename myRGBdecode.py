from __future__ import division
import picamera
import time

#matplotlib inline
#import matplotlib

#import pylab as plt
#import matplotlib.image as mpimg

import numpy as np
#import matplotlib.pyplot as plt

width = 1280
height = 1020
stream = open('image.data', 'w+b')

# Capture the image in RGB format
with picamera.PiCamera() as camera:
    camera.resolution = (width, height)

    ##Camera Properties
    camera.sharpness = 20
    camera.contrast = 0
    camera.brightness = 50
    camera.saturation= 0
    camera.ISO = 0
    camera.video_stabilization = False
    camera.exposure_compensation = 0
    camera.exposure_mode = 'auto'
    camera.meter_mode = 'average'
    camera.awb_mode = 'auto'
    camera.image_effect = 'none'
    camera.color_effects = None
    camera.rotation = 0
    camera.hflip = False
    camera.vflip = False
    camera.crop = (0.0 ,0.0, 1.0, 1.0)
    ##End Camera Properties
    
    camera.start_preview()
    time.sleep(2)
    camera.capture(stream, 'rgb')
    
# Rewind the stream for reading
stream.seek(0)

# Calculate the actual image size in the stream (accounting for rounding
# of the resolution)
fwidth = (width + 31) // 32 * 32
fheight = (height + 15) // 16 * 16

# Load the data in a three-dimensional array and crop it to the requested
# resolution
image = np.fromfile(stream, dtype=np.uint8).\
        reshape((fheight, fwidth, 3))[:height, :width, :]

# If you wish, the following code will convert the image's bytes into
# floating point values in the range 0 to 1 (a typical format for some
# sorts of analysis)
image = image.astype(np.float)
image = image / 255.0

# Image Display

#def displayImage(image):
#    plt.imshow(image)
#    plt.show()
