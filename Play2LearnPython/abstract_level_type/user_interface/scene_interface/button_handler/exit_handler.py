from prompt_toolkit.application.current import get_app

# Quitter l'application

class exit_handler():

    def __init__(self,interface):
        self.interface = interface
    
    def run(self):
        self.interface.stdout_stream.clear()
        self.interface.stdout_stream.reset()
        self.interface.application.exit(result = {'completed' : self.interface.is_won(), 'want_continue' : False})
