screening_type = input()
rows = int(input())
columns = int(input())
capacity = rows * columns
price = 0
if screening_type == "Premiere":
    price = 12.00
elif screening_type == "Normal":
    price = 7.50
elif screening_type == "Discount":
    price = 5.00
income = capacity * price
print(f"{income:.2f}")