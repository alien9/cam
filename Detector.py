

import opencv
from opencv import highgui
import time
import copy
camera = highgui.cvCreateCameraCapture(-1)
THRESHOLD=40
PEAK=3000
def get_image():
    im = highgui.cvQueryFrame(camera)
    #detect(im)
    #convert Ipl image to PIL image
    return opencv.adaptors.Ipl2PIL(im)

im=get_image()
W=im.size[0]
H=im.size[1]

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
    

ig=copy.copy(im)
while True:    
    im = get_image()
    h=difere(im,ig)
    print '%08d' % h
    if h>PEAK:
        time.sleep(10)
    ig=copy.copy(im)
    
    

