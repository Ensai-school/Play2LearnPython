- [Import Errors](#import-errors)
  - ['NoneType' object is not subscriptable](#nonetype-object-is-not-subscriptable)
    - [Vérify the scene YAML](#vérify-the-scene-yaml)
      - [the short answer](#the-short-answer)
      - [the long answer](#the-long-answer)


# Import Errors

## 'NoneType' object is not subscriptable


### Vérify the scene YAML


#### the short answer
Be careful not creating an empty object in the YAML

```yaml
game objects :

  # new game object
  -
    type : OldBook
    common_dict :
      [...]
    custom_dict : 
  -
# ^
# THAT DASH IS CAUSING THE PROBLEM
```

#### the long answer
here is an example :




```python
[DEBUG] 2021-07-19 15:12:52,968 - Choosing Importer...
[DEBUG] 2021-07-19 15:12:52,968 - time elapsed choosing importer : 0.0
[DEBUG] 2021-07-19 15:12:52,968 - importing scene objects :
[INFO] 2021-07-19 15:12:52,982 - Importing aOldBook
[ERROR] 2021-07-19 15:12:52,982 - Ohoh ... Something unexpected happend ...
```

```python
[ERROR] 2021-07-19 15:12:52,982 - 'NoneType' object is not subscriptable
```

We could think that an attribute of the last object of `aOldBook` is cuasing some edge cases breaking the code


```python
Traceback (most recent call last):
[...]
File "C:\Users\alexa\Documents\GitHub\Play2LearnPython\Play2LearnPython\abstract_level_type\factory\scene_factory.py", line 38, in create_scene

    object = self.game_object_factory.create_object(object_dict=object_dict, game_object_list=self.game_object_list)

File "C:\Users\alexa\Documents\GitHub\Play2LearnPython\Play2LearnPython\abstract_level_type\factory\object_factory.py", line 50, in create_object
    
    logging.info('Importing a' + object_dict['type'])

TypeError: 'NoneType' object is not subscriptable
```

by taking a closer look at the debug and especially the scene dict meant to be imported :


```PYTHON
[DEBUG] 2021 - 07 - 19 15: 12: 52, 952 - imported scene: {
    'scene_type': 'prompt',
    'dimension': (60, 30),
    'display text': {
        'fr': 'En arrivant devant la porte, vous apercevez un petit livre posé par terre.\n\nUne voix résonne alors à nouveau dans le temple :\n “Pour ouvrir la porte, il faudra calculer la somme de tous les chiffres présents dans ce livre !” Vous pouvez observer la liste des nombres dans le livre avec :\n old_book.numbers\n \n Bonne chance!\n ',
        'en': 'TODO'
    },
    'win conditions': {
        'key': '10234267'
    },
    'game objects': [{
        'type': 'OldBook',
        'common_dict': {
            'id': 'old_book',
            'numbers': [1123, 3453634, 32432534543, 21345645632, 123435346563, 2343453564578, 768645674534, 32453564563545, 234345645634, 2342345]
        },
        'custom_dict': None
    }, 
    None ]
#    ^
#    |
}
```
it's actually the parser which interprets 
```yaml 
    (...)

    - 
```

as
```python
[ (...)  ,None]
#           ^
#           |
```

