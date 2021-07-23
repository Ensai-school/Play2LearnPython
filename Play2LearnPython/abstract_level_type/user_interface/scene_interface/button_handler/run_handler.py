import threading
import time
from custom_level_types.grid.user_interface.render.grid_render import GridRender
from core.exec_user_code import exec_code
from prompt_toolkit.shortcuts import yes_no_dialog
import copy

#Récupère le code de l'utilisateur pour l'executer et affiche le nouveau feedback

class run_handler():

    def __init__(self,interface):
        """
        Links a button to an interface
        """
        self.interface = interface

    def run(self):
        self.interface.scene = copy.deepcopy(self.interface.scene_copy) #Reset the scene
        self.interface.stdout_stream.clear() # Clear the stdout
        code_execution = threading.Thread(target= exec_code.run, args=[self.interface], daemon= True) # Create a thread to run the user code
        code_execution.start() # Run the thread
        #time.sleep(2)
        code_execution.join(timeout = 2) # Join the threads
        if code_execution.is_alive():
            self.interface.code_result.text = "Runtime error"
            del code_execution
        else:
            rendered_states = self.interface.render.render(self.interface) # Update the rendered_states of the GameObjects
            self.interface.update(rendered_states)
        if self.interface.is_won():#Checks if the scene is won
            self.interface.code_result.text = "Niveau complété!" #Displays a win message to the user
