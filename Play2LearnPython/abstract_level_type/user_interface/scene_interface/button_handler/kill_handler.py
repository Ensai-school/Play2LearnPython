from prompt_toolkit.application.current import get_app
from custom_level_types.grid.user_interface.render.grid_render import GridRender
import copy
#Arrete l'execution en cours

class kill_handler():

    def __init__(self,interface):
        """
        Links the button to an interface
        """
        self.interface = interface
    
    def run(self):
        self.interface.stdout_stream.clear()
        self.interface.scene = copy.deepcopy(self.interface.scene_copy)#Reset the scene
        rendered_states = self.interface.render.render(self.interface)
        self.interface.code_result.text = ""
        self.interface.update(rendered_states)