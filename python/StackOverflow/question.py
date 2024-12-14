from typing import List
from user import User
from answer import Answer
from comment import Comment
class Question():
    id_counter = 0
    def __init__(self,user_id,tag):
        Question.id_counter += 1
        self.id = Question.id_counter
        self.tag = tag
        self.user_id = user_id
        self.voters:List[User] = []
        self.answers:List[Answer] = []
        self.comments:List[Comment] = []
    def change_tag(self,tag):
        self.tag = tag
    def get_userid(self):
        return user_id
    def upvote(self,user):
        user.change_score(0.1)
        self.voters.append(user)
    def add_answer(self,answer):
        self.user.change_score(1)
        self.answers.append(answer)
    def add_comment(self,comment):
        self.user.change_score(0.5)
        self.comment.append(comment)
    def get_total_votes(self):
        return len(self.voters)


