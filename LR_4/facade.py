from systems import MusicSystem, LightSystem, TemperatureSystem, AlarmSystem

class SmartHomeFacade:
    def __init__(self):
        self.music = MusicSystem()
        self.light = LightSystem()
        self.temp = TemperatureSystem()
        self.alarm = AlarmSystem()

    def sleep_mode(self):
        results = []
        results.append(self.light.turn_off())
        results.append(self.music.set_volume(3))
        results.append(self.music.play_music("calm"))
        results.append(self.music.set_timer(20))
        results.append(self.temp.set_temperature(20))
        results.append(self.alarm.set_alarm("06:00"))
        return results
