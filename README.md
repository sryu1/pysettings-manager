# pysettings
A module for saving and loading settings

## Get Started
This is not recommended yet, as the module is in development constantly
```console
$ pip install git+https://github.com/sryu1/pysettings
```

```python
import pyinstaller

value_1 = 1
value_two = "two"

pyisntaller.save(config_file="settings.json", value_1=value_1, value_two=value_two)
one, two = pyinstaller.load(config_file="settings.json", unpack=True)
print(one)
print(two)
```
