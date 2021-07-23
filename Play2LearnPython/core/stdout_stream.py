import sys

class stdoutStream:
    """
    Transfer the stdout into a list
    """
    def __init__(self):
        self.data = []

    def write(self, s) -> None:
        self.data.append(s)

    def redirect(self) -> None:
        """
        Redirect the stdout to the stdoutstream list
        """
        sys.stdout = self

    def reset(self) -> None:
        """
        Reset the old stdout
        """
        sys.stdout = sys.__stdout__

    def clear(self) -> None:
        """
        Clear the stdout history
        """
        self.data = []