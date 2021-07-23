from abc import abstractmethod
from abstract_level_type.definition.game_object import GameObject

class PromptObject(GameObject):
    name = "Default Prompt Object"
    is_editable = False
    def __init__(self, common_dict : dict, custom_dict : dict, game_object_list : list) -> None:
        super().__init__(common_dict, custom_dict, game_object_list)
        self.id = common_dict['id']
    
    @abstractmethod
    def update(self):
        """Abstract method
        Each GameObject can be updated every frame
        """
        pass
    
    @abstractmethod
    def __str__(self):
        pass
