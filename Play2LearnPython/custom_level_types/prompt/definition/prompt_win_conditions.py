from abstract_level_type.definition.win_conditions import WinConditions


class PromptWinConditions(WinConditions):

    def __init__(self, key : str):
        self.key = key

    def update(self,word):
        self.word = word

    def __bool__(self):
        return(self.key == self.word)
        