from custom_level_types.grid.definition.grid_object import GridObject

class GridObstacle(GridObject):
    is_editable = False
    game_object_character = "X"
    name = "Obstacle"
    def __init__(self,  common_dict : dict, custom_dict : dict, game_object_list : list) -> None:
        super().__init__(common_dict, custom_dict, game_object_list)
    
    def update(self, game_objects_list):
        pass
