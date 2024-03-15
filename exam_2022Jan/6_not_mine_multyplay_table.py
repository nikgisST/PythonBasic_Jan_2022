number = int(input())  # Трицифрено число положително
s_1 = number // 100 % 10
s_2 = number // 10 % 10
s_3 = number % 10
for i in range(1, s_3 + 1):
    for j in range(1, s_2 + 1):
        for k in range(1, s_1 + 1):
            print(f"{i} * {j} * {k} = {(i * j * k)};")

input_number = int(input())
first_start_num = input_number // 100 % 10
second_start_num = input_number // 10 % 10
third_start_num = input_number // 1 % 10
for i in range(1, third_start_num + 1):
    for j in range(1, second_start_num + 1):
        for k in range(1, first_start_num + 1):
            print(f"{i} * {j} * {k} = {i * j * k};")

number = int(input())
n3 = number // 100 % 10
n2 = number // 10 % 10
n1 = number % 10
for i in range(n1 + 1):
    for j in range(n2 + 1):
        for k in range(n3 + 1):
            if i <= 0 or j <= 0 or k <= 0:
                continue
            print(f"{i} * {j} * {k} = {i * j * k};")