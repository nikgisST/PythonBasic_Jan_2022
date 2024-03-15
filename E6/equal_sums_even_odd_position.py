first_number = int(input())
second_number = int(input())
for current_number in range(first_number, second_number + 1):
    odd_digit_sum = 0
    even_digit_sum = 0
    current_number_as_string = str(current_number)
    for index, digit in enumerate(current_number_as_string):
        if index % 2 == 0:
            odd_digit_sum += int(digit)
        elif index % 2 == 1:
            even_digit_sum += int(digit)
    if odd_digit_sum == even_digit_sum:
        print(current_number_as_string, end= " ")

# start = input()
# end = input()
# for i in range(int(start), int(end) + 1):
#     to_string = str(i)
#     length_string = len(to_string)
#     even_sum = 0
#     odd_sum = 0
#     for digit in range(0, length_string):
#         if digit % 2 ==0:
#             even_sum += int(to_string[digit])
#         else:
#             odd_sum += int(to_string[digit])
#     if even_sum == odd_sum:
#         print(i, end= " ")