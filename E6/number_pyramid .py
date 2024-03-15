number = int(input())
counter = 0
for row in range(1, number + 1):              # ВЪНШЕН ЦИКЪЛ
    for columns in range(1, row + 1):
        counter += 1
        if counter > number:
            break
        print(f"{counter}", end=" ")
    print()                                   # ВЕЧЕ СМЕ ВЪВ ВЪНШНИЯ ЦИКЪЛ - НОВ РЕД, ДЕФИНИРАН В НАЧАЛОТО МУ
    if counter > number:                      # ВЪНШЕН ЦИКЪЛ
        break                                 # ВЪНШЕН ЦИКЪЛ
    #print()                                  # МОЖЕ ДА ПРЕНЕСЕМ НА НОВ РЕД И В КРАЯ НА ВЪНШНИЯ ЦИКЪЛ

number = int(input())
counter = 1
#all_is_printed = False
for row in range(1, number + 1):
    for columns in range(1, row + 1):
        print(counter, end= " ")
        counter += 1
        if counter > number:
            #all_is_printed = True
            break
    if counter > number:                  #if all_is_printed:
        break
    print()

