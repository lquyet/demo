with open("is.py", "r") as f:
    print(dir(f))


class FileContextManager:
    def __init__(self, file, mode):
        self.file = open(file, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


class CustomContextManager:
    def __init__(self):
        print("init")

    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")


with CustomContextManager() as c:
    print("entering with block")