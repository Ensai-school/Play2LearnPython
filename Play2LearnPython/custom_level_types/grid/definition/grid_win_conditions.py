from abstract_level_type.definition.win_conditions import WinConditions

class Condition():
    """ A condition object
    Checks with __bool__ if a GameObject meets a certain condition

    Attribute
    ----------
    game_object_list : list
        The list of all the GameObject in the scene
    id : str
        The id of the Object to check
    var_name : str
        The variable to check
    comparator : str
        For example : "is_equal","is_superior","is_inferior"
    value 
        The value of the variable
    """
    def __init__(self,game_object_list : list,id,var_name : str,comparator : str, value):
        for object in game_object_list:# Cherche le GameObject qui correspond à l'id de la condition
            if hasattr(object,'id'): #Si l'objet a un id
                if object.id == id : # On vérifie que son id correspond à celui de la condition
                    self.object = object # Si c'est le bon GameObject, on l'enregistre et on quitte la boucle de recherche
                    break
        self.var_name = var_name
        self.comparator = comparator # par exemple "is_equal","is_inferior","is_superior"
        self.value = value
    
    def __bool__(self) -> bool:
        '''Vérifie si la condition est vérifiée et retourne un booléen
        '''
        if self.comparator == "is_equal":
            return(getattr(self.object,self.var_name) == self.value)

        elif self.comparator == "is_inferior":
            return(getattr(self.object,self.var_name) < self.value)
        
        elif self.comparator == "is_superior":
            return(getattr(self.object,self.var_name) > self.value)

#L'arbre qui regroupe les conditions entre elles avec des connecteurs comme : ET,OU

class GridWinConditions(WinConditions):

    def __init__(self, list : list,connector : str):
        self.list = list
        self.connector = connector

    def __bool__(self):
        
        if self.connector == "or":
            return(any(self.list))
        elif self.connector == "and":
            return(all(self.list))