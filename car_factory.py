from abc import ABC, abstractmethod

class CarFactory(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    
class ConcreteCreator1(Creator):
    def factory_method(self) -> Car:
        return ConcreteProduct1()