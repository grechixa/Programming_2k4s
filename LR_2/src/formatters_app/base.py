from abc import ABC, abstractmethod


class IFormat(ABC):
    """
    Абстрактный интерфейс для форматирования и сохранения данных.

    Интерфейс IFormat определяет общий контракт для классов,
    которые реализуют преобразование словаря в строковое
    представление определённого формата (например, CSV, JSON, YAML),
    а также сохранение этих данных в файл.

    Methods
    -------
    format(data: dict) -> str
        Абстрактный метод для форматирования словаря в строку
        определённого формата.

        Args:
            data (dict): Словарь с данными, который необходимо
                преобразовать в строковое представление.

        Returns:
            str: Отформатированная строка.

    save(data: dict, filename: str) -> None
        Сохраняет данные словаря в файл.

        Args:
            data (dict): Словарь с данными для сохранения.
            filename (str): Путь и имя файла для записи.

        Returns:
            None
    """

    @abstractmethod
    def format(self, data: dict) -> str:
        ...
        
    @abstractmethod
    def save(self, data: dict, filename: str) -> None:
        ...
