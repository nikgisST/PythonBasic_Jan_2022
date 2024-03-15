k = int(input())
l = int(input())
m = int(input())
n = int(input())
first_of_number = 0
second_of_number = 0
counter = 0
limited_substitutions = False
for first_number in range(k, 8 + 1):
    if first_number % 2 == 0:
        for second_number in range(9, l - 1, -1):
            if second_number % 2 != 0:
                first_of_number = str(f"{first_number}{second_number}")
                for third_number in range(m, 8 + 1):
                    if limited_substitutions:
                        break
                    if third_number % 2 == 0:
                        for fourth_number in range(9, n - 1, -1):
                            if fourth_number % 2 != 0:
                                second_of_number = str(f"{third_number}{fourth_number}")
                                if second_of_number != first_of_number:
                                    print(f"{first_of_number} - {second_of_number}")
                                    counter += 1
                                    if counter >= 6:
                                        limited_substitutions = True
                                        break
                                else:
                                    print("Cannot change the same player.")

# invalid_change = False
# K = int(input())
# L = int(input())
# M = int(input())
# N = int(input())
# counter = 0
# for first_digit_first_number in range(K, 8 + 1, 2):
#     for second_digit_first_number in range(9, L + 1, -1):
#         if second_digit_first_number % 2 == 1:
#             continue
#         for first_digit_second_number in range(M, 8 + 1, 2):
#             for second_digit_second_number in range(9, N + 1, -1):
#                 if second_digit_second_number % 2 == 1:
#                     continue
#                 counter += 1
#                 #invalid_change = False
#                 if first_digit_first_number == first_digit_second_number or second_digit_first_number == second_digit_second_number:
#                     invalid_change = True
#                 if counter > 6:
#                     #invalid_change = True
#                     break
# if not invalid_change and counter <= 6:
#     print(f"{K}{L} - {M}{N}")
# elif invalid_change and counter <= 6:
#     print("Cannot change the same player.")

# k = int(input())
# l = int(input())
# m = int(input())
# n = int(input())
# count_subs = 0
# for first in range(k, 8 + 1, + 1):
#     for second in range(9, l - 1, - 1):
#         for third in range(m, 8 + 1, + 1):
#             for forth in range(9, n - 1, - 1):
#                 if first % 2 == 0 and third % 2 == 0 and second % 2 != 0 and forth % 2 != 0:
#                     if first == third and second == forth:
#                         print('Cannot change the same player.')
#                     else:
#                         print(f'{first}{second} - {third}{forth}')
#                         count_subs += 1
#                 if count_subs == 6:
#                     break
#             if count_subs == 6:
#                 break
#         if count_subs == 6:
#             break
#     if count_subs == 6:
#         break



