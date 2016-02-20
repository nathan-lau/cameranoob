import picamera
from time import sleep

camera = picamera.PiCamera()

##Camera Properties
camera.sharpness = 0
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

camera.start_preview() ##initiate preview

##play with brightness
for i in range(100):
    camera.brightness = i
    sleep(0.2)

camera.brightness = 50
camera.capture('image1.jpg') ##capture the first image
sleep(2)
camera.brightness = 60
camera.capture('image2.jpg')
sleep(2)
camera.brightness = 70
camera.capture('image3.jpg')
sleep(2)

camera.stop_preview() ##stop preview

##video
##camera.start_recording('video.h264')
##sleep(5)
##camera.stop_recording()
