from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style
import os

class LevelSelector():
    def __init__(self, path = "./levels"):
        self.levels_dict = LevelSelector.get_level_list( path)
        self.current_level_scene = 0
    
    def menu(self):
        values_list = [ (key, key) for key in self.levels_dict  ]
        example_style = Style.from_dict({
            'dialog':             'bg:#000000',
            'dialog frame.label': 'bg:#000000 #ffffff',
            'dialog.body':        'bg:#000000 #ffffff',
            'dialog shadow':      'bg:#000000',
            'dialog.title' : 'bg:#00aa00 #ffffff '
        })
        result = radiolist_dialog(
            title="Sélection du niveau",
            text="Choose your level",
            values = values_list,
            style= example_style,
            ok_text= "PLAY",
            cancel_text="QUIT"
        ).run()
        return result
        
    @staticmethod
    def get_level_list(levels_path = "./levels"):
        levels = {}
        if os.path.isdir(levels_path):
            root_path = os.path.normpath(levels_path)
            # os.walk on parcourt la structure à partir du dossier des niveaux
            for root, dirs, files in os.walk(levels_path):
                # si on regarde /levels
                if os.path.normpath(root) == root_path :
                    # on regarde chaque dossier
                    for directory in dirs :
                        # si il possède un fichier 01.yaml à l'intérieur
                        first_scene = "/".join([root, directory, "01.yaml"])
                        if os.path.exists(first_scene) :
                            # c'est un niveau que l'on peut sélectionner
                            levels.update({directory : []})
                    #print(levels)
                for name in files:
                    # on ne regarde que les yaml et json
                    if name.endswith((".yaml", ".json")):
                        # file_path = chemin complet (relatif au projet) vers le yaml
                        file_path = os.path.normpath(os.path.join(root, name))
                        # on l'ajoute au niveau correspondant
                        levels[ LevelSelector.get_folder_position_name(file_path, 1) ].append(file_path)
                        #                                     /levels/my_level/*
                        #                                        0        1     2
            return levels
        else :
            raise Exception("le chemin donné n'est pas un dossier !")
        
    @staticmethod
    def get_folder_position_name(path, position):
        """Retourne le nom du dossier à la profondeur indiquée

        pour path =
        /profondeur0/profondeur1/profondeur3/fichier.ext
        
        get_folder_position_name(path, 1) : profondeur1

        """
        L = os.path.normpath(path).split("\\")
        if len(L) == 1 :
            L = os.path.normpath(path).split("/")
            if len(L) == 1 :
                return path
        return L[position]