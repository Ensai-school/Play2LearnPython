# GENERAL
from abstract_level_type.factory.scene_factory import SceneFactory
# LEVEL TYPE
from custom_level_types.grid.factory.grid_object_factory import GridObjectFactory
from custom_level_types.grid.definition.grid_scene import GridScene
from custom_level_types.grid.importer.grid_win_conditions_importer import GridWinConditionsImporter

class GridSceneFactory(SceneFactory):
    # def __init__(self, scene_dict: dict, level_folder) -> None:
    def __init__(self, scene_dict: dict) -> None:
        # super().__init__(scene_dict, level_folder)
        super().__init__(scene_dict)
        # self._game_object_factory = GridObjectFactory(scene_dict, level_folder)
        self._game_object_factory = GridObjectFactory(scene_dict)


    def build_scene(self, scene_dict, game_object_list):
        win_conditions = GridWinConditionsImporter.create(win_condition_dict= scene_dict["win conditions"], game_object_list= game_object_list)
        scene = GridScene(dimension=scene_dict["dimension"], 
                          game_object_list=game_object_list,
                          display_text=scene_dict["display text"], 
                          win_conditions= win_conditions)
        return scene
