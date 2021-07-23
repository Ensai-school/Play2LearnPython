from custom_level_types.prompt.definition.prompt_object import PromptObject

class PromptBook(PromptObject):

    is_editable = True
    def __init__(self, common_dict : dict, custom_dict : dict, game_object_list : list):
        super().__init__(common_dict, custom_dict, game_object_list)
        self._title = common_dict['title']
        self._pages = common_dict['pages']
        self._summary = common_dict['summary']
        self._publication_year = common_dict['publication_year']

    def __str__(self):
        return f"Title : {self.title}\nSummary : {self.summary}\nPublication year : {self.publication_year}"
    
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
    
    @property
    def publication_year(self):
        return self._publication_year