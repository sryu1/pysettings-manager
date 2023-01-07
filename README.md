# pysettings-manager

[![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/sryu1/pysettings-manager)](https://github.com/sryu1/pysettings-manager/releases)
A python module for saving and loading settings

## Get Started

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
