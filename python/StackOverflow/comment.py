class Comment:
    def __init__(self,author,content:str):
        self.id = id(self)
        self.content = content
        self.author = author
