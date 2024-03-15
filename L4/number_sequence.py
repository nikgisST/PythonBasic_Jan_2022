import sys

number = int(input())
max_num = - sys.maxsize
min_num = sys.maxsize
for i in range(1, number + 1):           #(0, number)   #(number)
    value = int(input())
    if value > max_num:
        max_num = value
    if value < min_num:
        min_num = value
print(f"Max number: {max_num}")
print(f"Min number: {min_num}")