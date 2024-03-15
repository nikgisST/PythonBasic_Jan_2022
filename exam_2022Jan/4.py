import math

count_days = int(input())
kilometers_first_day = float(input())
total_kilometers = kilometers_first_day
for current_day in range(1, count_days + 1):
    percents_update = int(input())
    kilometers_first_day = kilometers_first_day + kilometers_first_day * percents_update / 100
    total_kilometers += kilometers_first_day
diff = abs(total_kilometers - 1000)
if total_kilometers >= 1000:
    print(f"You've done a great job running {math.ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(diff)} more kilometers")




# import math
#
# days_to_train = int(input())
# first_distance = float(input())
# trip_to_end = 1000
# total_distance_trained = first_distance
# she_weakned = False
# for i in range(days_to_train):
#     percent_to_train_input = int(input())
#     first_distance = first_distance + first_distance * percent_to_train_input / 100
#     total_distance_trained += first_distance
#     if total_distance_trained >= trip_to_end:
#         she_weakned = True
#         break
# diff_of_distance = abs(trip_to_end - total_distance_trained)
# if she_weakned:
#     print(f"You've done a great job running {math.ceil(diff_of_distance)} more kilometers!")
# else:
#     print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(diff_of_distance)} more kilometers")