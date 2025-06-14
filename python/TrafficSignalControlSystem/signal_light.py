from typing import Literal
class SignalLight:
    def __init__(self,color:str,duration:int):
        self.color = color
        self.duration = duration
    def get_color(self):
        return self.color
    def get_duration(self):
        return self.duration