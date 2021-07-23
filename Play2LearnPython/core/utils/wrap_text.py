from prompt_toolkit.layout.containers import Window
from prompt_toolkit.document import Document
from prompt_toolkit.formatted_text import to_formatted_text, HTML
from prompt_toolkit import print_formatted_text

def is_surrounded_by_spaces(text, position) -> bool:
    return left_character_is_space(text, position) or right_character_is_space(text, position)

def left_character_is_space(text, position):
    return text[position - 1] == " "

def right_character_is_space(text, position):
    return text[position] == " "


def log_wrap_text(textarea, text: str):
    """
    Wraps the text manually with /n to register the right amount of lines
    It's a fix to the scroll issue : 
    https://github.com/prompt-toolkit/python-prompt-toolkit/pull/693
    https://github.com/CoinAlpha/hummingbot/pull/447
    """

    #! moyen de casser le code : un seul mot très très long
    if textarea.window.render_info is None:
        max_width = 100
    else:
        max_width = textarea.window.render_info.window_width - 1
    new_lines_raw: list[str] = str(text).split('\n')
    new_lines = []
    for line in new_lines_raw:
        while len(line) > max_width:
            cut_position : int = max_width
            if not is_surrounded_by_spaces(line, max_width): 
                while not left_character_is_space(line, cut_position):
                    cut_position -= 1
            new_lines.append(line[0:cut_position])
            line = line[cut_position:]
        new_lines.append(line)

    new_text: str = "\n".join(new_lines)
    textarea.text = new_text


# TODO : HTML aulieu de text
def html_wrap_text(window, html : HTML):
    if window.window.render_info is None:
        max_width = 100
    else:
        max_width = window.window.render_info.window_width - 1
    
    new_lines = []
    current_line_counter = 0
    formatted_line_jump = ('', '\n')

    for formatted_block in html.formatted_text :
        current_line_counter += len(formatted_block[1])

        if current_line_counter > max_width :
            if " " in formatted_block[1] :
                format_class = formatted_block[0]
                words = formatted_block[1].split(" ")

        new_lines.append(formatted_block)
