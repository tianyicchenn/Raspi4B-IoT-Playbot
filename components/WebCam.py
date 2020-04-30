import os
import time


class WebCam:
    def capture(self):
        t = time.gmtime()
        timestamp = time.strftime("%Y-%m-%d_%H:%M:%S", t)
        impath = "/home/pi/Desktop/Camera/webCam/{}.jpg".format(timestamp)
        os.system("fswebcam --no-banner -r 1280x720 {}".format(impath))
        return impath


'''
webCam = WebCam()
print(webCam.capture())
'''
