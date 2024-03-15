# import sys
#
# number = int(input())
# counter = 0
# max_diff = - sys.maxsize
# for pairs in range(0, number):
#     pair_1 = int(input())
#     pair_2 = int(input())
#     sum = pair_1 + pair_2
#     counter += 1
#     if sum == number:
#         value = sum
#         print(f"Yes, value = {value}")
#     elif sum != number:
#         if number > max_diff:
#             max_diff = number
#             max_diff = number - sum
#             print(f"No, maxdiff = {max_diff}")
import sys

number = int(input())
sum_a = 0
sum_b = 0
sum = 0
max_diff = -sys.maxsize
for i in range(0, number):
    pair_1 = int(input())
    pair_2 = int(input())
    sum_a = pair_1 + pair_2
    if i == 0:
        diff = sum_a
    else:
        diff = abs(sum_a - sum_b)
        if diff > max_diff:
            max_diff = diff
    sum = sum_b
    sum_b = sum_a
if max_diff == 0 or i == 0:
    if i == 0:
        print(f"Yes, value={sum_a}")
    else:
        print(f"Yes, value={sum}")
else:
    print(f"No, maxdiff={abs(max_diff)}")
