# GENERAL
from abstract_level_type.factory.scene_factory import SceneFactory
# LEVEL TYPE
from custom_level_types.prompt.definition.prompt_scene import PromptScene
from custom_level_types.prompt.importer.prompt_win_conditions_importer import PromptWinConditionsImporter

class PromptSceneFactory(SceneFactory):
    """Creates the PromptScene object, by calling the object factory
    """
    # def __init__(self, scene_dict: dict, level_folder) -> None:
    #     super().__init__(scene_dict, level_folder)
    def __init__(self, scene_dict: dict) -> None:
        super().__init__(scene_dict)

    def build_scene(self, scene_dict, game_object_list):
        win_conditions = PromptWinConditionsImporter.create(win_condition_dict= scene_dict["win conditions"], game_object_list= game_object_list)
        scene = PromptScene(game_object_list=game_object_list,
                          display_text=scene_dict["display text"], 
                          win_conditions= win_conditions)
        return scene
