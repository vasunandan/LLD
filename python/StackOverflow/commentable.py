from abc import ABC,abstractmethod
from user import User


class Comentable(ABC):
    @abstractmethod
    def add_comment(self,user:User,content:str):
        pass
    @abstractmethod
    def get_comments(self):
        pass
    # @abstractmethod
    # def downVote(self):
    #     pass