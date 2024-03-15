price_for_luggage_over_20_kg = float(input())
pounds_of_luggage = float(input())
days_before_trip = int(input())
number_of_luggage = int(input())
price = 0
if pounds_of_luggage < 10:
    price = price_for_luggage_over_20_kg * 0.20
elif pounds_of_luggage <= 20:
    price = price_for_luggage_over_20_kg * 0.50
else:
    price = price_for_luggage_over_20_kg
if days_before_trip < 7:
    price += price * 0.40
elif days_before_trip <= 30:
    price += price * 0.15
else:
    price += price * 0.10
total_price = number_of_luggage * price
print(f"The total price of bags is: {total_price:.2f} lv.")