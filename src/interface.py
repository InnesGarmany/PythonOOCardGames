from abc import ABC, abstractmethod

class Input(ABC):
    
    @abstractmethod
    def get_input(self, message):
        pass