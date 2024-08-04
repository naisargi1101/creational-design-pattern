'''
Prototype Design Pattern:
    - The Prototype Method Design Pattern in Python enables the creation of new objects by cloning existing ones, promoting efficient object creation and reducing overhead. 
'''

from abc import ABC, abstractmethod
import copy

class ProtoType(ABC):
    @abstractmethod
    def clone(self):
        pass

class Object(ProtoType):
    def __init__(self, name):
        self.name = name

    def clone(self):
        return copy.deepcopy(self)

if __name__ == "__main__":
    obj1 = Object("Naisargi")
    obj2 = obj1.clone()
    print(obj1)
    print(obj2)
    print(obj1 == obj2)
    print(obj1 is obj2)
    print(obj1.name)
    print(obj2.name)
    obj2.name = "Savaliya"
    print(obj1.name)
    print(obj2.name)
