from abc import ABC, abstractmethod
from abstract_level_type.factory.object_factory import ObjectFactory
import logging
import time

class SceneFactory(ABC):
    """Creates the {scene_type} Scene Object from a scene_dict

    Calls the object factory to create the objects according to the {scene_type}
    """
    # def __init__(self, scene_dict: dict, level_folder : str) -> None:
    def __init__(self, scene_dict: dict) -> None:
        self._scene_dict = scene_dict
        self.game_object_list = []
        # self.level_folder = level_folder
        # self._game_object_factory = ObjectFactory(scene_dict=self.scene_dict, level_folder=self.level_folder)
        self._game_object_factory = ObjectFactory(scene_dict=self.scene_dict)


    # getter 
    @property
    def game_object_factory(self):
        return self._game_object_factory

    # getter
    @property
    def scene_dict(self):
        return self._scene_dict

    def create_scene(self):
        """Crée chaque objet demandé dans le dict et les confie à la scene factory afin de créer un objet Scene
        """

        logging.debug(f"importing scene objects :")
        start_time = time.time() 
        for object_dict in self.scene_dict["game objects"] :
            # {'id': 1, 'position': (2, 5), 'type': 'Personnage'}
            object = self.game_object_factory.create_object(object_dict=object_dict, game_object_list=self.game_object_list)
            self.game_object_list.append(object)
        logging.debug(f"time elapsed to import objects : {time.time() - start_time}")

        #! instancie la classe qui faut : à définir dans la classe concrete
        logging.debug("creating the scene : ")
        start_time = time.time() 
        scene = self.build_scene(
                                scene_dict=self.scene_dict, 
                                game_object_list=self.game_object_list)
        logging.debug(f"time elapsed to create the scene : {time.time() - start_time}")

        return scene

    @abstractmethod
    def build_scene(self, scene_dict, game_object_list):
        """How the scene is supposed to be built, dependent on the scene type
        """
        pass
