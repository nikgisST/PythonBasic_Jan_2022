budget = float(input())
price_flour = float(input())
eggs_price = 0.75 * price_flour
price_milk = 1.25 * price_flour
price_of_loaf = eggs_price + price_flour + 0.25 * price_milk
colored_eggs = 0
counter_of_loaf = 0
while budget >= price_of_loaf:
    budget -= price_of_loaf
    counter_of_loaf += 1
    colored_eggs += 3
    if counter_of_loaf % 3 == 0:
        colored_eggs -= counter_of_loaf - 2
print(f"You made {counter_of_loaf} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")



budged = float(input())
flour_price = float(input())
colored_eggs = 0
eggs_price = flour_price * 0.75
milk_liter_price = flour_price + (flour_price * 0.25)
milk_needed_price = milk_liter_price / 4
bread_price = eggs_price + flour_price + milk_needed_price
bread_count = budged // bread_price
bread_count = int(bread_count)
for i in range(1, bread_count + 1):
    colored_eggs += 3
    if i % 3 == 0:
        colored_eggs -= i - 2
money_left = budged - (bread_price * bread_count)
print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
