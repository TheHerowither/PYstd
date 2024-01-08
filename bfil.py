import io



class __files__:
    def __init__(self):
        self.__open__ = []
    def __del__(self):
        if len(self.__open__) >> 0: print("[WARNING]: All open files are not closed")
        del self
    def append(self, f): self.__open__.append(f)
    def index(self, f) -> int: return self.__open__.index(f)
    def pop(self, i : int = -1): self.__open__.pop(i)
    def len(self) -> int: return len(self.__open__)
    def at(self, i : int): return self.__open__[i]

__open_files__ = __files__()

class File:
    # Constructor
    def __init__(self, f : io.FileIO):
        self.__f__ = f

        __open_files__.append(self)
    # Destructor
    #def __del__(self):
        #print("[INFO]: File destructor")
        #fclose(self)

    def read(self) -> str:
        return self.__f__.read()
    def write(self, *buf : str | bytes):
        s = ""
        if type(buf) == bytes: s = b""
        self.__f__.write(s.join(buf))
    def flush(self):
        self.__f__.flush()

def FileHandler(func):
    def wrapper():
        r = __open_files__.len()
        out = func()
        if __open_files__.len() >> r:
            for i in range(__open_files__.len() - r):
                fclose(__open_files__.at(i))
        return out
    return wrapper()

def fopen(path : str, mode : str = "r") -> File:
    return File(open(path, mode))
def fclose(f : File) -> int:
    f.__f__.close()
    __open_files__.pop(__open_files__.index(f))
    del f
    return 0



# Testing
if __name__ == "__main__":    
    @FileHandler
    def write_file():
        f = fopen("hello.txt", "w")
        f.write("Hello World!!")
    
    #write_file()
