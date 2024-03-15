n = int(input())
sum = 0
for current_number in range(1, n + 1):
    every_number = int(input())
    sum += every_number
average = sum / n
print(f"{average:.2f}")
