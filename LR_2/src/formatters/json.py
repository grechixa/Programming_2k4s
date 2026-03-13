import json
from ..base import IFormat


class JSONFormatter(IFormat):
    """
    Класс JSONFormatter реализует интерфейс IFormat для форматирования
    и сохранения данных в формате JSON.

    Класс предоставляет методы для:
    - преобразования словаря в JSON-строку с отступами и сортировкой ключей;
    - сохранения отформатированных данных в файл.

    Methods
    -------
    **format(data: dict) -> str**
        **Преобразует словарь в строку JSON.**

        Args:
            data (dict): Словарь, который необходимо преобразовать в JSON.

        Returns:
            str: JSON-строка с отступами и отсортированными ключами.

    **save(data: dict, filename: str) -> None**
        **Сохраняет данные словаря в файл в формате JSON.**

        Args:
            data (dict): Словарь для сохранения.
            filename (str): Путь и имя файла, в который будут записаны данные.

        Returns:
            None
    """

    def format(self, data: dict) -> str:
        return json.dumps(data, indent=2, sort_keys=True)

    def save(self, data: dict, filename: str) -> None:
        with open(filename, "w") as f:
            f.write(self.format(data))
