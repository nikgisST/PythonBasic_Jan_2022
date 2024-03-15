movеs_in_the_game = int(input())
total_points = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
counter_6 = 0
is_invalid = True #-- > False е коректно да е, но не става в Judge
for current_number in range(0, movеs_in_the_game):
    number = int(input())
    if 0 <= number <= 9:
        advance_1 = 0.20 * number
        total_points += advance_1
        counter_1 += 1
    elif 10 <= number <= 19:
        advance_2 = 0.30 * number
        total_points += advance_2
        counter_2 += 1
    elif 20 <= number <= 29:
        advance_3 = 0.40 * number
        total_points += advance_3
        counter_3 += 1
    elif 30 <= number <= 39:
        advance_4 = 50
        total_points += advance_4
        counter_4 += 1
        total_points = total_points
    elif 40 <= number <= 50:
        advance_5 = 100
        total_points += advance_5
        counter_5 += 1
    elif number < 0 or number > 50:
        total_points = total_points / 2
        counter_6 += 1
        is_invalid = True
        # total_points = total_points
#total_points = total_points
percent_2 = counter_2 / movеs_in_the_game * 100
percent_1 = counter_1 / movеs_in_the_game * 100
percent_3 = counter_3 / movеs_in_the_game * 100
percent_4 = counter_4 / movеs_in_the_game * 100
percent_5 = counter_5 / movеs_in_the_game * 100
percent_6 = counter_6 / movеs_in_the_game * 100
print(f"{total_points:.2f}")
print(f"From 0 to 9: {percent_1:.2f}%")
print(f"From 10 to 19: {percent_2:.2f}%")
print(f"From 20 to 29: {percent_3:.2f}%")
print(f"From 30 to 39: {percent_4:.2f}%")
print(f"From 40 to 50: {percent_5:.2f}%")
if is_invalid:                                        # Не става, защото задължително трябва да се принтират 7 реда, а така в if ще влезе, ако има само такова условие, а не се иска това
    print(f"Invalid numbers: {percent_6:.2f}%")

# movеs_in_the_game = int(input())
# total_points = 0
# counter_1 = 0
# counter_2 = 0
# counter_3 = 0
# counter_4 = 0
# counter_5 = 0
# counter_6 = 0
# is_invalid = False
# for current_number in range(0, movеs_in_the_game):
#     number = int(input())
#     if number >= 0 and number <= 9:
#         advance_1 = 0.20 * number
#         total_points += advance_1
#         counter_1 += 1
#     elif 10 <= number <= 19:
#         advance_2 = 0.30 * number
#         total_points += advance_2
#         counter_2 += 1
#     elif 20 <= number <= 29:
#         advance_3 = 0.40 * number
#         total_points += advance_3
#         counter_3 += 1
#     elif 30 <= number <= 39:
#         advance_4 = 50
#         total_points += advance_4
#         counter_4 += 1
#         total_points = total_points
#     elif 40 <= number <= 50:
#         advance_5 = 100
#         total_points += advance_5
#         counter_5 += 1
#     elif number < 0 or number > 50:
#         total_points = total_points / 2
#         counter_6 += 1
#         is_invalid = True
#         # total_points = total_points
# #total_points = total_points
# percent_1 = counter_1 / movеs_in_the_game * 100
# percent_2 = counter_2 / movеs_in_the_game * 100
# percent_3 = counter_3 / movеs_in_the_game * 100
# percent_4 = counter_4 / movеs_in_the_game * 100
# percent_5 = counter_5 / movеs_in_the_game * 100
# percent_6 = counter_6 / movеs_in_the_game * 100
# print(f"{total_points:.2f}")
# print(f"From 0 to 9: {percent_1:.2f}%")
# print(f"From 10 to 19: {percent_2:.2f}%")
# print(f"From 20 to 29: {percent_3:.2f}%")
# print(f"From 30 to 39: {percent_4:.2f}%")
# print(f"From 40 to 50: {percent_5:.2f}%")
# if is_invalid:
#     print(f"Invalid numbers: {percent_6:.2f}%")