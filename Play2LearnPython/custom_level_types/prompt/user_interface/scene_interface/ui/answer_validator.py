from prompt_toolkit.document import Document
from prompt_toolkit.validation import ValidationError, Validator

class AnswerValidator(Validator):
    """
    validation system for user input
    makes sure he has the right answer before moving on

    __ ATTRIBUTES __

    answer : str
    """
    
    def __init__(self, answer) -> None:
        super().__init__()
        self.answer = answer
    
    def validate(self, document: Document) -> None:
        text = document.text
        if not text :
            raise ValidationError(message="I am not evil enough to choose an empty answer as a solution !")
        elif text and not text.lower() == self.answer.lower() :
            raise ValidationError(message="wrong answer")
        elif text and text.lower() == self.answer.lower() :
            # alors on a a gagné
            self.is_won()