#!/usr/bin/env python
from subprocess import call
import thread
import detector

def brink(what):
  call("mplayer ../logoo.mov -loop 0 -fs < /dev/null &", shell=True)

thread.start_new_thread ( brink, (1,) )
#brink(1)
d=detector.Detector()
