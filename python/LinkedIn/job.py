class Job:
    def __init__(self,title,description,requirements,location):
        self.id = id(self)
        self.title = title
        self.description = description
        self.requirements = requirements
        self.location = location
        self.applicants = []

    def __eq__(self,other):
        if not isinstance(other,User):
            return NotImplemented
        return self.id == other.id
    def apply(self,user):
        if user not in self.applicants:
            self.applicants.append(user)
            print("Applied")
        else:
            print("Already applied")
    
    