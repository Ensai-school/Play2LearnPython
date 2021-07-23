from abc import abstractmethod
from core.observer_pattern.observer import Observer


class Scene(Observer):

    def __init__(self,display_text : dict, win_conditions, game_object_list : list):
        self.display_text = display_text
        self.win_conditions = win_conditions
        self.game_object_list = game_object_list

    @abstractmethod
    def update():
        """
        The scene is an observer and this method is called when one of the subjet notified the scene
        """
        pass

    @abstractmethod
    def is_won() -> bool:
        """
        Returns a bool : True if the scene is won
        """
        pass
    # TODO : iterable scene -> borrow from GridScene