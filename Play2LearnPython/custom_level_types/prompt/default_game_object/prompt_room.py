from custom_level_types.prompt.definition.prompt_object import PromptObject

class PromptRoom(PromptObject):

    is_editable = True
    def __init__(self, common_dict : dict, custom_dict : dict, game_object_list : list):
        super().__init__(common_dict, custom_dict, game_object_list)
        self._name = common_dict['name']
        self._info = common_dict['info']
        self._opening_hours = common_dict['opening_hours']
    
    """
    GETTER
    """
    @property
    def name(self):
        return self._name
    
    @property
    def info(self):
        return self._info
    
    @property
    def opening_hours(self):
        return self._opening_hours
    
    def update(self):
        pass

    def __str__(self):
        return f"Room\nName : {self.name}\nInfo : {self.info}\nOpening hours : {self.opening_hours}"