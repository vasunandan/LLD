from profile import Profile
class User:
    def __init__(self,name,email,password,profile=Profile()):
        self.name = name
        self.email = email
        self.password = password
        self.profile = profile
        self.employer = False
        self.connections = []
        self.request = []

    def raise_request(self,user):
        pass # add into the request

    def accept_req(self,user):
        pass # and move requst arr to connection and noify the user , which add into there connections

    def __eq__(self,other):
        if not isinstance(other,User):
            return NotImplemented
        return self.email == other.email

    def notify_connections(self,msg):
        for conn in self.connections:
            conn.notify(msg)

    def notify(self,msg):
        print(f"Notfied '{msg}'")
