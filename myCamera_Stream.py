import io
import picamera
import time


width = 1920
height = 1080
stream = open('image.jpg', 'wb')

# Capture the image in RGB format
with picamera.PiCamera() as camera:
    camera.resolution = (width, height)
    #camera.resolution = camera.MAX_IMAGE_RESOLUTION

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
    camera.capture(stream)
