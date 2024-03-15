kind_of_flowers = input()
count = int(input())
budget = int(input())
price_Roses = 5
price_Dahlias = 3.80
price_Tulips = 2.80
price_Narcissus = 3
price_Gladiolus = 2.50
total_price = 0
bought = 0                                 #ем тъй трябва
if kind_of_flowers == "Roses":
    if count > 80:
        bought = count * price_Roses
        total_price = bought - bought * 0.10  #НИЕ ТЪРСИМ ТOTAL_PRICE НЯМА КАК ДА ГО + ИЛИ - В ДРУГИТЕ ЗАДАЧИ ГО ИМА ДАДЕН
    else:
        total_price = count * price_Roses
elif kind_of_flowers == "Dahlias":
    if count > 90:
        bought = count * price_Dahlias
        total_price = bought - bought * 0.15
    else:
        total_price = count * price_Dahlias
elif kind_of_flowers == "Tulips":
    if count > 80:
        bought = count * price_Tulips
        total_price = bought - bought * 0.15
    else:
        total_price = count * price_Tulips
elif kind_of_flowers == "Narcissus":
    if count < 120:
        bought = count * price_Narcissus
        total_price = bought + bought * 0.15
    else:
        total_price = count * price_Narcissus
elif kind_of_flowers == "Gladiolus":
    if count < 80:
        bought = count * price_Gladiolus
        total_price = bought + bought * 0.20
    else:
        total_price = count * price_Gladiolus
difference = abs(total_price - budget)
if total_price <= budget:
    print(f"Hey, you have a great garden with {count} {kind_of_flowers} and {difference:.2f} leva left.")
elif total_price > budget:
    print(f"Not enough money, you need {difference:.2f} leva more.")


# kind_of_flowers = input()
# count = int(input())
# budget = int(input())
# price_Roses = 5
# price_Dahlias = 3.80
# price_Tulips = 2.80
# price_Narcissus = 3
# price_Gladiolus = 2.50
# total_price = 0
# bought = 0
# if kind_of_flowers == "Roses":
#     if count > 80:
#         bought = count * price_Roses
#         total_price = bought - bought * 0.10  #НИЕ ТЪРСИМ ТOTAL_PRICE НЯМА КАК ДА ГО + ИЛИ - В ДРУГИТЕ ЗАДАЧИ ГО ИМА ДАДЕН
#     else:
#         total_price = count * price_Roses
# elif kind_of_flowers == "Dahlias":
#     if count > 90:
#         bought = count * price_Dahlias
#         total_price = bought - bought * 0.15
#     else:
#         total_price = count * price_Dahlias
# elif kind_of_flowers == "Tulips":
#     if count > 80:
#         bought = count * price_Tulips
#         total_price = bought - bought * 0.15
#     else:
#         total_price = count * price_Tulips
# elif kind_of_flowers == "Narcissus":
#     if count < 120:
#         bought = count * price_Narcissus
#         total_price = bought + bought * 0.15
#     else:
#         total_price = count * price_Narcissus
# elif kind_of_flowers == "Gladiolus":
#     if count < 80:
#         bought = count * price_Gladiolus
#         total_price = bought + bought * 0.20
#     else:
#         total_price = count * price_Gladiolus
# difference = abs(total_price - budget)
# if total_price <= budget:
#     print(f"Hey, you have a great garden with {count} {kind_of_flowers} and {difference:.2f} leva left.")
# elif total_price > budget:
#     print(f"Not enough money, you need {difference:.2f} leva more.")



