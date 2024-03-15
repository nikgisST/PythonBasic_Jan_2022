import math

n = int(input())
print(math.factorial(n))



n = int(input())
sum = 1
for i in range(1, n + 1):
    sum *= i
print(sum)



n = int(input())
sum = 1
while n > 1:            #while True:
    sum = sum * n
    n = n - 1
    if n <= 1:         #if not n > 1:
        break
print(sum)


