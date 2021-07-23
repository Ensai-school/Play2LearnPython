from prompt_toolkit.application.current import get_app

# Quitter l'application

class next_handler():

    def __init__(self,interface):
        self.interface = interface
    
    def run(self):
        if self.interface.is_won():
            self.interface.stdout_stream.reset()
            self.interface.application.exit(result = {'completed' : True, 'want_continue' : True})