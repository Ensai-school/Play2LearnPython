from core.utils.str_utils import *

def get_obj_info(obj):
    """Returns Objects information

    - Memory Adress ID
    - Class
    - All Attributes

    """
    adress = hex(id(obj))
    H1("object class")
    print( str( type(obj).__name__ ) )
    H1("object adress")
    print( str(adress) )
    H1("Attributes")
    for attr in dir(obj):
                H2(attr)
                print( "obj.%s = %r" % (attr, getattr(obj, attr)))


def get_class_name(x):
    """Retourne le nom de la classe d'un objet

    x = PromptObjectFactory()
    get_class_name(x)

    > "PromptObjectFactory"

    """
    return type(x).__name__

def get_class_prefix(object, prefix_of):
    """retourne le prefixe de la classe d'un objet
    """
    return get_prefix(prefix_of = prefix_of, str = get_class_name(object) )

def get_sub_classes(mother_class) :
    """ Retourne les sous classes d'une classe mère
    """
    return [classe.__name__ for classe in mother_class.__subclasses__() ]

def prefix_create_object_exec(prefix, class_name, package, python_file, attr_dict, name = None, is_attribute_of = None):
    """[DEPRECATED : do not use it] Create an object with Prefix of a specified class


    Arguments :
        - prefix            : str       ==>     "Prompt"
        - class_name        : str       ==>     "SceneInterface"
        - package           : str       ==>     (1) "path.to.python.file"
        - python_file       : str       ==>     (1) "scene_interface"       | without .py
        - attr_dict         : dict      ==>     (2)
        - name              : str       ==>     None | 'a_name'
        - is_attribute_of   : str       ==>     None | 'targeted_object'

    NOTES :

    (1)
    if python file is located in /path/to/python/file/scene_interface.py

    (2) attr_dict form :
    
    {
        "common" : {
            "common_attr_1" : value1,
            "common_attr_2" : value2,
            "common_attr_3" : value3,
            "common_attr_4" : value4,
        },
        "custom" : {
            "custom_attr_1" : value5,
            "custom_attr_2" : value6,
            "custom_attr_3" : value7,
        }
    }

    """


    #! CLASS NAME

    class_name = f"{prefix}{class_name}"
    # on recherche dans importation.parser.format_parser
    class_name_code = f"{package}.{python_file}." + class_name


    
    #! IMPORT PACKAGE CODE
    

    # import le package où se situe la classe
    # try :
    #    import path.to.package
    # except :
    #    pass
    import_code = f"try :\n\timport {package}\nexcept :\n\tpass"

    # attr_dict
    # 'common' : { 'attr1' : value1, 'attr2' : value2 }
    # 'custom' : { 'custom_attr1' : value3, 'custom_attr2' : value4 }


    
    #! ATTRIBUTES | CONSTRUCTOR PARAMETERS CODE
    

    #? COMMON ATTRIBTUES

    common_attr = ""
    if len(attr_dict["common"]) > 0 :
        for arg in attr_dict['common'] :
            common_attr += f"{arg} = dict['common'][\'{arg}\'] ,"
        # on retire la dernière ,
        common_attr = common_attr[0:len(common_attr) - 1]
    else :
        raise Exception("les common attributes sont obligatoires")


    #? CUSTOM ATTRIBTUES

    custom_attr = ""
    if len(attr_dict["custom"]) > 0 :
        for arg in attr_dict['custom'] :
            # arg = dict['custom']['arg']
            custom_attr += f"{arg} = dict['custom'][\'{arg}\'] ,"
        # on retire la dernière ,
        custom_attr = common_attr[0:len(common_attr) - 1]

    # les common attributes sont obligatoires, ils ne peuvent être vide

    if custom_attr == "" :
        attr = "( " + common_attr + " )"
    else :
        attr = "( " + common_attr + "," + custom_attr + " )"
    

    #! NAMING

    #? the new Object is not attribute of another object (belongs to general environment)
    if is_attribute_of is None :
        # Must have a name to declare object
        if name is None :
            raise Exception("you must specify a name for the new object")
        else :
            name_code = name
    #? the new Object is an attribute of another object
    else :
        # PromptObjectFactory
        # with name = None
        # --> prompt_object_factory
        # with name = "a_certain_name"
        # --> prompt_object_factory_a_certain_name
        name_class_code = uppercase_to_underscore(class_name)
        if name is None :
            name_code = f"{is_attribute_of}.{name_class_code}"
        else :
            name_code = f"{is_attribute_of}.{name_class_code}_{name}"


    #! CODE EXECUTION

    code = f"{name_code} = " + class_name_code + attr
    
    exec(import_code)
    exec(code)
    """
    print(import_code)
    print(code)
    """