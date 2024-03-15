bag_capacity = float(input())
put_more_bags = 0
command = input()
bag_volume = 0
increasing_bag_size = 0
while command != "End":
    bag_volume = float(command)
    increasing_bag_size += 1
    if (increasing_bag_size) % 3 == 0:
        bag_volume = bag_volume + 0.10 * bag_volume
    if bag_volume > bag_capacity:
        break
    put_more_bags += 1                           # ред 6 и 7 бяха на ред 10 и 11, а ред 7 и 8 бяха на ред 10 и 11

    bag_capacity -= bag_volume
    command = input()
if command == "End" or bag_volume <= bag_capacity:
    print("Congratulations! All suitcases are loaded!")
elif bag_volume > bag_capacity or command != "End":
    print("No more space!")
print(f"Statistic: {put_more_bags} suitcases loaded.")


full_capacity = float(input())
command = input()
counting = 0
capacity_full = False
total_bags = 0
while command != "End":
    capacity = float(command)
    counting += 1
    if counting % 3 == 0:
        capacity = capacity * 1.1
    full_capacity -= capacity
    if full_capacity <= 0:
        capacity_full = True
        break
    else:
        total_bags += 1
    command = input()
if capacity_full:
    print("No more space!")
    print(f"Statistic: {total_bags} suitcases loaded.")
else:
    print("Congratulations! All suitcases are loaded!")
    print(f"Statistic: {total_bags} suitcases loaded.")


# bag_capacity = float(input())
# total_bag_space = 0
# counter = 0
# command = input()
# while command != "End":
#     bag_volume = float(command)
#     if (counter + 1) % 3 == 0:
#         bag_volume *= 1.1
#     total_bag_space += bag_volume
#     if bag_capacity < total_bag_space:
#         break
#     if total_bag_space == bag_capacity:
#         counter += 1
#         break
#     counter += 1
#     command = input()
# if bag_capacity < total_bag_space:
#     print("No more space!")
# elif bag_capacity >= total_bag_space:
#     print("Congratulations! All suitcases are loaded!")
# print(f"Statistic: {counter} suitcases loaded.")
