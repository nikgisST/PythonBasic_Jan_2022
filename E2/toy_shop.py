excursion_price = float(input())
count_puzzles = int(input())
count_talking_dolls = int(input())
count_teddy_bears = int(input())
count_minions = int(input())
count_trucks = int(input())
puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2
toy_price = count_puzzles * puzzle_price + count_talking_dolls * talking_doll_price + \
              count_teddy_bears * teddy_bear_price + count_minions * minion_price + \
              count_trucks * truck_price
all_toys = count_puzzles + count_talking_dolls + count_teddy_bears + count_minions + count_trucks
if all_toys >= 50:
    discount = toy_price * 0.25
else:
    discount = 0
final_price = toy_price - discount
rent = final_price * 0.10
needed_sum = final_price - rent
difference = abs(needed_sum - excursion_price)
if needed_sum >= excursion_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
