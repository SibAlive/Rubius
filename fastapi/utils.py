import json


async def add_to_file(new_data, item_id=None):
    with open("data.json", 'r', encoding='utf-8') as f:
        data = json.load(f)

    if item_id:
        data[item_id] = new_data
    else:
        data = new_data

    with open("data.json", 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def open_file():
    with open("data.json", 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data