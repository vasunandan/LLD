def singleton(cls):
    instances = {}
    def get_instances(*args):
        if cls not in instances:
            instances[cls] = cls(*args)
        return instances[cls]
    return get_instancess

@singleton
class StackOverFlow:
    def __init__(self,pages:int):
        self.pages = [page for i in range pages]
