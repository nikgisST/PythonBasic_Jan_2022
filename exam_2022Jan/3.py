count_people = int(input())
season = input()
price = 0
total_price = 0
if season == "spring":
    if count_people <= 5:
        price = 50
    elif count_people > 5:
        price = 48
    total_price = price * count_people
elif season == "summer":
    if count_people <= 5:
        price = 48.50
    elif count_people > 5:
        price = 45
    total_price = price * count_people
    total_price = total_price - 0.15 * total_price
elif season == "autumn":
    if count_people <= 5:
        price = 60
    elif count_people > 5:
        price = 49.50
    total_price = price * count_people
elif season == "winter":
    if count_people <= 5:
        price = 86
    elif count_people > 5:
        price = 85
    total_price = price * count_people
    total_price = total_price + 0.08 * total_price
print(f"{total_price:.2f} leva.")