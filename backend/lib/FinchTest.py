from BirdBrain import Finch
import time

myFinch = Finch()

myFinch.playNote(60,0.5)

for i in range(0,10):
    myFinch.setBeak(100, 100, 100)
    time.sleep(1)
    myFinch.setBeak(0, 0, 0)
    time.sleep(1)
	
myFinch.stopAll()
