import importlib


def dynamic_import_dict(module_path : str):
    """returns the dict Globals() needs to import * via the dict.update method
    """
    module = importlib.import_module(module_path)
    if hasattr(module, '__all__') :
        update_dict = {n: getattr(module, n) for n in module.__all__}  
    else :
        update_dict = {k: v for (k, v) in module.__dict__.items() if not k.startswith('_')}
    return update_dict


def dynamic_import(module_path : str, globals_dict : dict):
    """mimics the "from <module>/<package> import *" so it can be used dynamically
    """
    return globals_dict.update( dynamic_import_dict(module_path) )


def dynamic_import_explained(module_path : str, globals_dict : dict):
    """mimics the "from <module>/<package> import *" so it can be used dynamically
    """
    #! OBJECTIVE : from module_path import *
    #? from module_path

    # SOURCE : https://stackoverflow.com/questions/44492803/python-dynamic-import-how-to-import-from-module-name-from-variable/44492879#44492879
    
    # utilisation de importlib plutot que __import__ suggéré par la documentation de python :  https://docs.python.org/2/library/functions.html#__import__

    module = importlib.import_module(module_path)
    # H2("MODULE")
    # print(module)
    # H2("BEFORE")
    # pprint(globals())

    #? import *
    # recreates the behavior of < import * >
    globals_dict.update(
        
        # The real import machinery when doing a * import checks if the module has an __all__ attribute and only imports what is given there - mata [https://stackoverflow.com/users/1350899/mata]
        
        # SOURCE : https://stackoverflow.com/a/44492879/15962450

        #! STEP 1 : looks for __all__ import

        {n: getattr(module, n) for n in module.__all__} if hasattr(module, '__all__') 
        
        #? What is __all__ ?

        #__all__ customizes * in [from <module> import *] and [from <package> import *]
        # - Bob Stein [https://stackoverflow.com/users/673991/bob-stein]

        # it is declared in the __init__.py file for packages
        # or in the module.py for modules
        
        # __all__ = [ 
        #             # class names
        #             'classA', 'classB',

        #             # function names
        #             'fcnA', 'fcnB',
            
        #             # constant names
        #             'ctaA', 'cstB', 'cstC'
        #             ]
        

        # It's a list of public objects of that module, as interpreted by import *. It overrides the default of hiding everything that begins with an underscore. - Jimmy [https://stackoverflow.com/users/4435/jimmy]

        
        #! avoid __all__ when : You're still in early development mode and have no users

        # SOURCE : https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python


        #! STEP 2 if there's no __all__, use the _ convention
        #? > ie : will not import what starts with _

        else

        # By default, Python will export all names that do not start with an _. You certainly could rely on this mechanism.

        # Using the _ convention can be more elegant because it removes the redundancy of naming the names again. But it adds the redundancy for imports (if you have a lot of them)

        # - Aaron Hall [https://stackoverflow.com/users/541136/aaron-hall]
        # hide functions which start with _
        {k: v for (k, v) in module.__dict__.items() if not k.startswith('_')}
    )
    # H2("AFTER")
    # pprint(globals())
