# pysettings

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A python module for saving and loading settings

This module will most likely change it's name depending on availability in pypi

## Get Started

This is not recommended yet, as the module is in development constantly

```console
$ pip install git+https://github.com/sryu1/pysettings
```

```python
import pysettings

value_1 = 1
value_two = "two"

pysettings.save(config_file="settings.json", value_1=value_1, value_two=value_two)
one, two = pysettings.load(config_file="settings.json", unpack=True)
print(one)
print(two)
```

If you find a bug, please report them in issues, pull requests are welcome :)
