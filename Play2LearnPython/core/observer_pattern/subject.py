from abc import abstractmethod, ABC

# subject | observer pattern
# https://en.wikipedia.org/wiki/Observer_pattern
# GameObject = classe observable
# property and setters : https://www.python-course.eu/python3_properties.php
# https://refactoring.guru/fr/design-patterns/observer/python/example
# https://refactoring.guru/fr/design-patterns/observer

class Subject(ABC):
    def __init__(self):
        self.observers = []
    def register(self, observer):
        self.observers.append(observer)
    def unregister(self, observer):
        self.observers.pop( self.observers.index(observer) )
    @abstractmethod
    def notify(self, data):
        pass