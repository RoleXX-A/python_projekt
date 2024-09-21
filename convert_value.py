import requests

url = 'https://www.cbr-xml-daily.ru/daily_json.js'

response = requests.get(url)
data = response.json()
amount = int(input("Введите сумму: "))
to_currency = input("Введите валюту для перевода: ").upper()

print(amount/data['Valute'][to_currency]['Value'])
