- [B - Creating Levels](#b---creating-levels)
  - [B.1 - Level architecture](#b1---level-architecture)
  - [B.2 - Creating Custom GameObjects](#b2---creating-custom-gameobjects)
  - [B.3 - Creating a scene](#b3---creating-a-scene)
    - [B.3.1 - Using YAML](#b31---using-yaml)
      - [YAML TO PYTHON TYPE SYNTAX](#yaml-to-python-type-syntax)
      - [define Scene Type](#define-scene-type)
      - [Define GameObjects](#define-gameobjects)
      - [Define Win Condition](#define-win-condition)
        - [Grid Win Conditions](#grid-win-conditions)
        - [Prompt Win Conditions](#prompt-win-conditions)
      - [entire YAML example](#entire-yaml-example)
        - [grid](#grid)
        - [prompt](#prompt)
  - [B.2](#b2)
    - [B.2.1 [to be changed] Objects containing others](#b21-to-be-changed-objects-containing-others)
- [Looking for errors](#looking-for-errors)
  - [the log](#the-log)
- [Known Limitations](#known-limitations)
  - [win condition](#win-condition)
  - [object importer](#object-importer)
    - [objects containing others](#objects-containing-others)



if you want more details on how the game engine works :
please take a look at [this documentation](./about_the_program.md)


# B - Creating Levels

## B.1 - Level architecture

levels have to be put inside the `levels` folder (located in root folder)


```
📦Play2LearnPython
 ┣ 📂.git
 ┣ 📂.vscode
 ┣ 📂abstract_level_type
 ┣ 📂core
 ┣ 📂custom_level_types
 ┣ 📂documentation
 ┣ 📂importation
 =============================
 ┣ 📂levels     <= THAT ONE
 =============================
 ┣ 📂user_interface
 ┣ 📜.gitignore
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┗ 📜__main__.py
```



A level must contain `01.yaml` and `setup.py` to be detected
> ie : must contain at least a "first scene"


```
📦levels
 ┣ 📂my_level
 ┃ ┣ 📜setup.py         <= mandatory (even if it is empty)
 ┃ ┣ 📜01.yaml
 ┃ ┗ 📜README.md        <= not mandatory but recommended
 ┣ 📂pacman
 ┃ ┣ 📜setup.py         <= create custom Game Objects
 ┃ ┣ 📜01.yaml
 ┃ ┣ 📜02.yaml
 ┃ ┣ 📜03.yaml
 ┃ ┗ 📜README.md
 ┣ 📂no setup           <= won't be detected
 ┃ ┣ 📜01.yaml
 ┣ 📂no 01 - starts with 02
 ┗ ┣ 📜02.yaml          <= won't be detected    
```



## B.2 - Creating Custom GameObjects

In order to create a custom game object, you need to define it in the `setup.py` inside 

```
 ┣ 📂levels
 ┃ ┗ 📂pacman
 ┃ ┃ ┣ 📜01.yaml
 ┃ ┃ ┣ 📜README.md
 ====================
 ┃ ┃ ┗ 📜setup.py    <==
 ====================
```

> from scratch

```python
from custom_level_types.my_level_type.definition.my_level_type_object
```

> from an already defined default object

```python
from custom_level_types.my_level_type.default_game_object.my_level_type_certain_object
```

> 

```python
class MyCustomGameObject(MyLevelTypeObject):

    def __init__() -> None :

```

- the `common_dict` stores the mandatory values for a certain class of game objects.

- the `custom_dict` creates attributes that are specific **to one specific object**


Creating custom objects inside `setup.py` allows the level creator to have objects with a very specific behavior (custom methods and attributes) created specifically a scene



```python
class OldBook(PromptObject):
    is_editable = True
    def __init__(self,common_dict,custom_dict, game_object_list):
        super().__init__(common_dict, custom_dict, game_object_list)
        self.numbers = common_dict['numbers']
    
    def update(self):
        self
    
    def __str__(self):
        print('Un vieux livre')
```


## B.3 - Creating a scene


### B.3.1 - Using YAML


#### YAML TO PYTHON TYPE SYNTAX

[Learn More about PyYaml with the official documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)

| Python                                   | Yaml                       |
|------------------------------------------|----------------------------|
| None                                     | null                       |
| True                                     | true                       |
| False                                    | false                      |
| int                                      | 3                          |
| float                                    | 3.1415                     |
| dict                                     | {key1: 13, key2: 5}        |
| list => ['LITE', 'RES_ACID', 'SUS_DEXT'] | [LITE, RES_ACID, SUS_DEXT] |
| string                                   | !!str "my string"          |


`PYTHON SPECIFIC`

| Python                                   | Yaml                           |
|------------------------------------------|--------------------------------|
| tupple => (1,2)                          | !!python/tuple [1,2]           |
| unicode str                              | !!python/unicode               |
| complex number                           | !!python/complex               |


`custom modules`

| Python                                   | Yaml                           |
|------------------------------------------|--------------------------------|
| module . name                            | !!python/name:module.name      |
| package.module                           | !!python/module:package.module |
| module.cls instance                      | !!python/object:module.cls     |


#### define Scene Type

```yaml
# will be the prefix
scene_type : "myleveltype"
```

#### Define GameObjects

```yaml
# Define your Scene Game Objects
game objects :
  # new game object
  -                     # - needed to create new dict
    type : Personnage               # GameObject class you want to summon
    common_dict :                   # mandatory GO class attributes fields
        attribut1 : null
        attribut2 : null
    custom_dict :                   # create custom GO attributes
        attribut3 : null            # for that specific object
        attribut4 : null            # not thought out for that GO class

  # new game object
  -                     # - needed to create new dict
    type : Obstacle
    common_dict :
        attribut1 : null
        attribut2 : null
    custom_dict :
        attribut3 : null

```

#### Define Win Condition

> determined by the WinConditionImporter of the desired level type

```yaml
win conditions :

```

In order to complete a level, the end user / player has to verify the win condition when the program stops.

the way a win condition has to e implemented depends on the level type

here are the ways to define a win condition with the 2 already included level types :

##### Grid Win Conditions

Grid Win Conditions need to point to a certain game object's property, and check whether its value is greater than, less than or equal to another value

```yaml
win conditions :
  cond1 :                       # name of the condition
  id : Pirate                   # which gameobject ?? | id attribute
  var_name : position           # the attribute we look at
  comparator : "is_equal"       # which operation
  value : !!python/tuple [31,8] # which value
```

##### Prompt Win Conditions

Prompt level type are `CTF like` level types, you need to enter a flag / password in order to complete the level

the win condition is defined in the yaml as follows :


```yaml
win conditions :
  key : 'Damien Cébizar'
```



#### entire YAML example


##### grid

```yaml
scene_type : "grid"

# Grid dimensions
dimension : !!python/tuple [50,25]

display text: 
  fr : !!str "Notions abordées dans ce niveau :\n
\n
- Boucle while :\n
    Les boucles permettent de réaliser des itérations \n
-  Déplacement de personnage \n
- Comparaison\n
\n
Objets utilisables dans ce niveau :\n
- Magicien :\n
    Personnage du niveau, il est représenté par le caractère O.\n

Méthodes disponibles pour le niveau :\n
-déplacement :\n
        go_left()\n
        go_right()\n
        go_down()\n
        go_up()\n
\n
Les personnages se déplacent de la manière suivante : \n
   Magicien.go_left()\n

Variables disponibles pour le niveau:\n
objectif\n

Magicien.objectif retourne un tuple de la forme suivante :\n
Magicien.objectif =(3,4\n
\n
Le magicien doit alors se déplacer aux coordonnées de l'objectif.\n
\n
-- Objectif du niveau  --\n

Un magicien cherche un artefact invisible. Il connait uniquement sa position. Le magicien doit trouver l'artefact."
  en : !!str "-- The goal of this level is to show the abilities of the app and the GRID levels --\n
\n
NOT DONE YET"

win conditions :
  cond1 :
  id : Magicien
  var_name : position
  comparator : "is_equal"
  value : !!python/tuple [3,20]

game objects :
  # new game object
  -
    type : GridCharacter
    common_dict :
        id : Magicien
        position : !!python/tuple [28,16]
    custom_dict :
        objectif : !!python/tuple [3,20]

    # new game object
  -
    type : GridObstacle
    common_dict : 
      position : !!python/tuple [0,0]
    custom_dict : 
  # new game object
  -
    type : GridObstacle
    common_dict : 
      position : !!python/tuple [0,1]
    custom_dict : 
[...]
```

##### prompt

```yaml
scene_type : "prompt"

# Grid dimensions
dimension : !!python/tuple [60,30]

display text: 
  fr : !!str "En arrivant devant la porte, vous apercevez un petit livre posé par terre.\n

Une voix résonne alors à nouveau dans le temple :\n
“Pour ouvrir la porte, il faudra calculer la somme de tous les chiffres présents dans ce livre !”
Vous pouvez observer la liste des nombres dans le livre avec :\n
old_book.numbers\n
\n
Bonne chance!\n
\n
Lorsque vous aurez trouvé le bon résultat, écrivez le dans la barre en bas et relancez le code.
"

  en : !!str "TODO"

# C1 et C2 et ( C3 ou C4 ou [C6 et C7] )
win conditions :
  key : '35977228772131'

game objects :

  # new game object
  -
    type : OldBook
    common_dict :
      id : old_book
      numbers : [1123,3453634,32432534543,21345645632,123435346563,2343453564578,768645674534,32453564563545,234345645634,2342345]
    custom_dict : 
```

## B.2 

### B.2.1 [to be changed] Objects containing others

- `id`

- constructor
  - adding to a list, objects which have the right `id`


# Looking for errors

## the log

there are 2 levels of logging :
DEBUG [max details]
INFO

they will help you understand where some erros might be when implementing your own custom level type

it uses the `logging` package.

```
📦Play2LearnPython
 ┣ 📂log
 ┃ ┣ 📜debug.log
 ┃ ┗ 📜info.log
```

```cmd
[DEBUG] 2021-07-16 12:26:31,227 - ===== scene : levels/demo_grid/04.yaml =====
[DEBUG] 2021-07-16 12:26:31,228 - Choosing Parser...
[DEBUG] 2021-07-16 12:26:31,228 - time elapsed choosing parser : 5.7697296142578125e-05
[DEBUG] 2021-07-16 12:26:31,527 - temps parse de levels/demo_grid/04.yaml = 0.2992229461669922
[DEBUG] 2021-07-16 12:26:31,529 - Choosing Importer...
[DEBUG] 2021-07-16 12:26:31,529 - time elapsed choosing importer : 0.00033926963806152344
[DEBUG] 2021-07-16 12:26:31,529 - Importer class for scene : <class 'method'>
[DEBUG] 2021-07-16 12:26:31,529 - Choosing Importer...
[DEBUG] 2021-07-16 12:26:31,530 - time elapsed choosing importer : 8.654594421386719e-05
[DEBUG] 2021-07-16 12:26:31,530 - importing scene objects :
[DEBUG] 2021-07-16 12:26:31,685 - time elapsed to import objects : 0.15555930137634277
[DEBUG] 2021-07-16 12:26:31,686 - creating the scene : 
[DEBUG] 2021-07-16 12:26:31,686 - time elapsed to create the scene : 0.0005691051483154297
[DEBUG] 2021-07-16 12:26:31,687 - ============================================
```


# Known Limitations

## win condition

The win condition is verified at the end of the user script which means that if the win condition is verified while the loop si still running, it won't end the level.

**THE LOOP HAS TO END ON WIN CONDITION**

verifying win conditions while a loop is running is something that could be implemented in future versions of Play2LearnPython, but isn't implemented in the current version.


## object importer

### objects containing others

the current implementation needs a trick / hack to create objects that contain other objects.
For instance : a bookshelf, which contains books.
Right now, in order to create such an object

> a **rework** of the import system has to be implemented