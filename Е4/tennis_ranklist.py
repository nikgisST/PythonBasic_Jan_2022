import math

tournaments = int(input())
start_points = int(input())
final_points = 0
w_points = 0
f_points = 0
sf_points = 0
wins = 0
for i in range(tournaments):
    current_stage = input()
    if current_stage == "W":
        w_points += 2000
        wins += 1
    elif current_stage == "F":
        f_points += 1200
    elif current_stage == "SF":
        sf_points += 720
final_points += start_points + sf_points + f_points + w_points
average_points = (w_points + f_points + sf_points) / tournaments
percent_of_wins = wins / tournaments * 100
print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percent_of_wins:.2f}%")


# import math
#
# tournaments = int(input())
# start_points = int(input())
# final_points = 0
# w_points = 0
# f_points = 0
# sf_points = 0
# wins = 0
# for i in range(tournaments):
#     current_stage = input()
#     if current_stage == "W":
#         w_points += 2000
#         final_points += 2000
#         wins += 1
#     elif current_stage == "F":
#         f_points += 1200
#         final_points += 1200
#     elif current_stage == "SF":
#         sf_points += 720
#         final_points += 720
# final_points += start_points
# average_points = (w_points + f_points + sf_points) / tournaments
# percent_of_wins = wins / tournaments * 100
# print(f"Final points: {final_points}")
# print(f"Average points: {math.floor(average_points)}")
# print(f"{percent_of_wins:.2f}%")




# import math
#
# tournaments = int(input())
# start_points = int(input())
# final_points = 0
# w_points = 0
# f_points = 0
# sf_points = 0
# wins = 0
# w_times = 0
# f_times = 0
# sf_times = 0
# for i in range(tournaments):
#     current_stage = input()
#     if current_stage == "W":
#         w_points = 2000
#         final_points += w_points
#         wins += 1
#         w_times += 1
#     elif current_stage == "F":
#         f_points = 1200
#         final_points += f_points
#         f_times += 1
#     elif current_stage == "SF":
#         sf_points = 720
#         sf_times += 1
#         final_points += sf_points
# final_points += start_points
# average_points = (w_points * w_times + f_points * f_times + sf_points * sf_times) / tournaments
# percent_of_wins = wins / tournaments * 100
# print(f"Final points: {final_points}")
# print(f"Average points: {math.floor(average_points)}")
# print(f"{percent_of_wins:.2f}%")

