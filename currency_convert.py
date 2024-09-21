import requests

url = 'https://www.cbr-xml-daily.ru/daily_json.js'

response = requests.get(url)
data = response.json()
val = 'usd'.upper()

print(data['Valute'][val]['Value'])
