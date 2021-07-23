from abstract_level_type.definition.scene import Scene
from custom_level_types.grid.definition.grid_object import GridObject


class GridScene(Scene):
    def __init__(self, dimension : tuple, game_object_list : list, display_text : dict , win_conditions) -> None:
        super().__init__(display_text, win_conditions, game_object_list)
        self.dimension = dimension
        self.game_states = []
        # ajout de l'état inital
        self.update()
        """
        un gamestate est un dictionnaire de la façon suivante
        {

            id_objet_1 :
                {
                    attribut1 :
                    attribut2 :
                    attribut3 :
                    ...
                }
            id_objet_2 :
                {
                    _position : (x,y)
                    id : n
                    observers = [scene]
                }
            id_objet_3 :


        }

        il faut donc pour acceder à une valeur d'un gamestate faire
        gamestate[id_objet]["attribut"]
        
        et donc
        scene.game_states[numero_frame][id_objet]["attribut"]

        """

        # on inscrit la scene en tant qu'observateur de ses objets
        for game_object in self.game_object_list :
            #print(game_object)
            game_object.register(self)

    def add_game_state(self, render : str):
        self.game_states.append(render)
    def __add__(self, game_object : GridObject):
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
    def __len__(self):
        return len(self.game_object_list)

    
    def __str__(self):
        first = f"===== SCENE DESC ====\n\nscene de dimension :\nx: {self.dimension[0]}\ny : {self.dimension[0]}\n"
        second ="\n==== game objects ====\n\n"
        third = ""
        for objet in self.game_object_list :
            third += objet.__str__()
        return first + second + third


    # TODO : méthode qui calcule et ajoute une gamestate en mémoire
    # dans le cadre particulier du programme
    # on n'a pas besoin de la valeur en elle même
    # juste de la notification du changement
    # def update(self, subject):
    # devient donc
    def update(self):
        # dès qu'une valeur est changée
        # on capture un snapshot du gamestate de l'entièreté du jeu
        #Rajouter le moteur de jeu ici? Vérifier que 2 gameobjects ne se superposent pas ou qu'un trigger doit s'activer
        gamestate = {}
        for game_object in self :
            # .copy() pour copier les valeurs aulieu de référencer l'objet
            obj_dict = { game_object : game_object.__dict__.copy() }
            gamestate.update(obj_dict)
        
        self.game_states.append( gamestate )

    def select(self, object_id):
        for k in range( len(self) ):
            if self[k].id == object_id :
                if self[k].is_editable :
                    return self[k]
                else :
                    raise Exception("cet objet ne peut être modifié !")
        raise Exception("id non trouvé !")

    def su_select(self, object_id):
        for k in range( len(self) ):
            if self[k].id == object_id :
                return self[k]
        raise Exception("id non trouvé !")
    
    def is_won(self):
        return(bool(self.win_conditions))
    