from abc import ABC, abstractmethod
class Output(ABC):
    
    @abstractmethod
    def output(self, message):
        pass