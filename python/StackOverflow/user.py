class User():
    _id_counter = 1
    def __init__(self,name):
        User._id_counter += 1
        self.id = User._id_counter
        self.name = name
        self.score = 0
    def change_name(self,name):
        self.name = name
    def change_score(self,p):
        self.score += p
    def get_score(self):
        return self.score
    