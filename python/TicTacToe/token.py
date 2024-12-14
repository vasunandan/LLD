from enum import ENUM

class Tokens(ENUM):
    empty = -1
    circle = 0
    cross = 1



# from multiprocessing import Process

# def modify_dict(local_dict):
#     local_dict["key"] = "modified"
#     print(f"Dictionary in Process: {local_dict}")

# if __name__ == "__main__":

#     original_dict = {"key": "original"}
#     process = Process(target=modify_dict, args=(original_dict,))
#     process.start()
#     process.join()
#     print(f"Original Dictionary After Process: {original_dict}")


