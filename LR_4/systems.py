class MusicSystem:
    """Система управления музыкой"""
    def __init__(self):
        self.genre = None
        self.volume = None
        self.timer = None

    def play_music(self, genre):
        """Включить музыку"""
        self.genre = genre
        return (f"Играет жанр {genre}")

    def set_volume(self, level):
        """Регулировка громкости"""
        self.volume = level
        return (f"Установлена громкость {level}")

    def set_timer(self, minutes):
        """Авто-отключение музыки через какое-то время"""
        self.timer = minutes
        return (f"Музыка включена и остановиться через {minutes} минут")

class LightSystem:
    """Система управления светом"""
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        """Включить свет"""
        self.is_on = True
        return "Свет включен"
    
    def turn_off(self):
        """Выключить свет"""
        self.is_on = False
        return "Свет выключен"

class TemperatureSystem:
    """Система управления температурой"""
    def __init__(self):
        self.temperature = None

    def set_temperature(self, temp):
        """Установить температуру на N градусов"""
        self.temperature = temp
        return (f"Установлена температура {temp} градусов")

class AlarmSystem:
    """Будильник"""
    def __init__(self):
        self.at_time = None
    
    def set_alarm(self, at_time):
        """Завести будильник на N часов"""
        self.at_time = at_time
        return (f"Установлен будильник на {at_time} часов")
