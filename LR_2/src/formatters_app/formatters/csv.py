import csv
from ..base import IFormat

class CSVFormatter(IFormat):
    """
Класс CSVFormatter реализован для преобразования данных словаря в формат CSV.

Этот класс реализует интерфейс IFormat и предоставляет методы для:
- форматирования данных в строку CSV;
- сохранения данных непосредственно в CSV-файл.

Methods
-------
format(data: dict) -> str
    Форматирует заданные данные словаря в строку CSV.

    Args:
        data (dict): Словарь для форматирования, где ключи и значения
            обрабатываются как строки CSV.

    Returns:
        str: Строковое представление данных в формате CSV, где каждая
            пара ключ–значение является отдельной строкой.

save(data: dict, filename: str) -> None
    Сохраняет переданный словарь в CSV-файл.

    Args:
        data (dict): Словарь, который необходимо сохранить. Ключи и значения
            записываются как строки CSV.
        filename (str): Путь и имя файла, в который будут сохранены данные.

    Returns:
        None
"""
    def format(self, data: dict) -> str:
        rows = []
        for k,v in data.items():
            rows.append((k,v))
        return "\n".join(",".join(map(str, row)) for row in rows)
    
    def save(self, data: dict, filename: str) -> None:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            for k,v in data.items():
                writer.writerow([k,v])
