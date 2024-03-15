a1 = int(input())
a2 = int(input())
n = int(input())
for symbol_1 in range(a1, a2):                   # от а1 до а2-1
    for symbol_2 in range(1, n):                 # от 1 до n-1
        for symbol_3 in range(1,  n // 2):       # от 1 до (n/2)-1   #for symbol_3 in range(1, int(n / 2)):
            sum = symbol_1 + symbol_2 + symbol_3
            if sum % 2 == 1 and symbol_1 % 2 == 1:
                print(f"{chr(symbol_1)}-{symbol_2}{symbol_3}{symbol_1}")



a1 = int(input())
a2 = int(input())
n = int(input())
symbol_2_end = n - 1
symbol_3_end = n // 2 - 1
for symbol_1 in range(a1, a2):
    if symbol_1 % 2 == 1:
        ascii_table = chr(symbol_1)
    for symbol_2 in range(1, symbol_2_end + 1):
        for symbol_3 in range(1, symbol_3_end + 1):
            sum = symbol_2 + symbol_3 + symbol_1
            if sum % 2 != 0 and symbol_1 % 2 != 0:
                print(f"{ascii_table}-{symbol_2}{symbol_3}{symbol_1}")