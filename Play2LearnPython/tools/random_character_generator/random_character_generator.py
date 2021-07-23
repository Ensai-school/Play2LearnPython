"""
This function generates random characters that all have valid alibi.
You can then add the murderer with a fake alibi in the list.
"""
import random

def random_character_generator(first_name_list : list, name_list : list, hair_color_list : list, room_dict : dict):
    """
    All alibi will be true -> in a room open at the time and the alibi will cover the hour of the murder
    """
    pass
    text = "# new innocent PromptSuspect\n-\n  type : PromptSuspect\n  common_dict :\n"
    first_name = random.choice(first_name_list)
    name = random.choice(name_list)
    age = random.randint(20,70)
    height = random.randint(60,90)
    hair_color = random.choice(hair_color_list)
    alibi_room_id = random.choice(list(room_dict.keys()))
    text += f"    id : \"{first_name.lower()}_{name.lower()}\"\n"
    text += f"    name : \"{first_name} {name}\"\n"
    text += f"    age : {age}\n"
    text += f"    height : \"1m{height}\"\n"
    text += f"    hair_color : \"{hair_color}\"\n"
    text += f"    alibi_room_id : \"{alibi_room_id}\"\n"
    #TODO : Custom description
    description = "TODO"
    text += f"    description : \"{description}\"\n"
    #TODO : Custom alibi
    alibi = "TODO"
    text += f"    alibi : \"{alibi}\"\n"
    text += "  custom_dict :\n\n"
    return(text)

def random_character_list(first_name_list : list, name_list : list, hair_color_list : list, room_dict : dict,number : int, file_name : str):
    """
    Generate a number of random character
    """
    fichier_texte = open("export/" + file_name + ".txt","w+")
    text = ""
    for i in range(number):
        text += random_character_generator(first_name_list, name_list, hair_color_list, room_dict)
    fichier_texte.write(text)
    fichier_texte.close()

##Example

first_name_list = ['Jake','Rosa','Terry','Amy','Charles','Gina','Raymond','Michael','Norm','Haley','Alex','Luke','Claire','Cameron','Lily','Jay']

name_list = ['Peralta','Doaz','Jeffords','Santiago','Boyle','Linetti','Holt','Hitchcock','Scully','Dunphy','Pritchett','Tucker']

hair_color_list = ['Blond','Brun','Roux','Noir']

murder_time = (23,56)

room_dict = {
            'hotel': [[7,0],[24,0]],
            'hall' : [[7,0],[24,0]],
            'swimming_pool1' : [[9,0],[24,0]],
            'movie_theater' : [[0,0],[24,0]] 
            }

random_character_list(first_name_list,name_list,hair_color_list,room_dict,number = 20,file_name= 'test')