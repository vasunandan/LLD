class Comment():
    id_counter = 0
    def __init__(self,user,commet):
        Comment.id_counter += 1
        self.id = Comment.id_counter
        self.user = user
        self.comment = comment

