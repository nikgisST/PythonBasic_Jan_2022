length = float(input())
width = float(input())
#3 <= width <= length <= 100
length_cm = length * 100
width_cm = width * 100
hall_cm = 100
door = 1
chair = 2
length_of_working_place = 70
width_of_working_place = 120
number_of_working_places = door + chair

width_without_hall_cm = width_cm - hall_cm
desks = width_without_hall_cm // length_of_working_place
rest_desks_space = width_without_hall_cm % length_of_working_place

rows = length_cm // width_of_working_place
rest_rows_space = length_cm % width_of_working_place

total_places = rows * desks - number_of_working_places
print(f"{total_places}")                                      #print(int(total_places))     
