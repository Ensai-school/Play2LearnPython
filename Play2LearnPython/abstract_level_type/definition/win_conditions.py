from abc import ABC, abstractmethod

class WinConditions(ABC):

    @abstractmethod
    def __bool__(self):
        pass
