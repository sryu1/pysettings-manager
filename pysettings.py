import json
from typing import Any, Dict, Optional
import os


def save_dictionary(settings: Dict, config_file: str) -> None:
    """Save a dictionary to a JSON file."""
    try:
        with open(config_file, "w") as f:
            json.dump(settings, f)
    except FileNotFoundError:
        print(f"Error saving dictionary: {config_file} does not exist")
    except PermissionError:
        print(f"Error saving dictionary: permission denied for {config_file}")
    except IOError as e:
        print(f"Error saving dictionary: {e}")


def save_variables(config_file: str, **kwargs: Any) -> None:
    """Save variables to a JSON file."""
    try:
        with open(config_file, "w") as f:
            json.dump(kwargs, f)
    except FileNotFoundError:
        print(f"Error saving variables: {config_file} does not exist")
    except PermissionError:
        print(f"Error saving variables: permission denied for {config_file}")
    except IOError as e:
        print(f"Error saving variables: {e}")


def load_dictionary(config_file: str, default: Optional[Dict] = {}) -> Dict:
    """Load a dictionary from a JSON file."""
    try:
        with open(config_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error loading dictionary: {config_file} does not exist")
        return default
    except ValueError:
        print(f"Error loading dictionary: {config_file} is not a valid JSON file")
        return default
    except IOError as e:
        print(f"Error loading dictionary: {e}")
        return default


def load_variables(config_file: str, *, default: Optional[Any] = None) -> Any:
    """Load variables from a JSON file."""
    try:
        with open(config_file, "r") as f:
            settings = json.load(f)
    except FileNotFoundError:
        print(f"Error loading variables: {config_file} does not exist")
        return default
    except ValueError:
        print(f"Error loading variables: {config_file} is not a valid JSON file")
        return default
    except IOError as e:
        print(f"Error loading variables: {e}")
        return default
    return settings


def config_file_exists(config_file: str) -> bool:
    """Check whether a configuration file exists."""
    return os.path.exists(config_file)
