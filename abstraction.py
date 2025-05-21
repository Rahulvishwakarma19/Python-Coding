from abc import ABC,abstractmethod
class Family(ABC):
    def __init__(self,mony):
        self.mony=mony

    @abstractmethod
    def home(self):
        pass
    def car(self):
        print("I have more car..")