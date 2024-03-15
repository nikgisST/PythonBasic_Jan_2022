last_sector = input()
row_first_sector = int(input())
odd_row = int(input())
counter = 0
start_sector = "A"
start_seat = "a"
even_row = 0
for sector in range(ord(start_sector), ord(last_sector) + 1):
    for row in range(1, row_first_sector + 1):
        if row % 2 == 1:
            odd_row = odd_row
            end_row_odd = ord(start_seat) + odd_row
            for seats in range(ord(start_seat), end_row_odd ):
                print(f'{chr(sector)}{row}{chr(seats)}')
                counter += 1
        elif row % 2 == 0:
            even_row = odd_row + 2
            end_row_even = ord(start_seat) + even_row
            for seats in range(ord(start_seat), end_row_even ):
                print(f'{chr(sector)}{row}{chr(seats)}')
                counter += 1
    if row_first_sector + 1 > row_first_sector:
        row_first_sector += 1
print(counter)



#         row_first_sector += 1
#         even_row += 2
#         for seat in range(97, 122 + 1):
#             counter += 1
# print(f"{chr(sector)}{row}{chr(seat)}{counter}")



