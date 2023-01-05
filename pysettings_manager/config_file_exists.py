import os


def config_file_exists(config_file: str) -> bool:
    return os.path.exists(config_file)
