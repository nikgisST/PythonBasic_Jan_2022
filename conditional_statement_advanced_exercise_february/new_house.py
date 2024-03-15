type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())
costs = 0
if type_of_flowers == "Roses":
    costs = 5 * number_of_flowers
    if number_of_flowers > 80:
        costs -= costs * 0.10             # Alt + J
elif type_of_flowers == "Dahlias":
    costs = 3.80 * number_of_flowers
    if number_of_flowers > 90:
        costs -= costs * 0.15
elif type_of_flowers == "Tulips":
    costs = 2.80 * number_of_flowers
    if number_of_flowers > 80:
        costs -= costs * 0.15
elif type_of_flowers == "Narcissus":
    costs = 3 * number_of_flowers
    if number_of_flowers < 120:
        costs += costs * 0.15
elif type_of_flowers == "Gladiolus":
    costs = 2.50 * number_of_flowers
    if number_of_flowers < 80:
        costs += costs * 0.20
diff = abs(costs - budget)
if costs <= budget:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {diff:.2f} leva left.")
elif costs > budget:
    print(f"Not enough money, you need {diff:.2f} leva more.")









