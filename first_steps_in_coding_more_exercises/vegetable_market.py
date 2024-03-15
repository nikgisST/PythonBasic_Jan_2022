price_per_kilogram_of_vegetables = float(input())
price_per_kilogram_of_fruits = float(input())
total_kilogram_of_vegetable = int(input())
total_kilogram_of_fruits = int(input())
income = price_per_kilogram_of_fruits * total_kilogram_of_fruits + price_per_kilogram_of_vegetables * total_kilogram_of_vegetable
income_in_euro = income / 1.94
print(f"{income_in_euro:.2f}")
