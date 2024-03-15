days_for_stay = int(input())
type_of_room = input()
evaluation = input()
#price_for_the_whole_stay = 0
price_for_a_night = 0
discount = 0
count_of_nights = days_for_stay - 1
if type_of_room == "room for one person":
    price_for_a_night = 18.00
    #count_of_nights = days_for_stay - 1
    price = count_of_nights * price_for_a_night
elif type_of_room == "apartment":
    price_for_a_night = 25.00
    #count_of_nights = days_for_stay - 1
    price = price_for_a_night * count_of_nights
    if days_for_stay < 10:
        price -= 0.30 * price
    elif days_for_stay < 15:
        price -= 0.35 * price
    elif days_for_stay >= 15:                                 # <= TYK?
        price -= 0.50 * price
elif type_of_room == "president apartment":
    price_for_a_night = 35.00
    #count_of_nights = days_for_stay - 1
    price = price_for_a_night * count_of_nights
    if days_for_stay < 10:
        price -= 0.10 * price
    elif days_for_stay < 15:
        price -= 0.15 * price
    elif days_for_stay >= 15:                                 # <= TYK?
        price -= 0.20 * price
if evaluation == "positive":
    price = price + 0.25 * price
    print(f"{price:.2f}")
elif evaluation == "negative":
    price = price - 0.10 * price
    print(f"{price:.2f}")