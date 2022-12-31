import json
from typing import Any, Dict, Optional

def save_dictionary(settings: Dict, config_file: str) -> None:
    """Save a dictionary to a JSON file."""
    try:
        with open(config_file, "w") as f:
            json.dump(settings, f)
    except IOError as e:
        print(f"Error saving dictionary: {e}")

def save_variables(config_file: str, **kwargs: Any) -> None:
    """Save variables to a JSON file."""
    try:
        with open(config_file, "w") as f:
            json.dump(kwargs, f)
    except IOError as e:
        print(f"Error saving variables: {e}")

def load_dictionary(config_file: str) -> Dict:
    """Load a dictionary from a JSON file."""
    try:
        with open(config_file, "r") as f:
            return json.load(f)
    except IOError as e:
        print(f"Error loading dictionary: {e}")
        return {}

def load_variables(config_file: str, *, default: Optional[Any]=None) -> Any:
    """Load variables from a JSON file."""
    try:
        with open(config_file, "r") as f:
            settings = json.load(f)
    except IOError as e:
        print(f"Error loading variables: {e}")
        return default
    return settings
