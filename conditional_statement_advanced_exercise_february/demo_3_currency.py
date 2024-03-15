from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = int(input("Enter the amount of currency:"))
from_currency = input("From currency: ").upper()       #всички изходи са с големи букви
to_currency = input("To currency: ").upper()

result = c.convert(from_currency, to_currency, amount)

profit = f"{float(result) + (float(result) * 0.02):.2f}"

print(amount, from_currency, "--->", profit, to_currency)