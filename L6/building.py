floors = int(input())
rooms = int(input())
for f in range(floors, 0, -1):
    for r in range(0, rooms):
        if f == floors:
            print(f"L{f}{r}", end= " ")                    #name = input()
        elif f % 2 == 0:                                   # print("Hello, ", end= "")
            print(f"O{f}{r}", end= " ")                    # print(name, end= "")
        elif f % 2 != 0:                                   # print("!")
            print(f"A{f}{r}", end=" ")                            # ИМА ИНТЕРВАЛ В END=" ", защото иначе се долепят !!!!!!
    print()


