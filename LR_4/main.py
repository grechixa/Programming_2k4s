class MusicSystem:
    def __init__(self, genre: str, level: int, minutes: str):
        pass
    def play_music(self, genre):
        return (f"Играет жанр {genre}")
    def set_volume(self, level):
        return (f"Установлена громкость {level}")
    def set_timer(self, minutes):
        return (f"Установлен таймер на {minutes} минут")

class LightSystem:
    def __init__(self, status: str):
        pass
    def set_status(self, status):
        return (f"Свет {status}")

class TemperatureSystem:
    def __init__(self, status: str, temp: int):
        pass
    def set_temp(self, temp):
        return (f"Установлена температура {temp} градусов")

class AlarmSystem:
    def __init__(self, at_time:str):
        pass
    def set_alarm(self, at_time):
        return (f"Установлен будильник на {at_time} часов")
