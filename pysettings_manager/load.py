import json
from typing import Any, Optional


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
