from abc import ABC
from importation.import_objects_definition import ImportObjectsDefinition
import logging
import time


class ObjectFactory(ABC):
    """Creates a game object from an object_dict
    """

    # def __init__(self, scene_dict, level_folder):
    def __init__(self, scene_dict):
        """
        type_location dict form :

        {
            "type" : "custom_level_types/grid/default_game_object"
        }

        package : "custom_level_types.grid.default_game_object"
        ou
        package : "levels.pacman"
        file : "setup"
        "/levels/pacman/setup.py"

        """
        self._prefix = None
        self._package = None
        self._type_location_dict = None
        #? type location dict form

        # self.level_folder = level_folder
        self.scene_dict = scene_dict
        # self.object_importer = ImportObjectsDefinition(level_folder_path= self.level_folder, scene_dict = self.scene_dict)
        self.object_importer = ImportObjectsDefinition(scene_dict = self.scene_dict)


    def create_object(self, object_dict: dict, game_object_list: list):
        """Creates a GridObject

        Attributes
        -----------
        Object_dict : dict
            A dict that describes the GridObject to create
        GameObjectList : list
            The list where all GameObjects are stored
        """
        #! IMPORT GAME OBJECTS INTO ENVIRONMENT
        globals().update( self.import_objects() )
        logging.debug('Importing a '+ object_dict['type'])
        #! RETURN GAME OBJECT
        return(globals()[object_dict['type']](object_dict['common_dict'], object_dict['custom_dict'], game_object_list))
        #      |           Class             |              attributes

    def import_objects(self):
        return self.object_importer.import_objects()
