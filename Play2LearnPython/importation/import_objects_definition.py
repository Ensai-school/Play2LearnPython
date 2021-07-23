from core.utils.file_path_utils import get_module_path_list, path_to_module, path_to_package
import os.path
from posixpath import normpath
from core.utils.import_utils import dynamic_import, dynamic_import_dict
from core.store import Store

class ImportObjectsDefinition():
    """Import the the object classes needed in a scene

    Imports /level/setup.py classes
    and
    Imports /custom_level_type/default/ classes
    """
    # def __init__(self, level_folder_path, scene_dict) -> None:
    def __init__(self, scene_dict) -> None:
        # self.level_folder : str = level_folder_path
        self.level_folder : str = Store().level_folder_path
        self.scene_dict : dict = scene_dict

    def import_objects(self):
        """ returns the dict that has to be used to update globals


        __ USE CASE EXAMPLE __

        globals().update( ImportObjectsDefinition(scene_dict).import_objects() )
                           ________________________ __________________________
                                                   v
                                        the result : globals_dict_update
        """
        globals_dict_update = {}
        globals_dict_update.update(self.import_default())
        globals_dict_update.update(self.import_setup())
        return globals_dict_update

    
    def import_default(self):
        if os.path.isdir(self.level_folder):
            # we reach the level folder
            # if it exists
            globals_update_dict = {}
            # we look at the scene type to create the game objects
            scene_type = self.scene_dict["scene_type"].lower()
            # we get the paths of the default game objects python files
            object_module_list = get_module_path_list(f"./custom_level_types/{scene_type}/default_game_object/")
            for object_path in object_module_list :
                # we convert from a path to a module path
                module = path_to_module(object_path)
                # we get the dict of the import
                # and we append it to the final update dict
                globals_update_dict.update(dynamic_import_dict(module))
            # dict à update dans le globals
            return globals_update_dict

    def import_setup(self) -> globals:
        """retourne le dictionnaire pour update globals() des modules importés

        utilisation : globals().update( ImportObjectsDefintion(level_path).import_setup() )
        
        """
        if os.path.isdir(self.level_folder):
            # we reach the level folder
            path = os.path.normpath(self.level_folder)
            # look for setup.py 
            path += os.path.normpath("/setup.py")
            # if it exists
            if os.path.exists(path) :
                # we import it
                module = path_to_package(self.level_folder) + ".setup"
                # dict à update dans le globals
                return dynamic_import_dict(module)

