import math

width = float(input())
length = float(input())
height = float(input())
middle_height_astronauts = float(input())
volume = 0
volume = width * length * height
volume_one_room = (middle_height_astronauts + 0.40) * 2 * 2
astronauts = math.floor(volume / volume_one_room)
if astronauts < 3:
    print(f"The spacecraft is too small.")
if 3 <= astronauts <= 10:
    print(f"The spacecraft holds {astronauts} astronauts.")
elif astronauts > 10:
    print(f"The spacecraft is too big.")


