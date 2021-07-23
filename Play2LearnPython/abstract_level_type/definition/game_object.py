from abc import abstractmethod
from core.observer_pattern.subject import Subject

class GameObject(Subject):
    is_editable = False
    def __init__(self, common_dict : dict, custom_dict : dict, game_object_list :list):
        super().__init__()
        self.game_object_list = game_object_list
        if custom_dict is not None :
            for key in custom_dict.keys() :
                setattr(self,key, custom_dict[key])

    def notify(self):
        for observer in self.observers :
            observer.update()

    @abstractmethod
    def update(self):
        """Abstract method
        Each GameObject can be updated every frame

        The GameObject receives a list of info about the others GameObjects
        """
        pass
    
    @abstractmethod
    def __str__(self):
        """Abstract method
        Each GameObject can be printed to show info

        Note : some type of level don't show the stdout, the print method is then useless
        """
        pass