import json
from typing import Any, Dict, Optional
import os


def save(config_file: str, **kwargs: Any) -> None:
    directory = os.path.dirname(config_file)
    if directory:
        os.makedirs(directory, exist_ok=True)
    try:
        with open(config_file, "w") as f:
            json.dump(kwargs, f)
    except (FileNotFoundError, PermissionError) as e:
        raise e
    except IOError as e:
        raise IOError(f"Error saving variables: {e}")


def load(
    config_file: str, *, unpack: bool = False, default: Optional[Any] = None
) -> Any:
    try:
        with open(config_file, "r") as f:
            settings = json.load(f)
    except (FileNotFoundError, ValueError) as e:
        return default
    except IOError as e:
        raise IOError(f"Error loading variables: {e}")

    if unpack:
        if isinstance(settings, dict):
            return settings
        else:
            raise ValueError(
                "Cannot unpack variables: JSON file does not contain a dictionary"
            )
    else:
        return settings


def config_file_exists(config_file: str) -> bool:
    return os.path.exists(config_file)
