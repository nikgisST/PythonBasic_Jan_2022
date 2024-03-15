budget = float(input())
season = input()
kind_of_holiday = ""
destination = ""
costs = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        costs = 0.30 * budget
        kind_of_holiday = "Camp"
    elif season == "winter":
        costs = 0.70 * budget
        kind_of_holiday = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        costs = 0.40 * budget
        kind_of_holiday = "Camp"
    elif season == "winter":
        costs = 0.80 * budget
        kind_of_holiday = "Hotel"
elif budget > 1000:
    destination = "Europe"
    costs = 0.90 * budget
    kind_of_holiday = "Hotel"
print(f"Somewhere in {destination}")
print(f"{kind_of_holiday} - {costs:.2f}")



# budget = float(input())
# season = input()
# costs = 0
# if budget <= 100:
#     print("Somewhere in Bulgaria")
#     if season == "summer":
#         costs = 0.30 * budget
#         print(f"Camp - {costs:.2f}")
#     elif season == "winter":
#         costs = 0.70 * budget
#         print(f"Hotel - {costs:.2f}")
# elif budget <= 1000:
#     print("Somewhere in Balkans")
#     if season == "summer":
#         costs = 0.40 * budget
#         print(f"Camp - {costs:.2f}")
#     elif season == "winter":
#         costs = 0.80 * budget
#         print(f"Hotel - {costs:.2f}")
# elif budget > 1000:
#     print("Somewhere in Europe")
#     costs = 0.90 * budget
#     print(f"Hotel - {costs:.2f}")