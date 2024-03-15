budget = float(input())
season = input()
kind_of_holiday = ""                             # НЕ ГИ ДЕФИНИРАМ
destination = ""                                 # НЕ ГИ ДЕФИНИРАМ
price = 0
if season == "summer":
    kind_of_holiday = "Camp"
elif season == "winter":
    kind_of_holiday = "Hotel"

if budget <= 100:                                 # Бюджетът определя къдееее!
    destination = "Bulgaria"
    if season == "summer":
        price = budget - 0.30 * budget
    elif season == "winter":
        price = budget - 0.70 * budget

elif budget <= 1000:                             # elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget - 0.40 * budget
    elif season == "winter":
        price = budget - 0.80 * budget
elif budget > 1000:                              #else
    destination = "Europe"
    price = budget - 0.90 * budget

if destination == "Europe":                     # ТАЗИ ПРОВЕРКА Е ПОСЛЕДНААААА
    kind_of_holiday = "Hotel"                   # ЗАРАДИ ТОВА, ЧЕ ОТ ПАРИТЕ ДЕСТИНАЦИЯТА СТАВА ЕВРОПА СЕ СМЕНЯ ОТ САМП НА ХОТЕЛ

difference = abs(price - budget)
print(f"Somewhere in {destination}")
print(f"{kind_of_holiday} - {difference:.2f}")




# budget = float(input())
# season = input()
# kind_of_holiday = "Camp"
# destination = "Bulgaria"
# price = 0
# if season == "summer":
#     kind_of_holiday = "Camp"
# elif season == "winter":
#     kind_of_holiday = "Hotel"
# if destination == "Europe":
#     kind_of_holiday = "Hotel"
# if price <= 100 and destination == "Bulgaria":
#     if season == "summer":
#         price = budget - 0.30 * budget
#     elif season == "winter":
#         price = budget - 0.70 * budget
# elif price <= 1000 and destination == "Balkans":
#     if season == "summer":
#         price = budget - 0.40 * budget
#     elif season == "winter":
#         price = budget - 0.80 * budget
# elif price > 1000 and destination == "Europe":
#     price = budget - 0.90 * budget
# difference = abs(price - budget)
# print(f"Somewhere in {destination}")
# print(f"{kind_of_holiday} - {difference:.2f}")




# budget = float(input())
# season = input()
# destination = ""
# type_of_vacation = ""
# price = 0
# if season == "summer":
#     pass
# elif season == "winter":
#     pass
# if destination == "Europe":
#     pass
# if type_of_vacation == "Camp" or type_of_vacation == "Hotel":
#     if budget <= 100:
#         destination = "Bulgaria"
#         if season == "summer":
#             price = budget - 0.30 * budget
#         elif season == "winter":
#             price = budget - 0.70 * budget
#     elif budget <= 1000:
#         destination = "Balkans"
#         if season == "summer":
#             price = budget - 0.40 * budget
#         elif season == "winter":
#             price = budget - 0.80 * budget
#     elif budget > 1000:
#         destination = "Europe"
#         price = budget - 0.90 * budget
# difference = abs(price - budget)
# print(f"Somewhere in {destination}")
# print(f"{type_of_vacation} - {difference:.2f}")

