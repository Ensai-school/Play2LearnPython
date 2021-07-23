from PIL import Image



def import_map(image_name : str, game_object_dict : dict):
    """Transforms a PNG file into a YMAL GameObject dict

    Attributes
    ----------
    image_name : str
        The name of the image to transform
    game_object_dict : dict
        A dict that associates pixel color with a type of gameobject
    """
    fichier_texte = open("export/" + image_name + ".txt","w+")
    image = Image.open("map/" + image_name + ".png")
    (largeur,hauteur) = image.size
    for i in range(largeur):
        for j in range(hauteur):
            pixel = image.getpixel((i,j))
            if pixel in game_object_dict:
                common_dict = "common_dict : \n"
                common_dict += "      position : !!python/tuple [{},{}]\n".format(i,j)
                for key in game_object_dict[pixel]['common_dict'] :
                    common_dict += f"      {str(key)} : {str(game_object_dict[pixel]['common_dict'][key])}\n"
                custom_dict = "custom_dict : \n"
                for key in game_object_dict[pixel]['custom_dict'] :
                    if type(game_object_dict[pixel]['custom_dict'][key]) is str :
                        value = f"'{str(game_object_dict[pixel]['custom_dict'][key])}'"
                    else :
                        value = str(game_object_dict[pixel]['custom_dict'][key])
                    custom_dict += f"      {str(key)} : {value}\n"
                fichier_texte.write(f"  # new game object\n  -\n    type : {str(game_object_dict[pixel]['type'])}\n    {common_dict}    {custom_dict}")
    fichier_texte.close()

import_map("aventure_02",{(0,0,0) : {
    'type' : "GridObstacle",
    'common_dict' : {

                    },
    'custom_dict' : {
                    'game_object_character' : '-' 
                    }
                            },
                (0,51,255) : {
    'type' : "GridCharacter",
    'common_dict' : {

                    },
    'custom_dict' : {
                    'game_object_character' : 'X',
                    'is_rock' : True,
                    'is_editable' : False
                    }
                            },
                (0,0,255) : {
    'type' : "GridObstacle",
    'common_dict' : {

                    },
    'custom_dict' : {
                    'game_object_character' : 'A' 
                    }
                            },
                (255,0,0) : {
    'type' : "GridObstacle",
    'common_dict' : {

                    },
    'custom_dict' : {
                    'game_object_character' : '|' 
                    }
                            }
                }
            )

import_map("07",{(0,0,0) : {
    'type' : "GridObstacle",
    'common_dict' : {

                    },
    'custom_dict' : {
                    'game_object_character' : '-' 
                    }
                            },
                (0,0,255) : {
    'type' : "GridObstacle",
    'common_dict' : {

                    },
    'custom_dict' : {
                    'game_object_character' : 'A' 
                    }
                            },
                (255,0,0) : {
    'type' : "GridObstacle",
    'common_dict' : {

                    },
    'custom_dict' : {
                    'game_object_character' : '|' 
                    }
                            }
                }
            )