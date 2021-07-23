from typing import List

from prompt_toolkit.document import Document


def insert_into_str(str, inserted_str, pos):
    if pos == -1 :
        return str + inserted_str
    else :
        return str[:pos] + inserted_str + str[pos+1:]

def replace_character(str, pos, char):
    if len(char) > 1 :
        raise Exception("le remplacement ne doit concerner qu'un unique char !")
    if len(char) == 0:
        raise Exception("il n'y a pas de char de remplacement !")
    #print( str[:pos-1] + char + str[pos + 1:] )
    return str[:pos] + char + str[pos + 1:]

def get_prefix(prefix_of, str):
    """returns prefix of a string
    
    
    get_prefix(prefix_of    = "Object" , 
               str          = "PromptObjectAndOtherThings"
              )
    
    > "Prompt"
    
    """
    PREFIX = []
    if prefix_of in str :
        k = 0
        while str[k:k + len(prefix_of)] != "Scene":
            PREFIX.append(str[k])
            k += 1
        return "".join(PREFIX)
    else :
        raise Exception(f"{prefix_of} is not inside the given string")

def reset_color(str):
    return str + u" \u001b[0m"

def highlight(str, color):
    dict = {
        "bg red" : u"\u001b[41;1m",
        "bg magenta" : u"\u001b[45;1m",
        "bg blue" : u"\u001b[44;1m",
        #"bg yellow" : u"\033[43;1m",
        "fg magneta" : u"\033[35;1m",
        "fg yellow" : u"\033[33;1m",
        "reversed" : u"\u001b[7m",
        "underline" : u"\u001b[4m"
    }
    return dict[color] + " " + str

def title(str, color) :
    str = " " + str + " "
    str = str.center(50, "=")
    str = highlight(str, color)
    str = reset_color(str)
    print(str)

def H1(str):
    title(str, "bg magenta")

def H2(str):
    title(str, 'bg red')

# https://www.geeksforgeeks.org/python-ways-to-split-strings-on-uppercase-characters/

def split_uppercase(str):
    """Splits a string whenever an Uppercase is encountered
    """
    res_pos = [i for i, e in enumerate(str+'A') if e.isupper()]
    res_list = [str[res_pos[j]:res_pos[j + 1]]
                for j in range(len(res_pos)-1)
               ]
    return res_list

def uppercase_to_underscore(str):
    """ AnUppercaseStringExample => an_uppercase_string_example
    """
    return "_".join(split_uppercase(str)).lower()

def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

def log(window, text: str):
    # on récup la longueur
    max_width = window.window.width - 2
    # on split le texte en fonction des sauts de ligne
    new_lines_raw: List[str] = str(text).split('\n')
    new_lines = []
    # on découpe chaque ligne
    for line in new_lines_raw:
        # si elle dépasse la largeur max
        # côté récursif si jamais la ligne dépsse 3 fois la longueur
        # TODO : avec de l'arithmétique (plus rapide ?)
        while len(line) > max_width:
            new_lines.append(line[0:max_width])
            line = line[max_width:]
        new_lines.append(line)

    new_text: str = "\n".join(new_lines)
    return new_text
    