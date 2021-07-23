"""
DEPEDENCIES
"""
# prompt toolkit
from prompt_toolkit.application import Application
from prompt_toolkit.document import Document
from prompt_toolkit.layout.containers import HSplit, VSplit,Window
from prompt_toolkit.layout.dimension import D, Dimension
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.widgets import (
    Button,
    TextArea,
)
from prompt_toolkit.widgets.base import Frame
from custom_level_types.prompt.user_interface.render.prompt_render import PromptRender


# general
from abstract_level_type.user_interface.scene_interface.ui.scene_interface import SceneInterface

# custom : Prompt
from custom_level_types.prompt.user_interface.scene_interface.keybindings.KeyBindings_generator import interface_keybindings
from custom_level_types.prompt.user_interface.scene_interface.ui.answer_validator import AnswerValidator
from custom_level_types.prompt.user_interface.render.prompt_render import PromptRender

# utils
# from time import sleep
# import sys
# import copy
from core.utils.wrap_text import log_wrap_text

class PromptSceneInterface(SceneInterface):
    """
    The Interface displayed while playing a PROMPT Scene
    """

    def __init__(self, scene, language):


        #! custom layout
        #? set as an attribute so we can modify it when the user code is run
        self.feedback_area = TextArea(read_only=True,wrap_lines= False)
        #? user input area
        self.user_prompt = TextArea(
            multiline= False,
            read_only=False,
            height= 1,
            scrollbar=False,
            validator= AnswerValidator(answer = scene.win_conditions.key),
            focusable= True,
            focus_on_click= True,
            prompt = "Donnez votre réponse ici :"
            )

        container = HSplit( [ Frame(
                    body = self.feedback_area,
                    title = 'Zone de print'
                 ), Frame(
                    body = self.user_prompt,
                    title = 'Réponse'
                 ) ] )
        """CONTAINER :
        _____________________________
        |                           |
        |                           |
        |            RENDER         |   <= first text area      | 80%
        |                           |
        |                           |
        |___________________________|
        |                           |   <= second text area     | 20%   | + validator 
        |         USER   INPUT      |
        _____________________________
        """
        
        area = container

        super().__init__(scene, language, render = PromptRender , play_area = area)

        # self.width = self.user_prompt.window.width

    def start(self):
        """start method
        
        Run the application

        Note
        ----
        Running an application stops the main event loop.
        """

        #! KEYBINDS

        # interface's keybindings
        key_bindings = interface_keybindings.create(self)

        #! APPLICATION DEFINITION
        
        self.application = Application(
            layout= self.layout,
            mouse_support=True,
            full_screen=True,
            key_bindings= key_bindings
        )


        #! APPLICATION START

        result = self.application.run()

        """result is a dict with the following format:
        dict = {
            "completed" : True,
            "want_continue" : True
        }

        -completed : Bool : If the win_condition is met or not
        -want_continue : Bool : If the user want to stay on this level
        """

        return result
    
    def update(self, render_list):
        """update method

        Updates the current rendered_states list with a new one
        Reset the current_step

        Parameter
        ----------
        rendered_states : list
            List of rendered states

        """
        self.render_list = render_list
        self.current_frame = 0
        log_wrap_text(self.feedback_area,self.render_list[0])
        #self.feedback_area.text = self.render_list[0]
        self.frame_number = len(self.render_list)
        self.progress.text = f"{self.current_frame + 1}/{self.frame_number}"
    
    def is_won(self) -> bool:
        return self.scene.is_won(self.user_prompt.text)
