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