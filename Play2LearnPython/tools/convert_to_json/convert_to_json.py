from tools.convert_to_json.json_dumper import JsonDumper
from core.utils.import_utils import dynamic_import_dict
from core.utils.file_path_utils import get_file_format
import os

class ConvertToJson():
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.ext_table = {
            "yml" : "Yaml",
            "yaml" : "Yaml",
            "json" : "Json",
            "csv" : "Csv"
        }
    def convert_file( self ):
        ext = get_file_format( self.file_path )
        class_name = f"{self.ext_table[ext]}Parser"
        module = f"importation.parser.{self.ext_table[ext].lower()}_parser"
        globals().update( dynamic_import_dict(module) )
        dict = globals()[ class_name ]( file_path = self.file_path ).load()
        output_path = os.path.splitext(self.file_path)[0] + ".json"
        JsonDumper(dict, output_path).dump()
