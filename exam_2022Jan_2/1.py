price_1_page = float(input())
price_1_cover = float(input())
percent_discount = int(input())
sum = float(input())
percent_paid = int(input())
money = 0
pages = 899
covers = 2
money = price_1_page * pages + price_1_cover * covers
money -= percent_discount / 100 * money
money = money + sum
money -= percent_paid / 100 * money
print(f"Avtonom should pay {money:.2f} BGN.")