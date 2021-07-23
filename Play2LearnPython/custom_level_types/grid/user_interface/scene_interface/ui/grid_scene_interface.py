from prompt_toolkit.application import Application
from prompt_toolkit.layout.dimension import D, Dimension
from prompt_toolkit.widgets import (
    Button,
    TextArea,
)


from custom_level_types.grid.user_interface.scene_interface.keybindings.KeyBindings_generator import interface_keybindings
from custom_level_types.grid.user_interface.render.grid_render import GridRender
from abstract_level_type.user_interface.scene_interface.ui.scene_interface import SceneInterface

class GridSceneInterface(SceneInterface):
    """This class creates the application for a specified grid level.
    """

    def __init__(self, scene, language):
        self.feedback = TextArea(read_only= True, width= Dimension(weight= 1))
        super().__init__(scene = scene, language = language, render = GridRender, play_area = self.feedback)
        self.rendered_states = [self.render.SceneToText(self.scene)]
        self.feedback.text = self.rendered_states[0]
        """TextArea : Feedback area. Updates when the run button is triggered.
        Can be a map or a text prompt"""

    def start(self):
        """start method
        
        Run the application

        Note
        ----
        Running an application stops the main event loop.
        """

        """
        KeyBindings
        """
        #Key Bindings de l'interface
        key_bindings = interface_keybindings.create(self)

        """
        Application
        """
        self.application = Application(
            layout= self.layout,
            mouse_support=True,
            full_screen=True,
            key_bindings= key_bindings
        )
        result = self.application.run()
        #Run the application and store the result
        """result is a dict with the following format:
        dict = {
            "completed" : True,
            "want_continue" : True
        }

        -completed : Bool : If the win_condition is met or not
        -want_continue : Bool : If the user want to stay on this level
        """
        
        return( result)
        

    def update(self, rendered_states):
        """update method

        Updates the current rendered_states list with a new one
        Reset the current_step

        Parameter
        ----------
        rendered_states : list
            List of rendered states

        """
        self.rendered_states = rendered_states
        self.current_frame = 0
        self.feedback.text = self.rendered_states[0]
        self.frame_number = len(self.rendered_states)
        self.progress.text = f"{self.current_frame + 1}/{self.frame_number}"
    
    def is_won(self) -> bool:
        return self.scene.is_won()