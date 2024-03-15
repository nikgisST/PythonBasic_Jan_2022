fruit = input()
day = input()
quantity = float(input())
price = 0
is_valid = True
weekend = day == "Saturday" or day == "Sunday"
is_working_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" or\
                 day == "Thursday" or day == "Friday"
if is_working_day:
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
    else:
        is_valid = False
elif weekend:
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    else:
        is_valid = False
else:
    is_valid = False
total_price = quantity * price
if is_valid is True:                    #if is_valid:
    print(f"{total_price:.2f}")
elif is_valid is False:                #else:
    print("error")



# fruit = input()
# day = input()
# quantity = float(input())
# price = 0
# invalid = False
# weekend = day == "Saturday" or day == "Sunday"
# is_working_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" or\
#                  day == "Thursday" or day == "Friday"
# if is_working_day:
#     if fruit == "banana":
#         price = 2.50
#     elif fruit == "apple":
#         price = 1.20
#     elif fruit == "orange":
#         price = 0.85
#     elif fruit == "grapefruit":
#         price = 1.45
#     elif fruit == "kiwi":
#         price = 2.70
#     elif fruit == "pineapple":
#         price = 5.50
#     elif fruit == "grapes":
#         price = 3.85
#     else:
#         invalid = True
# elif weekend:
#     if fruit == "banana":
#         price = 2.70
#     elif fruit == "apple":
#         price = 1.25
#     elif fruit == "orange":
#         price = 0.90
#     elif fruit == "grapefruit":
#         price = 1.60
#     elif fruit == "kiwi":
#         price = 3.00
#     elif fruit == "pineapple":
#         price = 5.60
#     elif fruit == "grapes":
#         price = 4.20
#     else:
#         invalid = True
# else:
#     invalid = True
# total_price = quantity * price
#
# if invalid is True:
#     print("error")
# else:
#     print(f"{total_price:.2f}")


fruit = input()
day_of_the_week = input()
quantity = float(input())
price = 0
if day_of_the_week in 'Monday Tuesday Wednesday Thursday Friday':
    if fruit == 'banana':
        price = 2.5
    elif fruit == 'apple':
        price = 1.2
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.7
    elif fruit == 'pineapple':
        price = 5.5
    elif fruit == 'grapes':
        price = 3.85
if day_of_the_week in 'Saturday Sunday ':
    if fruit == 'banana':
        price = 2.7
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.90
    elif fruit == 'grapefruit':
        price = 1.60
    elif fruit == 'kiwi':
        price = 3
    elif fruit == 'pineapple':
        price = 5.6
    elif fruit == 'grapes':
        price = 4.2
total_price = price * quantity
if day_of_the_week not in 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday' or \
        fruit not in 'banana apple orange grapefruit kiwi pineapple grapes':
    print('error')
elif total_price > 0.00:
    print(f'{total_price:.2f}')