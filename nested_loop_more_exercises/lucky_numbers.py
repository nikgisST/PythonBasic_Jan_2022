n = int(input())
digit_1 = 0
digit_2 = 0
digit_3 = 0
digit_4 = 0
is_lucky_number = False
for current_first_number in range(1, 9 + 1):
    digit_1 = current_first_number
    for current_second_number in range(1, 9 + 1):
        digit_2 = current_second_number
        sum_1 = digit_1 + digit_2
        for current_third_number in range(1, 9 + 1):
            digit_3 = current_third_number
            for current_forth_number in range(1, 9 + 1):
                digit_4 = current_forth_number
                sum_2 = digit_3 + digit_4
                if sum_1 == sum_2 and n % sum_1 == 0:
                    is_lucky_number = True
                    print(f"{digit_1}{digit_2}{digit_3}{digit_4}", end=" ")



