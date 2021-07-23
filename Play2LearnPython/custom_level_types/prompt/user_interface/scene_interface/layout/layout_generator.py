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
    def create(scene_interface):
        '''Retourne un objet de type layout qui correspond au layout d'un niveau de jeu de la scène souhaitée
        '''
        root_container = VSplit([
            HSplit([
                Frame(
                    body = scene_interface.textfield,
                    title="Zone de code"
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
                    title="Instructions du niveau"),
                VSplit(
                    [
                    Frame(
                        body = scene_interface.progress,
                        title="Étape",
                        height= 4, width= 11),
                    Frame(
                        body= scene_interface.code_result,
                        title="Retour code",
                        height= 4),
                    Frame(
                        body= scene_interface.key_bindings_instructions,
                        title="Raccourcis",
                        height=4)
                    ]),
                Frame(scene_interface.feedback, title = "Zone de jeu"),
                Box(
                    body = VSplit(
                        [scene_interface.exit_button,
                        scene_interface.next_button]),
                    height= 2)],
                width= Dimension(weight= 1))
        ])
        return(Layout(root_container))