import traceback
import logging
import sys
#Run the user code

class exec_code():
    """This class runs the user code. It automatically declare variables names of editable GameObject.
    """

    def __init__():
        pass

    @staticmethod
    def run(interface):
        """Static method
        Runs the code
        """
        #Execute le code écrit par l'utilisateur dans le textfield de l'interface
        exec_code.declare_public_var(interface)
        code = interface.textfield.text
        try :
            logging.debug(f"user code : {code}")
            exec(code)
        except Exception as e:
            interface.code_result.text = exec_code.traceback_formatter()
        else :
            interface.code_result.text = "Code exécuté avec succès."
    
    @staticmethod
    def declare_public_var(interface) -> str:
        """Static method
        Declare variable name of editable gameobjects
        """
        #Retourne au format string un code qui assigne à des variables les gamesobjects de la scene qui sont éditables ( is_editable = True)
        #Le nom de variable de chaque gameobject correspond à son id
        for object in interface.scene:
            if object.is_editable:
                globals()[str(object.id)] = object

    @staticmethod
    def traceback_formatter() -> str :
        """format the traceback to display it

        Have to delete some elements, like the exec part of the traceback.

        A typical traceback looks like
        user exception : Traceback (most recent call last):
        File "path\core\exec_user_code.py", line 23, in run
            exec(code)
        File "<string>", line 4, in <module>
        File "<string>", line 2, in test
        NameError: name 'mario' is not defined

        The first 2 elements can be thrown away.
        The 3th to before last and have to be altered to change <string> and <module>

        :return: a traceback for the user
        :rtype: str
        """
        logging.debug(f'user exception : {traceback.format_exc()}')

        traceback_for_user = []
        for traceback_element in traceback.format_exception(*sys.exc_info())[2:-1]:
            altered_traceback = traceback_element
            altered_traceback = altered_traceback.replace('"<string>"', "User code")
            altered_traceback = altered_traceback.replace('<module>', "Text editor")
            traceback_for_user.append(altered_traceback)
        traceback_for_user.append(traceback.format_exception(*sys.exc_info())[-1])
        return "".join(traceback_for_user)