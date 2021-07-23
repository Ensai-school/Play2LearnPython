from custom_level_types.prompt.definition.prompt_win_conditions import PromptWinConditions
from abstract_level_type.importer.win_conditions_importer import WinConditionsImporter

# TODO

class PromptWinConditionsImporter(WinConditionsImporter):
    
    def __init__():
        pass

    @staticmethod
    def create(win_condition_dict : dict, game_object_list : list):
        '''Retourne l'object win_condition lié à une scène 
        '''
        return(PromptWinConditions(win_condition_dict['key']))

