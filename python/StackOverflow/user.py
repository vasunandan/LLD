class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.points = 0
        self.questions = []
        self.answers = []
        self.votes = []
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def update_points(self,p):
        self.points+=p
    def get_points(self):
        return self.points