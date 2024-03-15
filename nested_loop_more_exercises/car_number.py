start = int(input())
end = int(input())
for first_number in range(start, end + 1):
    if first_number % 2 == 0:
        pass
    elif first_number % 2 == 1:
        pass
    for second_number in range(start, end + 1):
        for third_number in range(start, end + 1):
            sum_1 = second_number + third_number
            if sum_1 % 2 == 1:
                continue
            for forth_number in range(start, end + 1):
                if first_number % 2 == 0 and forth_number % 2 == 1 and first_number > forth_number:
                    print(f"{first_number}{second_number}{third_number}{forth_number}", end=" ")
                elif first_number % 2 == 1 and forth_number % 2 == 0 and first_number > forth_number:
                    print(f"{first_number}{second_number}{third_number}{forth_number}", end=" ")