
class Player():
    _counter = 0 
    def __init__(self,user_name):
        Player._counter += 1
        self.id = Player._counter
        self.name = user_name