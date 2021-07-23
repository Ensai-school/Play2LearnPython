from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.containers import (
    HSplit,
    VSplit
)
from prompt_toolkit.widgets import (
    Box,
    Frame,
)
from prompt_toolkit.layout.dimension import D, Dimension
from prompt_toolkit.widgets.base import TextArea

class interface_layout():

    def __init__():
        pass

    @staticmethod
    def create(scene_interface, play_area):
        '''Retourne un objet de type layout qui correspond au layout d'un niveau de jeu de la scène souhaitée
        This part of the layout is common to all the level

        Parameters
        ----------
        scene_interface : interface
            The interface where the containers are stored
        play_area : layout
            The layout of the play_area
        '''
        layout_lang = {
            'fr' :
            {
                'code_area' : 'Zone de code',
                'instructions' : 'Instructions du niveau',
                'step' : 'Étape',
                'code_info' : 'Retour code',
                'keybindings' : 'Raccourcis',
                'play_area' : 'Zone de jeu'
            },
            'en':
            {
                'code_area' : 'Code Area',
                'instructions' : 'Level instructions',
                'step' : 'Step',
                'code_info' : 'Code result',
                'keybindings' : 'Key bindings',
                'play_area' : 'Play area'
            }

        }
        root_container = VSplit([
            HSplit([
                Frame(
                    body = scene_interface.textfield,
                    title = layout_lang[scene_interface.language]['code_area']
                 ), 
                Box(
                    body =VSplit(
                        [
                        scene_interface.run_button,
                        scene_interface.kill_button
                        ]),
                    height= 2)], 
                width= Dimension(weight= 1)),
            HSplit([
                Frame(
                    body = scene_interface.instructions,
                    title = layout_lang[scene_interface.language]['instructions'],
                    height= Dimension(weight= 5)),
                VSplit(
                    [
                    Frame(
                        body = scene_interface.progress,
                        title = layout_lang[scene_interface.language]['step'],
                        height= 4, width= 11),
                    Frame(
                        body = scene_interface.code_result,
                        title = layout_lang[scene_interface.language]['code_info'],
                        height= 4),
                    Frame(
                        body = scene_interface.key_bindings_instructions,
                        title = layout_lang[scene_interface.language]['keybindings'],
                        height=4)
                    ]),
                Frame(
                    play_area,
                    title = layout_lang[scene_interface.language]['play_area'],
                    height= Dimension(weight= 5)),
                Box(
                    body = VSplit(
                        [scene_interface.exit_button,
                        scene_interface.next_button]),
                    height= 2)],
                width= Dimension(weight= 1))
        ])
        return(Layout(root_container))