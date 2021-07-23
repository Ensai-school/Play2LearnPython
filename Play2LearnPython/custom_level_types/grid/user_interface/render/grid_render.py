from core.utils.str_utils import replace_character

class GridRender():
    
    def __init__(self) -> None:
        pass

    @staticmethod
    def SceneToText( scene ) -> str:
        """Fait le rendu de l'état actuel d'une scène et le renvoie sous forme de string

        """
        # on initialise les lignes :
        # on met du vide (espace) sur toute la longueur de la grille ( dimension suivant x)
        # il y a (dimension sur y) lignes
        Lignes = [ " " * scene.dimension[0] for i in range(scene.dimension[1]) ]
        # on vient modifier le caractère de la position de l'objet
        # en remplaçant l'espace par le caractère associé à la classe
        # du GameObject
        for object in scene.game_object_list :
            x = object.position[0]
            y = object.position[1]
            Lignes[y] = replace_character(str = Lignes[y], 
                                        pos = x, 
                                        char = object.game_object_character)
        return "\n".join(Lignes)

    @staticmethod
    def render(interface):
        """Fait le rendu de toutes les gamestates d'une scène et retourne sous forme de liste de "matrice"

        format :

        render = [

            frame 0,
            frame 1,
            frame 2

        ]
            = list[str]


        frame = "ligne 1 \n ligne 2 \n ... \n ligne 3"

        format d'une frame pendant
        étape intermédiaire (avant join) : 

        frame = [   "      x    ",
                    "           ",
                    "      x    ",
                    "  o        ",
                ]
              = list[str]

        """
        # on initialise les lignes :
        # on met du vide (espace) sur toute la longueur de la grille ( dimension suivant x)
        # il y a (dimension sur y) lignes
        #print(len(scene.game_states))
        render = [ [ " " * interface.scene.dimension[0] for i in range(interface.scene.dimension[1]) ] for k in range( len(interface.scene.game_states) ) ]
        #          |            axe x        |          axe y                   |               temps                |
        # on fait le rendu de chaque game state une à une

        #pprint(render)

        final_render = []

        for state in interface.scene.game_states :
            # on parcourt tous les objets d'une game state ( par leur id )
            #print("====== STATE ========")
            #pprint(state)

            for object in state :
                # on récupère leur position
                x = state[object]["_position"][0]
                y = state[object]["_position"][1]
                # on modifie la ligne où doit se situer l'objet
                # (ie on fixe y)
                #               numero de la frame             ligne
                #             = position de la state
                # et on place le caractère associé au type de game_object à la position x (de la ligne y)
                render[ interface.scene.game_states.index(state) ][ y ] = replace_character(str = render[ interface.scene.game_states.index(state) ][ y ], pos = x, char = object.game_object_character)
                #                 ligne                                                             ligne                              colonne        can select even non editable objects
                #print(render)
            final_state_render = ""
            final_state_render = "\n".join(render[ interface.scene.game_states.index(state) ])
            final_render.append(final_state_render)
            #print("======= FIN STATE ======")
        return final_render