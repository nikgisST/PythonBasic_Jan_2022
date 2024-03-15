x_height_of_the_house = float(input())
y_length_of_the_side = float(input())
h_height_of_a_triangle_side_roof = float(input())
price_green_walls = 3.4
price_red_walls = 4.3

side_walls = x_height_of_the_house * y_length_of_the_side
windows = 1.5 * 1.5
both_wall_1_without_window = 2 * side_walls - 2 * windows
back_wall = x_height_of_the_house * x_height_of_the_house
door = 1.2 * 2
both_front_and_back_walls = 2 * back_wall - door

total_sum_walls = both_wall_1_without_window + both_front_and_back_walls
liters_green_paint = total_sum_walls / price_green_walls

both_rectangle_roof_sides = 2 * (x_height_of_the_house * y_length_of_the_side)
both_triangles = 2 * (x_height_of_the_house * h_height_of_a_triangle_side_roof / 2)

total_sum_roof = both_rectangle_roof_sides + both_triangles
liters_red_paint = total_sum_roof / price_red_walls
print(f"{liters_green_paint:.2f}")
print(f"{liters_red_paint:.2f}")