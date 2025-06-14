class Intersection:
    def __init__(self,siganls):
        self.signals = siganls
        self.roads = len(self.signals)
        self.emergency = False
        self.idx = 0
    def start_signal(self):
        if not self.emergency:
            self.idx%=self.roads
            self.signals[self.idx].start_signal()
            print("Done with signal: ",self.idx)
            self.idx+=1
        else:
            print("Its emergency")
    def toggle_emergency(self):
        self.emergency ^= True
    def get_emergency_status(self):
        if self.emergency:
            print("ist an emerg")
        else:
            print("Normal time")

        

