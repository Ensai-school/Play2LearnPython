from abc import abstractmethod, ABC

# subject | observer pattern
# https://en.wikipedia.org/wiki/Observer_pattern
# GameObject = classe observable
# property and setters : https://www.python-course.eu/python3_properties.php
# https://refactoring.guru/fr/design-patterns/observer/python/example
# https://refactoring.guru/fr/design-patterns/observer

class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass