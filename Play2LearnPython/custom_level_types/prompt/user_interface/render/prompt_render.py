from typing import final
from core.utils.str_utils import replace_character
from pprint import pprint
from abstract_level_type.user_interface.scene_interface.ui.scene_interface import SceneInterface

class PromptRender():
    
    def __init__(self) -> None:
        pass

    @staticmethod
    def render(interface : SceneInterface) -> list:
        """
        Retourne le standard output

        c'est à l'utilisateur de faire print
        """
        # TODO : calculer le nombre de lignes de la frame render pour ne pas avoir de scroll bar
        # non prioritaire
        
        stdout_list = interface.stdout_stream.data
        str = "".join(stdout_list)

        return [str]
    