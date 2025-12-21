import json


def create_json(data: dict) -> str:
    """Функция создает json файл и возвращает имя файла"""
    file_name = 'data.json'
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)
    return file_name


def read_json(file_name: str) -> dict:
    """Функция читает json файл и возвращает словарь"""
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def count_sum(data: dict) -> int:
    result = sum(data.values())
    return result


def find_greatest_word(data: dict) -> str:
    result = sorted(data.keys(), key=len, reverse=True)
    return result[0]
