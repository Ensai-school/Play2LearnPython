from abc import ABC
from abstract_level_type.factory.scene_factory import SceneFactory

class SceneImporter(ABC):
    """ Takes a level Dict as input and returns a Scene object
    """

    # def __init__(self, scene_dict, level_folder) -> None:
    def __init__(self, scene_dict) -> None:
        self.scene_dict = scene_dict
        # self.level_folder = level_folder
        # SceneFactory(scene_dict, level_folder)
        self._scene_factory : SceneFactory = None

    @property
    def scene_factory(self):
        return self._scene_factory

    @scene_factory.setter
    def scene_factory(self, value):
        self._scene_factory = value

    def call_factory(self):
        if self.scene_factory is not None:
            return self.scene_factory.create_scene()
        else :
            raise Exception("aucune scene factory n'a été assignée")
