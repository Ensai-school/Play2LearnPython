#Add gameobject name from the scene to the WorldCompleter of the interface

class auto_complete():

    def __init__(self) -> None:
        pass

    @staticmethod
    def ScenetoCompleter(scene) -> list:
        '''Scene to Completer
        Récupère les id des gameobjects qui ont la valeur is_editable == True
        Retourne la liste de ces id
        '''
        dict = []
        for object in scene:
            if object.is_editable:
                dict.append(object.id)
        return(dict)