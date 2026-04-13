from facade import SmartHomeFacade

home = SmartHomeFacade()

for action in home.sleep_mode():
    print(action)



