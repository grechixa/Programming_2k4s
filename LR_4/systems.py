class MusicSystem:
    def __init__(self):
        self.genre = None
        self.volume = None
        self.timer = None

    def play_music(self, genre):
        self.genre = genre
        return (f"Играет жанр {genre}")

    def set_volume(self, level):
        self.volume = level
        return (f"Установлена громкость {level}")

    def set_timer(self, minutes):
        self.timer = minutes
        return (f"Установлен таймер на {minutes} минут")

class LightSystem:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        return "Свет включен"
    
    def turn_off(self):
        self.is_on = False
        return "Свет выключен"

class TemperatureSystem:
    def __init__(self):
        self.temperature = None

    def set_temperature(self, temp):
        self.temperature = temp
        return (f"Установлена температура {temp} градусов")

class AlarmSystem:
    def __init__(self):
        self.at_time = None
    
    def set_alarm(self, at_time):
        self.at_time = at_time
        return (f"Установлен будильник на {at_time} часов")
