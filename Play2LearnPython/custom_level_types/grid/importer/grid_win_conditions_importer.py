from custom_level_types.grid.definition.grid_win_conditions import *
from abstract_level_type.importer.win_conditions_importer import WinConditionsImporter

class GridWinConditionsImporter(WinConditionsImporter):

    def __init__():
        pass

    @staticmethod
    def create(win_condition_dict : dict, game_object_list : list):
        '''
        Retourne l'object win_condition lié à une scène de type Grid
        '''
        if 'comparator' not in win_condition_dict.keys():
            connector = list(win_condition_dict.keys())[0]
            condition_list = [GridWinConditionsImporter.create(dict1,game_object_list) for dict1 in win_condition_dict[connector]]
            return(GridWinConditions(list = condition_list,connector = connector))
        else:
            return(Condition(game_object_list = game_object_list,
                            id = win_condition_dict['id'],
                            var_name = win_condition_dict['var_name'],
                            comparator = win_condition_dict['comparator'],
                            value = win_condition_dict['value']))

