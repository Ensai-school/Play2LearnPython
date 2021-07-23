from prompt_toolkit.lexers import Lexer
from prompt_toolkit.styles.named_colors import NAMED_COLORS

class CustomLexer(Lexer):
    def __init__(self,scene):
        """
        Stores the name of all the GameObject,Method,Variable of the scene in lists
        """
        self.objects_name = []
        self.methods_name = []
        for object in scene:
            if hasattr(object,'id'):
                self.objects_name.append(object.id)
                for method in dir(object):
                    if method not in self.methods_name:
                        self.methods_name.append(method + '()')

    def lex_document(self, document):
        """
        Lexer method -> takes a line number and return the color instructions for the line
        """
        colors = list(sorted(NAMED_COLORS, key=NAMED_COLORS.get))

        def get_line(lineno):
            line_style = []
            for word in document.lines[lineno].split():
                if word in self.objects_name:
                    line_style.append(('#adff2f',word))
                elif word in self.methods_name:
                    line_style.append(('#60FDFE', word))
                else :
                    line_style.append(('#ffffff',word))
                line_style.append(('#ffffff',' '))
            return line_style

        return get_line

