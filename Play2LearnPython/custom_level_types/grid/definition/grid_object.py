from abc import abstractmethod
from abstract_level_type.definition.game_object import GameObject

class GridObject(GameObject):
    game_object_character = "?"
    name = "Default Game Object"
    _is_position_editable = False

    def __init__(self, common_dict : dict, custom_dict : dict, game_object_list : list) -> None:
        super().__init__(common_dict, custom_dict, game_object_list)
        self._position = common_dict['position']
    
    @abstractmethod
    def update(self):
        """Abstract method
        Each GameObject can be updated every frame
        """
        pass

    def __str__(self):
        return f"Type : {self.name}\nCharacter : {self.game_object_character}\nID : {self.id}\nMEMORY : {hex(id(self))}\nPosition : ({self._position[0], self._position[1]})\n\n"
    
    """
    GETTER
    """
    @property
    def position(self):
        return self._position
    
    # """
    # SETTER
    # """
    # @position.setter
    # def position(self, value):
    #     self._position = value
    #     # si la variable position est modifiée
    #     # (donc utilisation de la fonction setter)
    #     # on notifie les observeurs
    #     self.notify()

