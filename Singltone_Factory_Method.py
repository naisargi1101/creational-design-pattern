'''
Singletone Design Pattern: 
    - It is a way to provide one and only one object of a particular type. 
    - It involves only one class to create methods and specify the objects. 
'''

# Method 1: Classic Approach getInstance() method
class Singltone:
    __instance = None
    hi = "hello"

    @staticmethod
    def getInstance():
        if Singltone.__instance == None:
            Singltone.__instance = Singltone()
        return Singltone.__instance
    
    def __init__(self):
        if Singltone.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singltone.__instance = self

if __name__ == "__main__":
    a = Singltone()
    print(a)
    # b must raise an exception because it is a singleton
    b = Singltone()
    print(b)
    # c must be the same object as a
    c = Singltone.getInstance()
    print(c)

# Method 2: Monostate/Borg Singleton Design pattern
class Singltone:
    __shared_state = dict()
    def __init__(self) -> None:
        self.__dict__ = self.__shared_state
        self.state = "Naisargi"
    
    def __str__(self):
        return self.state

if __name__ == "__main__":
    a = Singltone()
    b = Singltone()
    a.state = "Naisargi Savaliya"
    b.state = "Savaliya Naisargi"
    print(a)
    print(b)

# Method 3: Using Locking
import threading
class Singltone:
    __instance = None
    __lock = threading.Lock()

    @classmethod
    def instance(cls):
        if not cls.__instance:
            with cls.__lock:
                if not cls.__instance:
                    cls.__instance = cls()
        return cls.__instance

if __name__ == "__main__":
    class X(Singltone):
        pass
    class Y(Singltone):
        pass
    
    a1, a2 = X.instance(), X.instance()
    b1, b2 = Y.instance(), Y.instance()
    assert a1 is a2
    assert b1 is b2
    assert a1 is not b1
    print(a1)
    print(a2)
    print(b1)
    print(b2)
