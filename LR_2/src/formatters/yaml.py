import yaml
from base import IFormat


class YAMLFormatter(IFormat):
    """
    Класс YAMLFormatter реализует интерфейс IFormat для форматирования
    и сохранения данных в формате YAML.

    Класс предоставляет методы для:
    - преобразования словаря в строку YAML;
    - сохранения отформатированных данных в файл.

    Methods
    -------
    format(data: dict) -> str
        Преобразует словарь в строку YAML.

        Args:
            data (dict): Словарь, который необходимо преобразовать
                в YAML-представление.

        Returns:
            str: Строка данных в формате YAML.

    save(data: dict, filename: str) -> None
        Сохраняет данные словаря в файл в формате YAML.

        Args:
            data (dict): Словарь для сохранения.
            filename (str): Путь и имя файла, в который будут записаны данные.

        Returns:
            None
    """

    def format(self, data: dict) -> str:
        return yaml.safe_dump(data)

    def save(self, data: dict, filename: str) -> None:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.format(data))
