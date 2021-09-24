import os

# Путь до пакета
PACKAGE_PATH = os.getcwd()
# Путь до родительской папки пакета
_path_to_parent_ = os.path.dirname(PACKAGE_PATH)
# Путь до файла конфигурации
CONFIG_PATH = os.path.join(_path_to_parent_, "configuration")


def set_config_path(path):
    """
    Установка конфигурационной папки приложения
    :param path: путь к конфигурационной папке
    :return: None
    """
    global CONFIG_PATH
    CONFIG_PATH = path



