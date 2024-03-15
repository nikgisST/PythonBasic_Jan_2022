month = input()
number_of_nights = int(input())
price_per_one_night_Apartment = 0
price_per_one_night_Studio = 0

if month == "May" or month == "October":
    price_per_one_night_Apartment = 65
    price_per_one_night_Studio = 50
    if 7 < number_of_nights < 14:
        price_per_one_night_Studio -= price_per_one_night_Studio * 0.05
    elif number_of_nights > 14:
        price_per_one_night_Studio -= price_per_one_night_Studio * 0.30
elif month == "June" or month == "September":
    price_per_one_night_Apartment = 68.70
    price_per_one_night_Studio = 75.20
    if number_of_nights > 14:
        price_per_one_night_Studio -= price_per_one_night_Studio * 0.20
    elif number_of_nights <= 14:
        price_per_one_night_Studio = price_per_one_night_Studio
elif month == "July" or month == "August":
    price_per_one_night_Apartment = 77
    price_per_one_night_Studio = 76

if number_of_nights > 14:
    price_per_one_night_Apartment -= price_per_one_night_Apartment * 0.10

price_for_the_whole_stay_Apartment = price_per_one_night_Apartment * number_of_nights
price_for_the_whole_stay_Studio = price_per_one_night_Studio * number_of_nights
print(f"Apartment: {price_for_the_whole_stay_Apartment:.2f} lv.")
print(f"Studio: {price_for_the_whole_stay_Studio:.2f} lv.")
