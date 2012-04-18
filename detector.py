import opencv
from opencv import highgui
import time
import copy
from subprocess import call
import termios, sys, os, signal
import thread

TERMIOS = termios
def getkey():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
        new[6][TERMIOS.VMIN] = 1
        new[6][TERMIOS.VTIME] = 0
        termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
        c = None
        try:
                c = os.read(fd, 1)
        finally:
                termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
        return c
        
        
global THRESHOLD
global PEAK
THRESHOLD=30
PEAK=10000

global pro
import os
pro=os.getpid()

class Detector:
  def __init__(self):
    def ahead(nu):
        print "KEY PRESSED "
        k = getkey()
        if k=='\x1b' or k=='q':
            print "CAI FORA"
            os.kill(pro, signal.SIGKILL)
            sys.exit(0)
            raise SystemExit
    thread.start_new_thread ( ahead, (1,) )
    def get_image():
        try:
            im = highgui.cvQueryFrame(camera)
            return opencv.adaptors.Ipl2PIL(im)
        except Exception: 
            print "Error: camera disconnected"
            sys.exit()
            raise SystemExit

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

    c=0
    while True: 

        c+=1
        im = get_image()
        if im==None or ig==None:
            sys.exit()

            
        h=difere(im,ig)
        print '*** %08d ***' % h
        if h>PEAK and c>50:
            print "toca video"
            #g.emit("eof",1)
            #.loadfile("../stood.mov")
            call("mplayer ../stood.mov -fs", shell=True)
            c=0
            time.sleep(5) 
        ig=copy.copy(im)
    exit()

        




      

  

      

