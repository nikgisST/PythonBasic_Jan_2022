# count_of_numbers = int(input())
# sum_of_all_elements = 0
# max_number = ""
# for number in range(0, count_of_numbers):
#     current_number = int(input())
#     if number == 0:
#         max_number = current_number
#     sum_of_all_elements += current_number
#     if current_number > max_number:
#         max_number = current_number
# if max_number == sum_of_all_elements - max_number:
#     print("Yes")
#     print(f"Sum = {max_number}")
# else:
#     print("No")
#     difference = abs(max_number - (sum_of_all_elements - max_number))
#     print(f"Diff = {difference}")
#
import sys

count_of_numbers = int(input())
sum_of_all_elements = 0
max_number = - sys.maxsize
for number in range(count_of_numbers):
    current_number = int(input())
    sum_of_all_elements += current_number
    if current_number > max_number:
        max_number = current_number
if max_number == sum_of_all_elements - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    difference = abs(max_number - (sum_of_all_elements - max_number))
    print(f"Diff = {difference}")