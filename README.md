# pysettings
A python module for saving and loading settings

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
