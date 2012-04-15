from subprocess import call
import thread

def brink():
  call("mplayer mf://brookfield.jpg -mf fps=1 -loop 0 -fs", shell=True)
thread.start_new_thread( brink )

print "depois"

