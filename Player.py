from subprocess import call
import thread
import detector

def brink(what):
  call("mplayer mf://brookfield.jpg -mf fps=0.001 -loop 0 -fs < /dev/null &", shell=True)
#thread.start_new_thread ( brink, (1,) )
brink(1)
d=detector.Detector()
