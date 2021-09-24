from environment import *
from HHparser import hh_data_loader
from parser_configuration import parser_configuration
import os
import pandas


def app():
    parser_cfg = parser_configuration(path_to_config=os.path.join(CONFIG_PATH, 'config.json'))
    data_loader = hh_data_loader(parser_cfg.get_config())
    set = data_loader.get_dataset()
    set.to_csv(path_or_buf="test.csv", sep="\t", encoding="UTF-16")


if __name__ == "__main__":
    app()