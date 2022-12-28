import pysettings

happy = "happy :)"
epic = "epic!!!"
settings = {"happy": "happy :)", "epic": "epic!!!"}
pysettings.save_variables(settings_file="settings.json", happy=happy, epic=epic)

nice = pysettings.load("settings.json")
# locals().update(nice)
print(nice)
