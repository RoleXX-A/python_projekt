import requests

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
def convert_val():
    response = requests.get(url)
    data = response.json()
    amount = int(input("Введите сумму: "))
    to_currency = input("Введите валюту для перевода: ").upper()
    result_convert = amount / data['Valute'][to_currency]['Value']
    print(result_convert)


response = requests.get(url)
data = response.json()
print(data)
print(data['Valute']['AUD']['Value'])