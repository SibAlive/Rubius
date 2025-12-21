import utils.helpers as helpers


my_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
}

# Создаем json файл
file_name = helpers.create_json(my_dict)

# Читаем данные из json файла
json_dict = helpers.read_json(file_name)

# Считаем сумму чисел значений словаря
summary = helpers.count_sum(json_dict)

# Находим самое длинное слово среди ключей словаря
greatest_word = helpers.find_greatest_word(json_dict)

print(f"Сумма значений словаря: {summary}\n"
      f"Саммое длинное слово среди ключей словаря: {greatest_word}")