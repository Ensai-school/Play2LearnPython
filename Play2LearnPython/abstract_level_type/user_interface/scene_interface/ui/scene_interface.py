from abc import ABC, abstractmethod
from prompt_toolkit import lexers
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.layout.dimension import D, Dimension
from prompt_toolkit.layout.processors import TabsProcessor
from prompt_toolkit.layout.menus import CompletionsMenu
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style, style
from prompt_toolkit.widgets import (
    Button,
    TextArea,
)
import sys
import copy
from abstract_level_type.user_interface.scene_interface.textfield_engine.auto_complete_constructor import auto_complete
from pygments.lexers.python import PythonLexer
from abstract_level_type.user_interface.scene_interface import button_handler
from abstract_level_type.user_interface.scene_interface.layout.layout_generator import interface_layout
from abstract_level_type.user_interface.scene_interface.textfield_engine.custom_lexer import CustomLexer
from core.stdout_stream import stdoutStream
from core.utils.wrap_text import log_wrap_text

class SceneInterface(ABC):

    def __init__(self, scene, language, render, play_area):
        """__init__ method.

        Parameter
        ----------
        scene : Scene
            The scene to display
        language : str
            The language of the level
        render : Render
            The render engine of the play_Area
        play_area : layout/TextArea
            The layout of the play area
        """
        self.scene = scene
        """Scene : scene object imported from the scene_dict"""

        self.scene_copy = copy.deepcopy(self.scene)
        """A deep copy of the scene to reset the game"""

        self.language = language
        """The language of the scene"""
        
        self.render = render
        """Render of the scene"""

        self.rendered_states = []
        """list : list of the rendered states of the scene.
        Note : There is only one frame at the init."""

        self.current_frame = 0
        """int : Current step of the rendered_states list."""

        self.frame_number = 1
        """int : len of the rendered_states list"""

        self.user_code = None
        """str : Str of the text input of the user.
        Note : user_code is only updated with the run button."""

        self.completer = WordCompleter(auto_complete.ScenetoCompleter(self.scene))
        """wordcompleter : a custom wordcompleter object. Autocomplete the name of the editable gameobjects."""

        self.textfield = TextArea(lexer=PygmentsLexer(PythonLexer),
                completer= self.completer,
                complete_while_typing= True,
                line_numbers= True, scrollbar= False,
                input_processors= [TabsProcessor(tabstop= 4, char1= 1)],
                width= Dimension(weight= 1),
                focusable= True,
                focus_on_click= True)
        """TextArea : Input zone for the user.
        Area to write the code"""
        self.instructions = TextArea(text = '', width= Dimension(weight= 1), lexer= CustomLexer(self.scene))
        """"TextArea : Instructions area. Displays level instructions"""
        log_wrap_text(self.instructions,self.scene.display_text[self.language])

        self.instructions.window.allow_scroll_beyond_bottom.__bool__ = True
        self.progress = TextArea(text = f"{self.current_frame + 1}/{self.frame_number}", width= Dimension(weight= 0.5))
        """"TextArea : A progress bar. Shows the current_step and the max_step with the following format:
        current_step/max_step"""

        self.code_result = TextArea(text = "")
        """TextArea : Feedback area. Display an error if the user code raised an exception.
        Display a message when the code runned successfully
        """

        # TODO : Traduire les indications de Keybindings en fonction de la langue de la scène
        self.key_bindings_instructions = TextArea(text = "Control-left - étape suivante\nControl-right - étape précèdente")
        """TextArea : Instructions area. Shows the different keybindings
        """

        """
        Buttons
        """
        ### HANDLER : Action à réaliser lorsqu'un bouton est activé
        #Handler du bouton exit
        exit_button_handler = button_handler.exit_handler(self)

        #Handler du bouton run
        run_button_handler = button_handler.run_handler(self)

        #Handler du bouton kill
        kill_button_handler = button_handler.kill_handler(self)

        #Handler du bouton next
        next_button_handler = button_handler.next_handler(self)

        #Widgets à placer sur l'interface
        self.exit_button = Button(text = "EXIT", handler=exit_button_handler.run)
        self.run_button = Button(text = "RUN", handler = run_button_handler.run)
        self.kill_button = Button(text = "KILL", handler = kill_button_handler.run)
        self.next_button = Button(text = "NEXT", handler = next_button_handler.run)


        #Layout de l'interface
        self.layout = interface_layout.create(self,play_area)

        self.stdout_stream = stdoutStream() 
        self.stdout_stream.redirect() # Redirect the stdout to prevent the interface from crashing

    @abstractmethod
    def start(self):
        """Runs and displays the interface to the user
        
        Note : 
            The main event loop is stopped while the interface is running
        """
        pass

    @abstractmethod
    def update(self):
        """Updates the play area
        """
        pass

    @abstractmethod
    def is_won(self) -> bool:
        """Return True if the player won the game
        """
        pass