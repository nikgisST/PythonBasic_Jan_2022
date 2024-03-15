import math

balls_in_the_box = int(input())
points = 0
total_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_color = 0
times = 0

for i in range(balls_in_the_box):
    color = input()
    if color == "red":
        red_balls += 1
        points += 5
    elif color == "orange":
        orange_balls += 1
        points += 10
    elif color == "yellow":
        yellow_balls += 1
        points += 15
    elif color == "white":
        white_balls += 1
        points += 20
    elif color == "black":
        black_balls += 1
        points = math.floor(total_points / 2)
        # times += 1                            #брой пъти,които точките са / на 2 съвпата == с брой пъти хващане на черна топка
    else:
        other_color += 1
    total_points = points

print(f"Total points: {total_points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_color}")
print(f"Divides from black balls: {black_balls}")    #{times}





# import math
#
# balls_in_the_box = int(input())
# color = input()
# points = 0
# red_balls = 0
# orange_balls = 0
# yellow_balls = 0
# white_balls = 0
# black_balls = 0
# total_points = 0
# other_colors_picked = 0
# times = 0
# for i in range(1, balls_in_the_box + 1):
#     color = input()
#     if color == "red":
#         points += 5
#         red_balls += 1
#     elif color == "orange":
#         points += 10
#         orange_balls += 1
#     elif color == "yellow":
#         points += 15
#         yellow_balls += 1
#     elif color == "white":
#         points += 20
#         white_balls += 1
#     elif color == "black":
#         black_balls += 1
#         points = total_points / 2
#         times += 1
#     else:
#         other_colors_picked += 1
#     total_points = points
# total_points = math.floor(total_points)
# # times = points // black_balls
# print(f"Total points: {total_points:.0f}")
# print(f"Red balls: {red_balls}")
# print(f"Red balls: {orange_balls}")
# print(f"Red balls: {yellow_balls}")
# print(f"Red balls: {white_balls}")
# print(f"Other colors picked: {other_colors_picked}")
# print(f"Divides from black balls: {times}")