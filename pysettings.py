import json


def save_dictionary(settings_file, settings):
    with open(settings_file, "w") as f:
        json.dump(settings, f)


def save_variables(settings_file, **kwargs):
    with open(settings_file, "w") as f:
        json.dump(kwargs, f)


def load_dictionary(settings_file):
    with open(settings_file, "r") as f:
        settings = json.load(f)


def load_variables(settings_file):
    # Load the settings from the JSON file
    with open(settings_file, "r") as f:
        settings = json.load(f)
    locals().update()

    return settings
