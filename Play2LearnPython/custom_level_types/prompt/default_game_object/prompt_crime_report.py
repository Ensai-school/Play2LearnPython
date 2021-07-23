from custom_level_types.prompt.definition.prompt_object import PromptObject
from custom_level_types.prompt.default_game_object.prompt_suspect import PromptSuspect

class PromptCrimeReport(PromptObject):

    is_editable = True
    def __init__(self, common_dict : dict, custom_dict : dict, game_object_list : list):
        super().__init__(common_dict, custom_dict, game_object_list)
        self._date = common_dict['date']
        self._description = common_dict['description']
        self._suspect_list = []
        for object in game_object_list:
            if isinstance(object,PromptSuspect):
                self._suspect_list.append(object)
    
    """
    GETTER
    """
    @property
    def date(self):
        return self._date
    
    @property
    def description(self):
        return self._description
    
    @property
    def suspect_list(self):
        return self._suspect_list


    def update(self):
        pass

    def __str__(self):
        return f"Crime scene report\nDate : {self.date}\ndescription : {self.description}\n"