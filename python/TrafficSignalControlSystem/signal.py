import time
from signal_light import SignalLight
class Signal:
    def __init__(self,red:SignalLight,yellow:SignalLight,green:SignalLight):
        self.red = red
        self.yellow = yellow
        self.green = green
    def start_signal(self):
        for light in [self.red,self.yellow,self.green]:
            print(light.color)
            time.sleep(light.duration)
        print("Done Signaling")
            
