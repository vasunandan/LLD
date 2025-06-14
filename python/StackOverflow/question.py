from user import User
from votable import Votable
from vote import Vote
from commentable import Commentable

class Question(Votable,Commentable):
    def __init__(self,user:User,keyword:str,tags:List[str]=[]):
        self.user = user
        self.keyword = keyword
        self.tags = tags
        self.answers = []
        self.comments = []
        self.votes = []
    def add_tag(tag:str):
        self.tags.append(tag)
    def upVote(self,user:User):
        bool flag = True
        for vote in votes:
            if vote.get_user() == user:
                flag = False
        if flag:  
            self.vote.append(Vote(users))
    def get_votes(self):
        return len(self.votes)
    def add_comment(self,user,content):
        self.comments.append(Comment(user,content))
    def get_comments(self):
        return self.comments
    def add_answer(self,answer):
        self.answers.append(answer)
    # def downVote(self,user:User):
    #     bool flag = True
    #     for vote in votes:
    #         if vote.get_user() == user:
    #             flag = False
    #     if flag:  
    #         self.vote.append(Vote(users))
