# number = int(input())
# for power in range(0, number + 1, 2):
#     print(2 ** power)                      # i == power

import math

n = int(input())
for power in range(0, n + 1, 2):
    print(f"{math.pow(2, power):.0f}")
