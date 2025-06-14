def singleton(cls):
    _instances = {}
    def get_instance(cls,*args,**kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args,**kwargs)
        return _instances[cls]
    return get_instance

@singleton
class LinkedIn:
    def __init__(self):
        self.users = []
        self.logins = []
        self.jobs = []
    def sign_in(self,name,email,password):
        user = User(name,email,password)
        if user not in self.users:
            self.users.append(user)
            print("Signed in successfully")
        else:
            print("email already exist")
    def login(self,user):
        if user not in self.users:
            print("User not signed in")
            return
        for us in self.users:
            if us.email == user.email and us.name == user.name and us.password = user.password:
                self.logins.append(user)
                print("Login succss")
                return
        print("Cant login")
    def logout(self,user):
        # self.logins.discard(user)s
        # print("logout succss")
        pass


