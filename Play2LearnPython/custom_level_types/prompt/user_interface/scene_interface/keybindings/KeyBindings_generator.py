import logging
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.application import get_app

class interface_keybindings():

    def __init__():
        pass

    @staticmethod
    def create(interface):
        '''Retourne un objet de type KeyBindings qui peut etre utiliser dans une interface pour définir les raccourcis clavier
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
        
        #Focus la zone de code
        @kb.add('c-left')
        def move_right(event):
            interface.layout.focus(interface.textfield)

        #Focus la zone de CTF
        @kb.add('c-right')
        def move_left(event):
            interface.layout.focus(interface.user_prompt)

        return(kb)