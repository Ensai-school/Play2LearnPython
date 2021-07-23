from custom_level_types.grid.definition.grid_object import GridObject

class GridTeleporteur(GridObject):
    is_editable= True
    game_object_character = "T"
    name = "Teleporter"
    def __init__(self,  common_dict : dict, custom_dict : dict, game_object_list : list) -> None:
        self.destination = common_dict['destination']
        if not isinstance(self.destination, tuple):
            raise TypeError
        super().__init__(common_dict, custom_dict, game_object_list)
    
    def update(self, game_objects_list):
        """Update method of teleporter. Checks on each frame if a GameObject needs to be teleported
        """
        for GameObject in game_objects_list :
            if GameObject.is_editable :
                if self.position[0] - 1 <= GameObject.position[0] <= self.position[0] + 1 and self.position[1] - 1 <= GameObject.position[1] <= self.position[1] + 1 and isinstance(GameObject,Personnage):
                    GameObject.position = self.destination