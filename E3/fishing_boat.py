budget = int(input())
season = input()
number_of_fishermen = int(input())
rent = 0
if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600
if number_of_fishermen <= 6:
    rent -= rent * 0.10                                       #rent *= 0.90 = 1 - 10% = 1 - 0.10 = 0.90
elif number_of_fishermen <= 11:
    rent = rent - rent * 0.15                                 #rent *= 0.85 = 1 - 15% = 1 - 0.15 = 0.85   #rent -= rent * 0.15
elif number_of_fishermen >= 12:                                  # >= !!!!!!!!!!!!!!!!!!!!!!!!!!!
    rent = rent - rent * 0.25                                 #rent *= 0.75 = 1 - 25% = 1 - 0.25 = 0.75   #rent -= rent * 0.25
if not season == "Autumn" and number_of_fishermen % 2 == 0:       #if season != "Autumn" and number...
    rent = rent - rent * 0.05                                 #rent *= 0.95 = 1 - 5% = 1 - 0.05 = 0.95    #rent -= rent * 0.05
difference = abs(rent - budget)
if budget >= rent:
    print(f"Yes! You have {difference:.2f} leva left.")
elif budget < rent:
    print(f"Not enough money! You need {difference:.2f} leva.")