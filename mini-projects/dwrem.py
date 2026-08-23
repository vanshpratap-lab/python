import time 
import winsound

class Interval:
    def __init__(self,interval,frequency,duration):
        self.interval = interval
        self.frequency = frequency # will keep 1000 HZ
        self.duration = duration # will keep 4000 milliseconds
        

    def start_reminder(self):
        while True:
            print("please drink water")
            winsound.Beep(self.frequency,self.duration) # forgot to use capital B in beep
            time.sleep(self.interval) # moved this from construtot too this method 

sound = Interval(5,1000,4000)
sound.start_reminder()




