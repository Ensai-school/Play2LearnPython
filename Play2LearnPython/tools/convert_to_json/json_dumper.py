import json


class JsonDumper():
    def __init__(self, dict, output_path) -> None:
        self.dict = dict
        self.output_path = output_path
    def dump(self):
        with open( self.output_path , mode="w", encoding= 'utf-8') as output_file :
            json.dump(self.dict, output_file, skipkeys= True)






