from get_currencies import get_currencies
from formatters.csv import CSVFormatter
from formatters.json import JSONFormatter
from formatters.yaml import YAMLFormatter

def run():
    data = get_currencies(['USD', 'EUR', "CNY"])

    if data is None:
        print("Ошибка получения данных с сайта ЦБ РФ")
        return
    
    csv_formatter = CSVFormatter()
    csv_formatter.save(data, "rates.csv")

    json_formatter = JSONFormatter()
    json_formatter.save(data, "rates.json")

    yaml_formatter = YAMLFormatter()
    yaml_formatter.save(data, "rates.yaml")

if __name__ == "__main__":
    run()