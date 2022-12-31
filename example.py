import pysettings

happy = "happy :)"
epic = "epic!!!"
settings = {"happy": "happy :)", "epic": "epic!!!"}
pysettings.save("settings.json", **settings)
print(pysettings.config_file_exists("settings.json"))

nice, nice_1 = pysettings.load("settings.json", unpack=True)
print(nice)
