days_for_stay = int(input())
type_of_room = input()
evaluation = input()
price = 0
count_of_nights = days_for_stay - 1
if type_of_room == "room for one person":
    price = 18 * count_of_nights
elif type_of_room == "apartment":
    price = 25 * count_of_nights
    if days_for_stay < 10:
        price -= 0.30 * price
    elif days_for_stay <= 15:
        price -= 0.35 * price
    elif days_for_stay > 15:
        price -= 0.50 * price
elif type_of_room == "president apartment":
    price = 35 * count_of_nights
    if days_for_stay < 10:
        price -= 0.10 * price
    elif days_for_stay <= 15:
        price -= 0.15 * price
    elif days_for_stay > 15:
        price -= 0.20 * price
if evaluation == "positive":
    price += 0.25 * price
elif evaluation == "negative":
    price -= 0.10 * price
print(f"{price:.2f}")