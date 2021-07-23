from abc import ABC, abstractmethod, abstractproperty

class Parser(ABC):
    def __init__(self, file_path):
        self._file_path = file_path
    
    @property
    def file_path(self):
        return self._file_path
    @file_path.setter
    def file_path(self, value):
        self._file_path = value

    @abstractmethod
    def load(self):
        """ Parses the file as a dict
        """
        pass