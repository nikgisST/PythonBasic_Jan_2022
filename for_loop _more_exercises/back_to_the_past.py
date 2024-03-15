inherited_money = float(input())
year = int(input())
current_years = 18
for year in range(1800, year + 1):
    if year % 2 == 0:
        inherited_money -= 12000
    elif year % 2 != 0:
        inherited_money -= 12000 + (18 + (year - 1800)) * 50
if inherited_money >= 0:
#difference = abs(inherited_money - inherited_money - (12000 + 50 * 19))
#if inherited_money >= inherited_money - (12000 + 50 * (18 + 1)):
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
else:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")

inherited_money = float(input())
year = int(input())
current_years = 18
for year in range(1800, year + 1):
    if year % 2 == 0:
        inherited_money -= 12000
    else:
        inherited_money -= 12000 + current_years * 50
    current_years += 1
if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
else:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")


inherited_money = float(input())
year_to_live = int(input())
money_spent = 0
age = 18
for year in range(1800,year_to_live+1):
    if year % 2 == 0:
        money_spent += 12000
    else:
        money_spent += 12000 + 50 * age
    age += 1
difference = abs(money_spent - inherited_money)
if inherited_money >= money_spent:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
else:
    print(f"He will need {difference:.2f} dollars to survive.")