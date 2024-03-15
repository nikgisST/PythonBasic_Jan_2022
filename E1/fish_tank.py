length = int(input())
width = int(input())
height = int(input())
percent = float(input())
volume_cm = length * width * height
volume_dm = volume_cm * 0.001     # volume_cm / 1000
liters_water = volume_dm * (1 - percent / 100)
print(liters_water)