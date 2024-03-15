men = int(input())
women = int(input())
max_count_tables = int(input())
# ticket = 1
free_seats = 0
couples = ""
all_seats = max_count_tables // 2
while free_seats < all_seats:
    for man in range(1, men + 1):
        for woman in range(1, women + 1):
           free_seats += 1
           couples += f"({man} <-> {woman}) "
           if free_seats == max_count_tables:
               break
        if free_seats == max_count_tables:
            break
    break
print(f"{couples}", end="")



men = int(input())
women = int(input())
max_count_tables = int(input())
# ticket = 1
counter = 0
couples = ""
# all_seats = 2 * max_count_tables
#while free_seats < all_seats:
for man in range(1, men + 1):
    for woman in range(1, women + 1):
        counter += 1
        couples += f"({man} <-> {woman}) "
        if counter == max_count_tables:
            break
    if counter == max_count_tables:
        break
print(f"{couples}", end="")



mans = int(input())
womans = int(input())
tables = int(input())
counting_tables = 0
for m in range (1, mans + 1):
    for w in range (1, womans + 1):
        counting_tables += 1
        if counting_tables <= tables:
            print (f"({m} <-> {w})", end = " ")
        else:
            break