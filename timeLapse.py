import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (2592, 1944)
    camera.start_preview()
    time.sleep(2)
    for filename in camera.capture_continuous('img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        time.sleep(2)
