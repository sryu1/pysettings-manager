import json


def save_dictionary(settings, settings_file):
    """Save a dictionary to a JSON file."""
    try:
        with open(settings_file, "w") as f:
            json.dump(settings, f)
    except IOError as e:
        print(f"Error saving dictionary: {e}")


def save_variables(settings_file, **kwargs):
    """Save variables to a JSON file."""
    try:
        with open(settings_file, "w") as f:
            json.dump(kwargs, f)
    except IOError as e:
        print(f"Error saving variables: {e}")


def load_dictionary(settings_file):
    """Load a dictionary from a JSON file."""
    try:
        with open(settings_file, "r") as f:
            return json.load(f)
    except IOError as e:
        print(f"Error loading dictionary: {e}")
        return {}


def load_variables(settings_file, *, default=None):
    """Load variables from a JSON file."""
    try:
        with open(settings_file, "r") as f:
            settings = json.load(f)
    except IOError as e:
        print(f"Error loading variables: {e}")
        return default
    return settings
