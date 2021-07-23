class MetaSingleton(type):
    __instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in MetaSingleton.__instances:
            # print(f'Creation d\'une nouvelle instance de {cls}')
            MetaSingleton.__instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        # print(MetaSingleton.__instances)
        return MetaSingleton.__instances[cls]
    
class Store(metaclass=MetaSingleton):
    def __init__(self) -> None:
        # Paramètres de niveau
        self.level_folder_path : str = None
        self.lang : str = None
        # Autres
