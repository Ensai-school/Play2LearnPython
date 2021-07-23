from core.utils.import_utils import dynamic_import_dict
import logging
from user_interface.selector.level_selector import LevelSelector
from user_interface.selector.lang_selector import LanguageSelector
from user_interface.selector import *
from importation.import_master import Import
# from custom_level_types.scene_type.user_interface.scene_interface.ui.scene_type_scene_interface import SceneTypeSceneInterface
import sys
from core.store import Store

class Manager():
    """Manages the different interfaces and importation calls
    """

    def __init__(self):
        
        #! chooses language
        #? Stored in Singleton
        # for use several layers bellow : ImportObjectDefinition
        # TODO : language has to be LEVEL dependant | should be chosen at each level
        # The manager should raise the level selector first and then the language selector
        Store().lang = LanguageSelector().menu()
        

        #! Initializes the current scene
        self.current_scene_number = 0
        

    def run(self):
        """Runs the manager
        """
        if self.current_scene_number == 0 : 
            """ If there is no level started, the manager asks the user the level he wants to play
            """
            logging.info('Level selection')
            self.level = LevelSelector().menu()
            if self.level is None:
                logging.info('There is no level to load')
                quit()
            Store().level_folder_path = "./levels/" + self.level
            importer = Import( Store().level_folder_path ) # The level is then imported
            self.scene_list = importer.import_levels()

        current_scene = self.scene_list[self.current_scene_number]

        #! Gets Prefix (Capitalized)
        type = current_scene.__class__.__name__.replace("Scene",'')
        
        #! import {level_type} Interface
        module_type = type.lower()
        module = f"custom_level_types.{module_type}.user_interface.scene_interface.ui.{module_type}_scene_interface"
        globals().update( dynamic_import_dict(module) )
        
        #! creates instance of the right importer
        interface = globals()[type + "SceneInterface"](current_scene,Store().lang)
        
        result = interface.start()

        if result["want_continue"] is False:                        # If the user wants to stop
            self.current_scene_number = 0                               # Reset the current scene
            self.run()                                                  # Restart the selection menu
        elif result["completed"] is True :                          # If the user completed the scene
            self.current_scene_number += 1                              # Keep track of the progress
            if self.current_scene_number < len(self.scene_list):        # If it is not the last scene of the level
                self.run()                                                  # Run the menu 
            else:                                                       #  If it is the last scene of the level
                self.current_scene_number = 0                               # Reset the current scene
                self.run()                                                  # Run the menu