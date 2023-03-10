# pysettings-manager

[![Python Versions](https://img.shields.io/pypi/pyversions/pysettings-manager)](https://www.python.org/downloads/)
[![PyPI Version](https://img.shields.io/pypi/v/pysettings-manager)](https://pypi.org/project/pysettings-manager)
[![PyPI downloads](https://img.shields.io/pypi/dm/pysettings-manager.svg)](https://pypistats.org/packages/pysettings-manager)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A python module for saving and loading settings

## Get Started

Take a look at the [documentation](https://sryu1.gitbook.io/pysettings-manager/)

```console
pip install pysettings-manager
```

```python
import pysettings_manager as pysm

value_1 = 1
value_two = "two"

pysm.save(config_file="settings.json", value_1=value_1, value_two=value_two)
one, two = pysm.load(config_file="settings.json", unpack=True)
print(one)
print(two)
```

If you find a bug, please report them in issues, pull requests are welcome :)
