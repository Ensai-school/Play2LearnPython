import logging
import os
from typing import List

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



def get_levels_and_scenes(levels_path = "./levels/"):
    """Returns a dict with all valid levels and their scenes' path

    ==== EXAMPLE ====


    folder structure : (cf README.md)

    📦levels
    ┣ 📂my_level
    ┃ ┣ 📜01.yaml
    ┃ ┗ 📜README.md        <= not mandatory but recommended
    ┣ 📂pacman
    ┃ ┣ 📜01.yaml
    ┃ ┣ 📜02.yaml
    ┃ ┣ 📜03.yaml
    ┃ ┗ 📜README.md
    ┣ 📂test               <= won't be detected
    ┣ 📂no 01 - starts with 02
    ┗ ┣ 📜02.yaml          <= won't be detected 

    returns :

    {'my_level': ['levels\\my_level\\01.yaml'], 
        'pacman': ['levels\\pacman\\01.yaml', 
                'levels\\pacman\\02.yaml', 
                'levels\\pacman\\03.yaml'
                ]
    }
    """
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
                    levels[ get_folder_position_name(file_path, 1) ].append(file_path)
                    #                                     /levels/my_level/*
                    #                                        0        1     2
                    #       pour avoir  "my_level" en clé
        return levels
    else :
        raise Exception("le chemin donné n'est pas un dossier !")

def get_level_scenes_path(level_path:str)-> List :
    """returns all scene paths inside a level folder in a list
    """
    if os.path.isdir(level_path) :
        scenes = []
        for root, dirs, files in os.walk(level_path) :
            for name in files :
                if name.endswith((".yaml", ".json")):
                    # file_path = chemin complet (relatif au projet) vers le yaml
                    file_path = os.path.normpath(os.path.join(level_path, name))
                    logging.debug(f'Add file {file_path} to scene list')
                    scenes.append(file_path)
        return scenes
    else :
        raise Exception("le chemin donné n'est pas un dossier !")

def get_file_format(file_path:str):
    """ returns the file extension of a file from its path


    example :

    /path/to/file.extension => extension
    """
    return os.path.splitext(file_path)[1][1::]

def path_to_package(path : str) -> str :
    """converts a file path to package format
    /!\ does not work with .py files modules, only packages

    /path/to/package/is/cool

    path.to.package.is.cool
    """
    work_path = os.path.normpath(path)
    if "/" in work_path :
        work_path_list = work_path.split("/")
    elif "\\" in work_path :
        work_path_list = work_path.split("\\")
    else :
        return work_path
    if work_path_list[0] == "" :
        return ".".join(work_path_list[1::])
    else :
        return ".".join(work_path_list)

def path_to_module(path : str) -> str :
    """converts module file path to module path format

    /path/to/my/cool/module.py

    path.to.my.cool.module
    """
    work_path = os.path.splitext(path)[0]
    return path_to_package(work_path)

def get_module_path_list(folder):
    """returns all modules (as path) available in a package
    """
    list = []
    if os.path.isdir(folder):
        root_path = os.path.normpath(folder)
        # os.walk on parcourt la structure à partir du dossier "folder"
        for root, dirs, files in os.walk(folder):
            for name in files:
                # on ne regarde que les py
                if name.endswith((".py")):
                    # file_path = chemin complet (relatif au projet) vers le py
                    file_path = os.path.normpath(os.path.join(root, name))
                    # on l'ajoute au niveau correspondant
                    list.append(file_path)
        return list
