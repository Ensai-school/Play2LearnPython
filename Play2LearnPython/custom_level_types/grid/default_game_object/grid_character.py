from custom_level_types.grid.definition.grid_object import GridObject

class GridCharacter(GridObject):
    is_editable= True
    game_object_character = "O"
    name = "Character"
    def __init__(self,  common_dict : dict, custom_dict : dict, game_object_list : list) -> None:
        super().__init__(common_dict, custom_dict, game_object_list)
        if self.is_editable :
            self.id = common_dict['id']

    def update(self, game_objects_list):
        pass
    
    """
    METHODES DE DEPLACEMENT
    """


    def go_left(self):
        """déplace le personnage d'un cran vers la gauche
        """
        new_pos = [self.position[0] - 1, self.position[1]]
        self.modify_pos_if_legal(new_pos)

    def go_right(self):
        """déplace le personnage d'un cran vers la droite
        """
        new_pos = [self.position[0] + 1, self.position[1]]
        self.modify_pos_if_legal(new_pos)

    def go_down(self):
        """déplace le personnage d'un cran vers le haut
        """
        new_pos = [self.position[0], self.position[1] + 1]
        self.modify_pos_if_legal(new_pos)

    def go_up(self):
        """déplace le personnage d'un cran vers le bas
        """
        new_pos = [self.position[0], self.position[1] - 1]
        self.modify_pos_if_legal(new_pos)
    
    # on doit vérifier si le move de bouger est légal avant de modifier
    def is_pos_legal(self, new_pos : list) -> bool:
        """retourne True si la position new_pos est légale, False sinon
        """

        """
        PASSER PAR DESSUS UN OBJET
        """
        for object in self.game_object_list :
            # on regarde si on passe par dessus
            if object.position == tuple(new_pos) :
                return False
            # si on ne passe au dessus d'aucun objet
        return True
    
    def modify_pos_if_legal(self, new_pos):
        """modifies character position to new_pos if the position is legal
        """
        if self.is_pos_legal(new_pos) :
            self._position = tuple(new_pos)
            self.notify()
    
    """
    OBSERVER LES AUTRES
    """

    def object_around(self):
        """The character looks around to see if there are other gameobjects
        Returns a dict with bool for each directions
        """
        left = []
        right = []
        up = []
        down = []
        for object in self.game_object_list :
            left.append(tuple(map(lambda x, y: x + y, self.position, (-1,0))) == object.position)
            right.append(tuple(map(lambda x, y: x + y, self.position, (1,0))) == object.position)
            up.append(tuple(map(lambda x, y: x + y, self.position, (0,-1))) == object.position)
            down.append(tuple(map(lambda x, y: x + y, self.position, (0,1))) == object.position)
        return({'left' : any(left),
                'right' : any(right),
                'up' : any(up),
                'down' : any(down)})