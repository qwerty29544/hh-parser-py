import environment as envir
import json


class parser_configuration:
    def __init__(self, path_to_config):
        # TODO: обработка разных исключений по работе и ветвления различных модов работы
        with open(path_to_config, "r") as json_config:
            self.configuration = json.load(json_config)

    def get_config(self):
        return self.configuration



