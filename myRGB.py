import time
import picamera

width = 100
height =100

with picamera.PiCamera() as camera:
    camera.resolution = (width,height)
    camera.start_preview()
    time.sleep(2)
    camera.capture('image.data', 'rgb')
