
# C - Implementing a new Scene Parser

## C.1 - How scenes are structured

A scene is a dict that can be imported :

here is the dict structure

```python
{

  # needed for ALL level types

  "scene_type" : str,
  # defines the prefix of the level type used for the scene

  "game objects" : [ game_obj_dict_1, game_obj_dict_2, game_obj_dict_3, ... ],
  # game objects are dict that are stored in a list
  # located at the key 'game objects'

  "display text" :  {
                      "fr" : "texte à afficher",
                      "en" : "text to display",
                      "ch" : "i don't speak chinese",
                      ...
                    },

  "win conditions" : 

}
```


## C.2 How GameObjects are structured

A game objecty is also a dict that will be converted into an object later on to be imported into the environment

here is the dict structure

```python
{

  # nom de la classe à instancier
  "type" : "ClassName",


  "common_dict" : {
                    "attribut1" : value,
                    "attribut2" : value,
                    "attribut3" : value
                  }

  "custom_dict" : {
                    "attribut4" : value,
                    "attribut5" : value,
                  }

}
```

## C.3 the Parser structure

![](/out/parser_structure_uml.png)

implementing a new parser is about implementing the `load()` method which parses the `file_path` attribute, (file path as an input, dit as an output)

here's an example of the JSON parser :

```python
import json
from importation.parser.parser import Parser

class JsonParser(Parser):
    def load(self):
        """Generates a dict / List from a JSON file
        """
        with open(self.file_path, mode="r", encoding= 'utf-8') as file :
            imported_dict = json.load(file)
        return(imported_dict)
```