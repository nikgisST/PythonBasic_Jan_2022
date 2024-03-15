name = input()
average_grade = 0
year = 1
times_counter = 0
yearly_grades = 0
while year <= 12:
    if times_counter > 1:
        break
    current_grade = float(input())
    if current_grade < 4:
        year = year
        times_counter += 1
    elif current_grade >= 4:
        year += 1
        yearly_grades += current_grade
        average_grade = yearly_grades / (year - 1)
if (year - 1) == 12:                                                      #if year == 13    #if times_counter <= 1:
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
if times_counter > 1:                                                                       #elif times_counter > 1:
    print(f"{name} has been excluded at {year} grade")

# name = input()
# average_grade = 0
# year = 1
# times_counter = 0
# yearly_grades = 0
# while year <= 12:
#     if times_counter > 1:
#         break
#     current_grade = float(input())
#     if current_grade < 4:
#         year = year
#         times_counter += 1
#     elif current_grade >= 4:
#         year += 1
#         yearly_grades += current_grade
#
# if times_counter <= 1:
#     average_grade = yearly_grades / 12
#     print(f"{name} graduated. Average grade: {average_grade:.2f}")
# elif times_counter > 1:
#     print(f"{name} has been excluded at {year} grade")




# name = input()
# year = 1
# sum = 0
# fail_count = 0
# while year <= 12:
#     if fail_count > 1:
#         break
#     grade = float(input())
#     if grade < 4:
#         fail_count += 1
#         continue
#     sum += grade
#     year += 1
# if fail_count > 1:
#     print(f"{name} has been excluded at {year} grade")
# else:
#     average_grade = sum / (year - 1)
#     print(f"{name} graduated. Average grade: {average_grade:.2f}")
