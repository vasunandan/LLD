from signal import Signal
from signal_light import SignalLight
from intersection import Intersection
red1 = SignalLight("red",5)
yellow1 = SignalLight("yellow",4)
green1 = SignalLight("green",3)
siganl1 = Signal(red1,yellow1,green1)

red2 = SignalLight("red",7)
yellow2 = SignalLight("yellow",3)
green2 = SignalLight("green",6)
siganl2 = Signal(red2,yellow2,green2)

intersection = Intersection([siganl1,siganl2])
intersection.start_signal()
intersection.toggle_emergency()
intersection.start_signal()
# intersection.toggle_emergency()
# intersection.start_signal()