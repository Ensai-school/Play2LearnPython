from abstract_level_type.importer.scene_importer import SceneImporter
# TYPE
from custom_level_types.grid.factory.grid_scene_factory import GridSceneFactory





class GridImporter(SceneImporter):
    # def __init__(self, scene_dict, level_folder) -> None:
    def __init__(self, scene_dict) -> None:
        # super().__init__(scene_dict,  level_folder)
        super().__init__(scene_dict)
        # self.scene_factory = GridSceneFactory(scene_dict = scene_dict,  level_folder =  level_folder)
        self.scene_factory = GridSceneFactory(scene_dict = scene_dict)



