from custom_level_types.prompt.definition.prompt_object import PromptObject

class PromptBookShelf(PromptObject):

    def __init__(self, common_dict : dict, custom_dict : dict, game_object_list : list):
        super().__init__(common_dict, custom_dict, game_object_list)
        self._title = common_dict['title']
        self._book_list = common_dict['book_list']
        self._books = []
        for object in game_object_list:
            if object.id in self._book_list:
                self._books.append(object)

    def __str__(self):
        return f"Title : {self.title}\nSummary : {self.summary}\n"
    
    def update(self):
        pass

    """
    GETTER
    """
    @property
    def title(self):
        return self._title
    
    @property
    def pages(self):
        return self._pages
    
    @property
    def summary(self):
        return self._summary