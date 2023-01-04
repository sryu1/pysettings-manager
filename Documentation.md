# `save` function

Save variables to a JSON file.

## Parameters

- `config_file` (str): The file to save the variables to.
- `**kwargs` (Any): The variables to save. Any number of keyword arguments can be passed to this function, and they will all be saved to the JSON file as a dictionary.

## Raises

- `FileNotFoundError`: If the directory for `config_file` does not exist.
- `PermissionError`: If the file cannot be opened for writing due to insufficient permissions.
- `IOError`: If there is an error writing to the file.

## Example

```python
# Save a dictionary to a JSON file
settings = {"foo": 1, "bar": "hello"}
save("settings.json", **settings)

# Save multiple dictionaries to a JSON file
settings1 = {"foo": 1, "bar": "hello"}
settings2 = {"baz": 2, "qux": "world"}
save("settings.json", **settings1, **settings2)

# `load` function

Load variables from a JSON file.

## Parameters

- `config_file` (str): The file to load the variables from.
- `unpack` (bool, optional): If `True`, the variables in the JSON file will be unpacked and returned as individual variables. If `False`, the entire contents of the JSON file will be returned as a dictionary. Defaults to `False`.
- `default` (Any, optional): The value to return if the file does not exist or is not a valid JSON file. Defaults to `None`.

## Returns

- `Any`: The variables stored in the JSON file, either as a dictionary or as individual variables, depending on the value of `unpack`. Returns `default` if the file does not exist or is not a valid JSON file.

## Raises

- `IOError`: If there is an error reading from the file.
- `ValueError`: If `unpack` is `True` and the JSON file does not contain a dictionary.

## Example

```python
# Unpack variables
foo, bar = load("settings.json", unpack=True)

# Return dictionary
settings = load("settings.json")
```