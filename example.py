import pysettings_manager as pysm

config_file = "settings.json"

happy = "happy :)"
epic = "epic!!!"
settings = {"happy": "happy :)", "epic": "epic!!!"}
pysm.save(config_file, **settings)
print(pysm.config_file_exists(config_file))

nice, nice_1 = pysm.load(config_file, unpack=True)
print(nice)
