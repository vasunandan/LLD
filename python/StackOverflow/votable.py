from abc import ABC,abstractmethod
from user import User
class Votable(ABC):
    @abstractmethod
    def upVote(self,user:User):
        pass
    @abstractmethod
    def get_votes(self):
        pass
    # @abstractmethod
    # def downVote(self):
    #     pass