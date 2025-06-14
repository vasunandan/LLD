from commentable import Commentable
from commnet import Comment
class Answer(Commentable,votable):
    def __init__(self,author,content):
        self.comments = []
        self.votes = []
        self.author = author
        self.content = content
    def upVote(self,user:User):
        bool flag = True
        for vote in self.votes:
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
    