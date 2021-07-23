import json
import logging
import time
from importation.parser.parser import Parser

class JsonParser(Parser):
    def load(self):
        """Generates a dict / List from a JSON file
        """
        start_time = time.time()
        with open(self.file_path, mode="r", encoding= 'utf-8') as file :
            imported_dict = json.load(file)
        logging.debug(f'temps parse de {self.file_path} = {time.time()-start_time}')
        return(imported_dict)
