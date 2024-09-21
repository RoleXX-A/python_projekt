from currency_converter import CurrencyConverter

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyConverter()
    result = c.convert(amount,from_currency,to_currency)
    return result

amount = float(input("Введите сумму: "))
from_currency = "rub".upper()
to_currency = input("Введите в какую валюту перевести: ").upper()

converted_amount = convert_currency(amount, from_currency, to_currency)

print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")


