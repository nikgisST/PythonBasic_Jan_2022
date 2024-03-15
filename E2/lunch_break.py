import math

name_of_series = input()
episode_duration = int(input())
rest_duration = int(input())
time_for_lunch = rest_duration / 8
time_for_chill = rest_duration / 4
left_rest_duration = rest_duration - (time_for_lunch + time_for_chill)
needed_time = math.ceil(abs(episode_duration - left_rest_duration))
#free_time = math.ceil(free_time)
if left_rest_duration >= episode_duration:
    print(f"You have enough time to watch {name_of_series} and left with {needed_time} minutes free time.")
elif left_rest_duration < episode_duration:
    print(f"You don't have enough time to watch {name_of_series}, you need {needed_time} more minutes.")