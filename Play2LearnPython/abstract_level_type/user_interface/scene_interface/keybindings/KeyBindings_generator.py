from prompt_toolkit.key_binding import KeyBindings

class interface_keybindings():

    def __init__():
        pass

    @staticmethod
    def create(interface):
        '''Retourne un objet de type KeyBindings qui peut etre utilisé dans une interface pour définir les raccourcis clavier
        '''
        kb = KeyBindings()

        #Tabulation et indentation
        @kb.add('tab')
        def tab(event):
            index = interface.textfield.document.cursor_position
            position = interface.textfield.document.translate_index_to_position( index)
            interface.textfield.text = interface.textfield.text[:index] + '  ' + interface.textfield.text[index:]
            if position[0] != 0:
                interface.textfield.buffer.cursor_down(position[0])
            interface.textfield.buffer.cursor_right(position[1] + 2)
        
        #Déplacement chargement
        @kb.add('pageup')
        def move_right(event):
            if interface.current_step + 1 < interface.max_step:
                interface.current_step +=1
                #interface.feedback.text = str(interface.current_step)
                interface.feedback.text = interface.rendered_states[interface.current_step]
                interface.progress.text = f"{interface.current_step + 1}/{interface.max_step}"

        @kb.add('pagedown')
        def move_left(event):
            if interface.current_step - 1 >= 0:
                interface.current_step -=1
                #interface.feedback.text = str(interface.current_step)
                interface.feedback.text = interface.rendered_states[interface.current_step]
                interface.progress.text = f"{interface.current_step + 1}/{interface.max_step}"
        
        return(kb)