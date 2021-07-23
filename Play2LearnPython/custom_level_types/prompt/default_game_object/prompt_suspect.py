from custom_level_types.prompt.definition.prompt_object import PromptObject

class PromptSuspect(PromptObject):

    is_editable = True
    def __init__(self, common_dict : dict, custom_dict : dict, game_object_list : list):
        super().__init__(common_dict, custom_dict, game_object_list)
        self._name = common_dict['name']
        self._age = common_dict['age']
        self._height = common_dict['height']
        self._alibi = common_dict['alibi']
        self._hair_color = common_dict['hair_color']
        self._description = common_dict['description']
        room_id = common_dict['alibi_room_id']
        for object in game_object_list :
            if object.id == room_id :
                self._alibi_room = object
    
    """
    GETTER
    """
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @property
    def height(self):
        return self._height
    
    @property
    def alibi(self):
        return self._alibi
    
    @property
    def hair_color(self):
        return self._hair_color
    
    @property
    def description(self):
        return self._description
    
    @property
    def alibi_room(self):
        return self._alibi_room
    
    def update(self):
        pass
    
    def __str__(self):
        return f"Suspect\nName : {self.name}\nAge : {self.age}\nHeight : {self.height}\nDescription : {self.description}\nAlibi :{self.alibi}\n"