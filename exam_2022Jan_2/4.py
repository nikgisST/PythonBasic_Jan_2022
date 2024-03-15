N = int(input())
M = int(input())
S = int(input())
number = 0
for every_address_number in range(M, N - 1, -1):
    if every_address_number % 2 == 0 and every_address_number % 3 == 0:
        number = every_address_number
        if number == S:
            break
        else:
            print(f"{every_address_number}", end=" ")
    # elif every_address_number % 2 == 0 and every_address_number % 3 == 0:



