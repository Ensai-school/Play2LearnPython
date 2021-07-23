from custom_level_types.prompt.definition.prompt_object import PromptObject

class PromptFruit(PromptObject):
    is_editable = True
    def __init__(self, common_dict : dict, custom_dict : dict, game_object_list : list):
        super().__init__(common_dict, custom_dict, game_object_list)
        self.type = common_dict['type']

    def update(self):
        """Abstract method
        Each GameObject can be updated every frame
        """
        pass

    def __str__(self):
        return f"Fruit:\nType : {self.type}\n"


class PromptFruitBag(PromptObject):
    is_editable = True
    def __init__(self, common_dict : dict, custom_dict : dict, game_object_list : list):
        super().__init__(common_dict, custom_dict, game_object_list)
        self.list = []
        for object in game_object_list :
            if isinstance(object, PromptFruit):
                self.list.append(object)

    def update(self):
        """Abstract method
        Each GameObject can be updated every frame
        """
        pass

    def __str__(self):
        text = 'Fruit bag\n'
        for fruit in self.list:
            text += f"Fruit:\nType : {fruit.type}\n"
        return text

class PromptFarmer(PromptObject):
    is_editable = True
    def __init__(self, common_dict : dict, custom_dict : dict, game_object_list : list):
        super().__init__(common_dict, custom_dict, game_object_list)
        for object in game_object_list:
            if isinstance(object,PromptFruitBag):
                self.fruit_bag = object
    
    def check_bag(self, list : list):
        #Vérifier que le sac donné correspond à ce qui est attendu sans pour autant etre une copie de l'autre
        #Meme sac mais avec une poire à la 7 places
        #Vérifier que les objects sont bien différents
        for object in list :
            for fruit in self.fruit_bag.list :
                if id(object) == id(fruit):
                    print("Tu as remis les memes pommes dans la nouvelle liste!")
                    return
        if len(list) == len(self.fruit_bag.list):
            for i in range(len(list)):
                if i == 7 and list[i].type != "Pear":
                    print("Tu n'as pas mis la poire!")
                    return
                elif i!=7 and list[i].type != self.fruit_bag.list[i].type:
                    print(f"Le fruit à la {i}ème place n'est pas le bon!")
            print("Bravo! C'est ce que je voulais! Le mot de passe est 3285.")
        else:
            print("Il n'y a pas le bon nombre de fruit!")
    
    def update(self):
        """Abstract method
        Each GameObject can be updated every frame
        """
        pass

    def __str__(self):
        pass