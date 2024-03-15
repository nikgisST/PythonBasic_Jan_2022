budget = float(input())
number_of_statists = int(input())
one_dress_price = float(input())
decor = budget * 0.10
dresses_price = number_of_statists * one_dress_price
if number_of_statists > 150:
    dresses_price -= dresses_price * 0.10           #total_dress_price *= 0.9
else:
    dresses_price = dresses_price
needed_money = dresses_price + decor
difference = abs(needed_money - budget)
if needed_money > budget:                                            #budget !!!!!
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")     #:.2f !!!!!!!!!!
else:
    print("Action!")
    print(f"Wingard starts filming with {needed_money:.2f} leva left.")