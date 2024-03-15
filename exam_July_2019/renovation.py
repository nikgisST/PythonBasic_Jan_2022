from math import ceil

height = int(input())
width = int(input())
percent = int(input())
command = input()
area = height * width * 4
area -= area * percent / 100
area = ceil(area)
all_is_painted = False
while command != "Tired!":
    litters_paint = int(command)
    area -= litters_paint
    if area <= 0:
        all_is_painted = True
        break
    command = input()
if command == "Tired!":
    print(f"{area} quadratic m left.")
elif area < 0:
    print(f"All walls are painted and you have {abs(area)} l paint left!")
elif area >= 0:
    print(f"All walls are painted! Great job, Pesho!")


from math import ceil

height_wall = int(input())
width_wall = int(input())
windows_percent = int(input())
tired = True
all_done = False
command = input()
area = height_wall * width_wall * 4
walls_painted = area - area * windows_percent / 100
walls_painted = ceil(walls_painted)
while command != "Tired!":
    litters_painting = int(command)
    walls_painted -= litters_painting
    if walls_painted < 0:
        tired = False
        break
    elif walls_painted == 0:
        tired = False
        all_done = True
        break
    command = input()
if tired:
    print(f"{walls_painted} quadratic m left.")
elif not tired:
    if all_done:
        print("All walls are painted! Great job, Pesho!")
    elif not all_done:
        print(f"All walls are painted and you have {abs(walls_painted)} l paint left!")


import math

height_wall = int(input())
width_wall = int(input())
windows_percent = int(input())
area = height_wall * width_wall * 4
walls_painted = area - area * windows_percent / 100
command = input()
while command != "Tired!":
    litters_painting = int(command)
    walls_painted -= litters_painting
    if walls_painted <= 0:
        break
    command = input()
if command == "Tired!":
    print(f"{math.ceil(walls_painted)} quadratic m left.")          #f"{walls_painted:.0f}
elif walls_painted < 0:
    print(f"All walls are painted and you have {math.ceil(abs(walls_painted))} l paint left!")  #{abs(walls_painted):.0f}
elif walls_painted >= 0:
    print("All walls are painted! Great job, Pesho!")