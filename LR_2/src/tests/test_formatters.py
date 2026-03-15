import json
import csv
import yaml
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from formatters.json import JSONFormatter
from formatters.csv import CSVFormatter
from formatters.yaml import YAMLFormatter


data = {
    "USD": 1.0,
    "EUR": 0.9,
    "RUB": 90
}


# -------------------------
# JSON FORMATTER
# -------------------------

def test_json_format_returns_string():
    formatter = JSONFormatter()
    result = formatter.format(data)

    assert isinstance(result, str)
    parsed = json.loads(result)
    assert parsed == data


def test_json_save_creates_file(tmp_path):
    formatter = JSONFormatter()
    file = tmp_path / "data.json"

    formatter.save(data, file)

    with open(file) as f:
        loaded = json.load(f)

    assert loaded == data


# -------------------------
# CSV FORMATTER
# -------------------------

def test_csv_format_contains_keys():
    formatter = CSVFormatter()
    result = formatter.format(data)

    assert "USD" in result
    assert "EUR" in result


def test_csv_save_creates_valid_file(tmp_path):
    formatter = CSVFormatter()
    file = tmp_path / "data.csv"

    formatter.save(data, file)

    with open(file) as f:
        reader = list(csv.reader(f))

    assert any("USD" in row for row in reader)


# -------------------------
# YAML FORMATTER
# -------------------------

def test_yaml_format_returns_yaml_string():
    formatter = YAMLFormatter()
    result = formatter.format(data)

    parsed = yaml.safe_load(result)
    assert parsed == data


def test_yaml_save_creates_file(tmp_path):
    formatter = YAMLFormatter()
    file = tmp_path / "data.yaml"

    formatter.save(data, file)

    with open(file) as f:
        loaded = yaml.safe_load(f)

    assert loaded == data


# -------------------------
# BASE FUNCTIONALITY
# -------------------------

def test_format_returns_string_for_all_formatters():
    formatters = [
        JSONFormatter(),
        CSVFormatter(),
        YAMLFormatter()
    ]

    for formatter in formatters:
        result = formatter.format(data)
        assert isinstance(result, str)


def test_save_writes_file(tmp_path):
    formatter = JSONFormatter()
    file = tmp_path / "test.json"

    formatter.save(data, file)

    assert os.path.exists(file)