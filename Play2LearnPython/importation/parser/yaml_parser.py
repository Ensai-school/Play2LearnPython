from importation.parser.parser import Parser
import yaml
import time
import logging

from yaml import CLoader as Loader

class YamlParser(Parser):
    def __init__(self, file_path):
        super().__init__(file_path)
    def load(self):
        """Generates a dict / List from a YAML file
        """
        start_time = time.time()
        with open(self.file_path, mode="r", encoding= 'utf-8') as file :
            imported_dict = yaml.load(file, Loader=Loader)
            #pprint(scene_dict)
        logging.debug(f'temps parse de {self.file_path} = {time.time()-start_time}')
        return(imported_dict)



