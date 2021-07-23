from custom_level_types.prompt.definition.prompt_object import PromptObject
from abstract_level_type.definition.scene import Scene
from custom_level_types.prompt.definition.prompt_object import PromptObject


class PromptScene(Scene):
    def __init__(self, game_object_list : list, display_text : dict , win_conditions) -> None:
        super().__init__(display_text, win_conditions, game_object_list)
        self.win_conditions = win_conditions
        
    def __add__(self, game_object : PromptObject):
        """
        ajoute un gameobject à la scène avec une syntaxe simple :

        scene + gameobject
        """
        self.objects.append(game_object)
    
    # Scene en tant qu'objet itérable
    # itère sur les game objects de la scene
    
    # for object in scene

    def __iter__(self):
        return self.game_object_list.__iter__()
    def __getitem__(self, key):
        return self.game_object_list[key]
    def __setitem__(self, key, item):
        self.game_object_list.__setitem__(key, item)
    def __delitem__(self, key):
        del self.game_object_list[key]
    def __next__(self):
        iter(self.game_object_list).__next__()
    def __len__(self) -> int:
        return len(self.game_object_list)

    
    def __str__(self):
        second ="\n==== game objects ====\n\n"
        third = ""
        for objet in self.game_object_list :
            third += objet.__str__()
        return second + third


    def update(self) -> None:
        pass        
    
    def is_won(self,word) -> bool:
        self.win_conditions.update(word)
        return(bool(self.win_conditions))