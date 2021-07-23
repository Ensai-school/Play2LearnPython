from abstract_level_type.importer.scene_importer import SceneImporter
# TYPE
from custom_level_types.prompt.factory.prompt_scene_factory import PromptSceneFactory





class PromptImporter(SceneImporter):
    """
    Calls the right scene factory
    """
    # def __init__(self, scene_dict, level_folder) -> None:
    #     super().__init__(scene_dict,  level_folder)
    #     self.scene_factory = PromptSceneFactory(scene_dict = scene_dict,  level_folder =  level_folder)
    def __init__(self, scene_dict) -> None:
        super().__init__(scene_dict)
        self.scene_factory = PromptSceneFactory(scene_dict = scene_dict)
    



