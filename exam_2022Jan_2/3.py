month = input()
hours = int(input())
people = int(input())
time_of_the_day = input()
total_price = 0
price = 0
if month == "march" or month == "april" or month == "may":
    if time_of_the_day == "day":
        price = 10.50
    elif time_of_the_day == "night":
        price = 8.40
    if people >= 4:
        price -= price * 0.10
    if hours >= 5:
        price -= price * 0.50
elif month == "june"or month == "july" or month == "august":
    if time_of_the_day == "day":
        price = 12.60
    elif time_of_the_day == "night":
        price = 10.20
    if people >= 4:
        price -= price * 0.10
    if hours >= 5:
        price -= price * 0.50
total_price = hours * people * price
print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")
