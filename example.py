import pysettings

happy = "happy :)"
epic = "epic!!!"
settings = {"happy": "happy :)", "epic": "epic!!!"}
pysettings.save_variables(config_file="settings.json", happy=happy, epic=epic)
pysettings.save_dictionary(settings, config_file="op.json")

nice = pysettings.load_variables("settings.json")
nice_2 = pysettings.load_dictionary("op.json")
print(nice)
print(nice_2)