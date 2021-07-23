from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.styles import Style

class LanguageSelector():

    def __init__(self):
        self.current_language = 'fr'

    def menu(self):
        values_list = [['fr','Français'],['en','English']]
        example_style = Style.from_dict({
            'dialog':             'bg:#000000',
            'dialog frame.label': 'bg:#000000 #ffffff',
            'dialog.body':        'bg:#000000 #ffffff',
            'dialog shadow':      'bg:#000000',
            'dialog.title' : 'bg:#00aa00 #ffffff '
        })
        result = radiolist_dialog(
            title="Language selection",
            text="Choose your language",
            values = values_list,
            style= example_style,
            ok_text= "PLAY",
            cancel_text="QUIT"
        ).run()
        return result