upper_boundary_first_number = int(input())
upper_boundary_second_number = int(input())
upper_boundary_third_number = int(input())
for number_1 in range(2, upper_boundary_first_number + 1, 2):
    for number_2 in range(2, upper_boundary_second_number + 1):
        for number_3 in range(2, upper_boundary_third_number + 1, 2):
            if number_2 == 2 or number_2 == 3 or number_2 == 5 or number_2 == 7:
                print(f"{number_1} {number_2} {number_3}")


first_number = int(input())
second_number = int(input())
third_number = int(input())
for f in range(1, first_number + 1):
    if f % 2 == 0:
        for s in range(1, second_number + 1):
            if s == 2 or s == 3 or s == 5 or s == 7:
                for t in range(1, third_number + 1):
                    if t % 2 == 0:
                        print(f"{f} {s} {t}")

upper_limit_first_number = int(input())
upper_limit_second_number = int(input())
upper_limit_third_number = int(input())
for first_number in range(2, upper_limit_first_number + 1, 2):
    for second_number in range(2, upper_limit_second_number + 1):
        non_prime_number = True
        for number in range(2, second_number):
            if second_number % number == 0:
                non_prime_number = False
                break
        if second_number == 2 or non_prime_number:
            for third_number in range(2, upper_limit_third_number + 1, 2):
                print(f"{first_number} {second_number} {third_number}")
