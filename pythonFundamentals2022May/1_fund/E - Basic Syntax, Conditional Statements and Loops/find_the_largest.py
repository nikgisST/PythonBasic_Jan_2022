# import sys
#
# number = int(input())
# string_number = str(number)
# max_number = - sys.maxsize
# current_number = number
# for current_digit in range(len(string_number)):
#     if int(string_number[current_digit]) > max_number:
#         max_number = int(string_number[current_digit])
#         new_string = str(max_number)
# print(new_string)

number = input()
sorted_number = sorted(number, reverse=True)     #reverse = True стават по низходящ ред
for index in range(len(number)):
    print(sorted_number[index], end='')



number = input()
sorted_number = sorted(number, reverse=True)
print(''.join(sorted_number))