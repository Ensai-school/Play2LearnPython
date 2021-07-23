from abc import ABC, abstractmethod, abstractstaticmethod
from abstract_level_type.definition.win_conditions import WinConditions

class WinConditionsImporter(ABC):
    """
    Abstract class for the WinConditionsImporter,
    all win conditions importer must have an import method that returns a WinConditions object
    """
    @abstractstaticmethod
    def create(win_condition_dict : dict, game_object_list : list):
        pass