#import opencv
#from opencv import highgui

import cv2.cv as cv
import numpy as np

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
PEAK=1000

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
            img = cv.QueryFrame(camera)
            return img
            #im = highgui.cvQueryFrame(camera)
            #return opencv.adaptors.Ipl2PIL(im)
        except Exception: 
            print "Error: camera disconnected"
            sys.exit()
            raise SystemExit
    def total(a):
        d=0
        x=0
        while x<W:
            y=0
            while y<H:
                p=a[y,x]
                d+=abs(p[0]+p[1]+p[2])
                y+=THRESHOLD
            x+=THRESHOLD
        return d    
    
    def difere(a,b):
        d=0
        x=0
        while x<W:
            y=0
            while y<H:
                #p=a.getpixel((x,y))
                #q=b.getpixel((x,y))
                p=a[y,x]
                q=b[y,x]
                d+=abs(p[0]-q[0]+p[1]-q[1]+p[2]-q[2])
                y+=THRESHOLD
            x+=THRESHOLD
        return d
    #camera = highgui.cvCreateCameraCapture(-1)
    camera = cv.CaptureFromCAM(0)
    img = cv.QueryFrame(camera)
    #W=im.size[0]
    #H=im.size[1]
    W=img.width
    H=img.height
    im=total(img)

    c=0
    while True: 

        c+=1


        h=abs(im-total(cv.QueryFrame(camera)))
        #h=difere(im,ig)
        print '*** %08d ***' % h
        if h>PEAK and c>50:
            print "toca video"
            #g.emit("eof",1)
            #.loadfile("../stood.mov")
            call("mplayer ../stood.mov -fs", shell=True)
            c=0
            time.sleep(5) 
        im = total(cv.QueryFrame(camera))
    exit()

        




      

  

      

