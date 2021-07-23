from core.utils.str_utils import repeat_to_length
import logging
# Type
from typing import Dict

"""Play2LearnPython modules
"""
# Import
from core.utils.import_utils import dynamic_import_dict
# path utils
from core.utils.file_path_utils import get_file_format, get_level_scenes_path
from abstract_level_type.importer.scene_importer import SceneImporter
from abstract_level_type.user_interface.render.render import Render
from importation.parser.parser import Parser
# strategy pattern
# https://refactoring.guru/fr/design-patterns/strategy/python/example


import time




class Import():
    """Manages the Level Import procedure : Imports entire level and returns list[scene]
    """
    def __init__(self, level_folder : str) -> None:
        self.level_folder:str = level_folder
        self.scene_dict:Dict = None
    
        """Strategy Attributes
        """

        self._scene_importer = None
        self._file_parser = None
        # self._renderer = None

        """GameObject classes import
        """


    # Scene Importer

    @property
    def scene_importer(self) -> SceneImporter :
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """
        return self._scene_importer
    @scene_importer.setter
    def scene_importer(self, importer : SceneImporter):
        """
        the Context allows replacing a Strategy object at runtime.
        """
        self._scene_importer = importer


    # File Parser
    # same structure

    @property
    def file_parser(self) -> Parser :
        return self._file_parser
    @file_parser.setter
    def file_parser(self, parser : Parser):
        self._file_parser = parser

    def import_levels(self):
        """main function called, which executes the strategy
        """
        logging.info('Level importation')
        time_start = time.time()
        level = get_level_scenes_path(self.level_folder)
        scene_list = []
        for scene_path in level :
            logging.debug(f"===== scene : {scene_path} =====")
            scene_dict = self.get_scene_dict(file_path = scene_path)
            logging.debug(f'imported scene : {scene_dict}')
            self.choose_importer(scene_dict)
            logging.debug(f'Importer class for scene : {self.choose_importer.__class__}')
            scene = self.get_scene(scene_dict)
            scene_list.append(scene)
            logging.debug(repeat_to_length("=", len(f"===== scene : {scene_path} =====")))

        logging.info(f'{len(scene_list)} loaded in {time.time() - time_start} s')
        return scene_list

    """Choose Strategy
    """

    def choose_importer(self, scene_dict : dict) -> None:
        """Sets the Scene Importer depending on the scene type
        """

        logging.debug("Choosing Importer...")
        start_time = time.time()

        #! scene type prefix
        # type
        type_prefix = scene_dict["scene_type"].lower()
        # Type
        type_class_prefix = scene_dict["scene_type"].capitalize()


        #! imports the right scene importer class
        module_path = f"custom_level_types.{type_prefix}.importer.{type_prefix}_importer" 
        # import
        # dynamic_import(module_path)
        globals().update( dynamic_import_dict(module_path= module_path) )

        #! creates instance of that importer
        # TypeImporter
        class_name = f"{type_class_prefix}Importer"
        # change self.scene_importer
        self.scene_importer = globals()[class_name](
            scene_dict=scene_dict 
            # level_folder=self.level_folder
            )
        logging.debug(f'time elapsed choosing importer : {time.time()-start_time}')


    #? FAIT PAR SCENE INTERFACE
    # def choose_renderer(self, scene_dict : dict) -> None:
    #     pass

    def choose_parser(self, file_path : str) -> None:
        """set the parser depending on the file format of the given file
        NB : force le nom du fichier à être format_parser.py dans le dossier /importation/parser/
        """

        logging.debug("Choosing Parser...")
        start_time = time.time()


        #? OBJECTIF : on souhaite éxecuter
        # pour file_path = path/to/file.format
        # self.parser = FormatParser(file_path = file_path)

        # On regarde le format du fichier
        file_format = get_file_format(file_path)
        # yaml => Yaml
        class_name = f"{file_format.capitalize()}Parser"
        # on recherche dans importation.parser.format_parser
        module_path = f"importation.parser.{file_format}_parser"

        #! on importe les classes du module spécifié

        # H1(module_path)
        # dynamic_import(module_path= module_path)
        globals().update( dynamic_import_dict(module_path) )
        # H1("choose_parser golbals")
        # pprint(globals())
        
        #! on instancie le parser
        self.file_parser = globals()[class_name](file_path = file_path)
        logging.debug(f'time elapsed choosing parser : {time.time()-start_time}')

    """ Intermediate Steps
    """

    def get_scene_dict(self, file_path):
        """charge le fichier et renvoie le dict de la scene associé

            - file_path : localisation du fichier de la scene (01.yaml par exemple)

            - choisit le parser
            - charge avec le parser
            - renvoie le dict

        """
        self.choose_parser(file_path= file_path)
        return self.file_parser.load()
    
    def get_scene(self, scene_dict):
        """renvoie la scene à partir du dict (en appelant la bonne factory associée au type de niveau)
        """
        self.choose_importer(scene_dict = scene_dict)
        scene = self.scene_importer.call_factory()
        return scene
