import sys

number = int(input())
sum = 0
# max_number = - sys.maxsize
# min_number = sys.maxsize
even_sum = 0
odd_sum = 0
min_odd_number = sys.maxsize                       # Тези са с сус мин и сус макс
max_odd_number = - sys.maxsize
min_even_number = sys.maxsize
max_even_number = - sys.maxsize
#no_min_max_number = False
for i in range(1, number + 1):
    current_number = float(input())
    if i % 2 == 1:
        odd_sum += current_number                  # Щом ми трябва сума, събирам текущите числа, не е брояч, че да увеличавам с 1!
        if current_number > max_odd_number:
            max_odd_number = current_number
        if current_number < min_odd_number:
            min_odd_number = current_number
    elif i % 2 == 0:
        even_sum += current_number
        if current_number > max_even_number:
            max_even_number = current_number
        if current_number < min_even_number:
            min_even_number = current_number
if number == 0:                                 #числата на четни и нечетни позиции (броим от 1). 1 e нечетно ДА ТУК!
    print(f"OddSum={odd_sum:.2f},")
    print("OddMin=No,")
    print("OddMax=No,")
else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={min_odd_number:.2f},")
    print(f"OddMax={max_odd_number:.2f},")
if number == 0 or number == 1:               #number <= 1   #числата на четни и нечетни позиции (броим от 1). 1 e четно НЕ ТУК!
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
else:
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={min_even_number:.2f},")
    print(f"EvenMax={max_even_number:.2f}")

    # if n == 0:
    #     print('OddSum=0.00,\nOddMin=No,\nOddMax=No,')
    # else:
    #     print(f'OddSum={oddSum:.2f},\nOddMin={oddMin:.2f},\nOddMax={oddMax:.2f},')
    #
    # if n <= 1:
    #     print(f'EvenSum=0.00,\nEvenMin=No,\nEvenMax=No')
    # else:
    #     print(f'EvenSum={evenSum:.2f},\nEvenMin={evenMin:.2f},\nEvenMax={evenMax:.2f}')

