import opencv
from opencv import highgui
import time
import copy
from subprocess import call

global THRESHOLD
global PEAK
THRESHOLD=30
PEAK=10000
class Detector:
  def __init__(self):
    def get_image():
        im = highgui.cvQueryFrame(camera)
        #detect(im)
        #convert Ipl image to PIL image
        return opencv.adaptors.Ipl2PIL(im)
    def difere(a,b):
        d=0
        x=0
        while x<W:
            y=0
            while y<H:
                p=a.getpixel((x,y))
                q=b.getpixel((x,y))
                d+=abs(p[0]-q[0]+p[1]-q[1]+p[2]-q[2])
                y+=THRESHOLD
            x+=THRESHOLD
        return d
    camera = highgui.cvCreateCameraCapture(-1)

    im=get_image()
    W=im.size[0]
    H=im.size[1]
    ig=copy.copy(im)
    
    while True:   

        im = get_image()
        h=difere(im,ig)
        print '*** %08d ***' % h
        if h>PEAK:
            print "toca video"
            call("mplayer -vf crop=830:1088:670:0 stand.mov -fs", shell=True)
            time.sleep(5) 
        ig=copy.copy(im)
        




      

  

      

