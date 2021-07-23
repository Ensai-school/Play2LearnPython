#Custom game object of this level
from custom_level_types.prompt.definition.prompt_object import PromptObject
from custom_level_types.grid.definition.grid_object import GridObject
from abstract_level_type.definition.game_object import GameObject

class OldBook(PromptObject):
    is_editable = True
    def __init__(self,common_dict,custom_dict, game_object_list):
        super().__init__(common_dict, custom_dict, game_object_list)
        self.numbers = common_dict['numbers']
    
    def update(self):
        self
    
    def __str__(self):
        print('Un vieux livre')

class MoveableRockList(GridObject):
    is_editable = True
    def __init__(self,common_dict,custom_dict, game_object_list):
        super().__init__(common_dict, custom_dict, game_object_list)
        self.list = []
        self.id = common_dict['id']
        for object in game_object_list :
            if hasattr(object,'is_rock'):
                self.list.append(object)



    def update(self):
        pass

    def __str__(self):
        pass