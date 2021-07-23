from abc import ABC, abstractmethod

class Render(ABC):
    """
    Abstract class of the rendered
    Each Render object can take an interface and render the frames
    Those frames are then pushed to the interface
    """
    def __init__():
        pass

    # @abstractmethod
    # def SceneToText(scene):
    #     pass
    
    @abstractmethod
    def render(interface) -> list:
        """
        Take the interface and render the frames.
        """
        pass