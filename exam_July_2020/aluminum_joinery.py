number_of_joinery = int(input())
type_of_joinery = input()
way_of_delivery = input()
price = 0
total_price = 0
delivery_price = 0
if type_of_joinery == "90X130":
    price = 110
    total_price = price * number_of_joinery
    if 30 < number_of_joinery <= 60:
        total_price -= total_price * 0.05
    elif number_of_joinery > 60:
        total_price -= total_price * 0.08
elif type_of_joinery == "100X150":
    price = 140
    total_price = price * number_of_joinery
    if 40 < number_of_joinery <= 80:
        total_price -= total_price * 0.06
    elif number_of_joinery > 80:
        total_price -= total_price * 0.1
elif type_of_joinery == "130X180":
    price = 190
    total_price = price * number_of_joinery
    if 20 < number_of_joinery <= 50:
        total_price -= total_price * 0.07
    elif number_of_joinery > 50:
        total_price -= total_price * 0.12
elif type_of_joinery == "200X300":
    price = 250
    total_price = price * number_of_joinery
    if 25 < number_of_joinery <= 50:
        total_price -= total_price * 0.09
    elif number_of_joinery > 50:
        total_price -= total_price * 0.14

if way_of_delivery == "Without delivery":
    delivery_price = 0
    total_price += delivery_price
elif way_of_delivery == "With delivery":
    delivery_price = 60
    total_price += delivery_price

if number_of_joinery > 99:
    total_price -= total_price * 0.04
else:
    total_price = total_price
if not number_of_joinery < 10:
    print(f"{total_price:.2f} BGN")
else:
    print(f"Invalid order")