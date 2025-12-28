import requests


request = requests.get("https://v6.exchangerate-api.com/v6/1f02a8bcab9dd8b8fe365448/latest/USD")
currency = input().upper()

currencies = request.json().get('conversion_rates')

if len(currency.split()) == 1:
    exchange_rate = currencies.get(currency)
    result = {k: v / exchange_rate for k, v in currencies.items()}
else:
    cur_1, cur_2 = currency.split()
    result = currencies.get(cur_2) / currencies.get(cur_1)

print(result)