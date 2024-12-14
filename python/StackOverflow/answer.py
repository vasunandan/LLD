from user import User
from comment import Comment
class Answer():
    id_counter = 0
    def __init__(self,user,question_id):
        Answer.id_counter += 1
        self.id = Answer.id_counter
        self.user = user
        self.voters:List[User] = []
        self.comments:List[Comment] = []
    def upvote(self,user):
        self.voters.append(user)
    def add_comment(self,comment):
        self.comments.append(comment)