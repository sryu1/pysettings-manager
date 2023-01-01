import json
from typing import Any, Dict, Optional
import os


def save(config_file: str, **kwargs: Any) -> None:
    """Save variables to a JSON file.

    Parameters:
        config_file: The file to save the variables to.
        **kwargs: The variables to save.

    Raises:
        FileNotFoundError: If the directory for `config_file` does not exist.
        PermissionError: If the file cannot be opened for writing due to insufficient permissions.
        IOError: If there is an error writing to the file.
    """
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
    """Load variables from a JSON file.

    Parameters:
    config_file (str): The file to load the variables from.
    unpack (bool, optional): If `True`, the variables in the JSON file will be unpacked and returned as individual variables. If `False`, the entire contents of the JSON file will be returned as a dictionary. Defaults to `False`.
    default (Any, optional): The value to return if the file does not exist or is not a valid JSON file. Defaults to `None`.

    Returns:
    Any: The variables stored in the JSON file, either as a dictionary or as individual variables, depending on the value of `unpack`. Returns `default` if the file does not exist or is not a valid JSON file.

    Raises:
    IOError: If there is an error reading from the file.
    ValueError: If `unpack` is `True` and the JSON file does not contain a dictionary.

    Example:
    >>> # Unpack variables
    >>> foo, bar = load("settings.json", unpack=True)
    >>>
    >>> # Return dictionary
    >>> settings = load("settings.json")
    """
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
    """Check whether a configuration file exists.

    Parameters:
        config_file: The file to check for existence.

    Returns:
        `True` if the file exists, `False` otherwise.
    """
    return os.path.exists(config_file)
