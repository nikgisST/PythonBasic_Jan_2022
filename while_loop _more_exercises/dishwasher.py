detergent_bottles = int(input())
total_detergent_bottles = detergent_bottles * 750
counter = 0
pots = 0
plates = 0
pots_detergent = 0
plates_detergent = 0
sum = 0
detergent_is_finished = False
while sum <= total_detergent_bottles:
    command = input()
    if command == "End":
        detergent_is_finished = True
        break
    total_dishes = int(command)
    counter += 1
    if counter % 3 == 0:
        pots += int(total_dishes)
        pots_detergent += int(total_dishes) * 15
    else:
        plates += int(total_dishes)
        plates_detergent += int(total_dishes) * 5
    sum = pots_detergent + plates_detergent
difference = abs(sum - total_detergent_bottles)
if detergent_is_finished:                          #if sum <= total_detergent_bottles:
    print("Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {difference} ml.")
elif not detergent_is_finished:                           #elif sum > total_detergent_bottles:
    print(f"Not enough detergent, {difference} ml. more necessary!")


# detergent_for_dishes = 5
# detergent_for_pots = 15
# bottle_of_detergent = 750
# count_of_the_counter = 0
# dishes_counter = 0
# pots_counter = 0
# detergent_over = False
# number_of_bottles_detergent = int(input())
# total_detergent = number_of_bottles_detergent * bottle_of_detergent
# tell_me_the_difference = total_detergent
# number_of_vessels = input()
# while number_of_vessels != "End":
#     count_of_the_counter += 1
#     if count_of_the_counter % 3 == 0:
#         pots_counter += int(number_of_vessels)
#         total_detergent -= int(number_of_vessels) * detergent_for_pots
#     else:
#         dishes_counter += int(number_of_vessels)
#         total_detergent -= int(number_of_vessels) * detergent_for_dishes
#     if total_detergent <= 0:
#         detergent_over = True
#         break
#     number_of_vessels = input()
# detergent_diff = abs(total_detergent)
# if detergent_over:
#     print(f"Not enough detergent, {detergent_diff} ml. more necessary!")
# else:
#     print("Detergent was enough!")
#     print(f"{dishes_counter} dishes and {pots_counter} pots were washed.")
#     print(f"Leftover detergent {detergent_diff} ml.")
#
#
#
# bottles_detergent = int(input())
# quantity_of_detergent = bottles_detergent * 750
# command = input()
# plates = 0
# cooking_pans = 0
# count_wash = 0
# detergent_usage = 0
# detergent_is_finished = False
# while command != "End":
#     count_wash += 1
#     number_of_dishes = int(command)
#     if count_wash % 3 == 0:
#         cooking_pans += number_of_dishes
#         detergent_usage = number_of_dishes * 15
#         quantity_of_detergent -= detergent_usage
#     else:
#         plates += number_of_dishes
#         detergent_usage = number_of_dishes * 5
#         quantity_of_detergent -= detergent_usage
#     if quantity_of_detergent < 0:
#         detergent_is_finished = True
#         break
#     command = input()
# if detergent_is_finished:
#     print(f"Not enough detergent, {abs(quantity_of_detergent)} ml. more necessary!")
# else:
#     print("Detergent was enough!")
#     print(f"{plates} dishes and {cooking_pans} pots were washed.")
#     print(f"Leftover detergent {abs(quantity_of_detergent)} ml.")
#
#
# num_bottles_detergent = int(input())
# available_detergent = num_bottles_detergent * 750
# needed_detergent = 0
# counter_days = 0
# counter_clean_plates = 0
# counter_clean_pots = 0
# while available_detergent >= needed_detergent:
#     command = input()
#     if command == "End":
#         break
#     else:
#         counter_days += 1
#         current_num_dishes = int(command)
#         if counter_days % 3 == 0:
#             needed_detergent += current_num_dishes * 15
#             counter_clean_pots += current_num_dishes
#         else:
#             needed_detergent += current_num_dishes * 5
#             counter_clean_plates += current_num_dishes
# diff = abs(needed_detergent - available_detergent)
# if available_detergent >= needed_detergent:
#     print("Detergent was enough!")
#     print(f"{counter_clean_plates} dishes and {counter_clean_pots} pots were washed.")
#     print(f"Leftover detergent {diff} ml.")
# else:
#     print(f"Not enough detergent, {diff} ml. more necessary!")
#
#
