from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass


class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of the abstract method")

obj1 = ConcreteClass()
obj1.abstract_method()


class DerivedClass(ABC):
    def __init__(self):
        pass

obj2 = DerivedClass()
