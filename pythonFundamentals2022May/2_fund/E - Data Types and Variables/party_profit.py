from math import floor

companions = int(input())
days = int(input())
coins = 0
for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        companions -= 2
    if current_day % 15 == 0:
        companions += 5
    if current_day % 3 == 0:
        coins -= companions * 3
    if current_day % 5 == 0:
        coins += companions * 20
        if current_day % 3 == 0:
            coins -= companions * 2
    coins += 50
    coins -= companions * 2
coins_per_companion = floor(coins / companions)   # int()  # //
print(f"{companions} companions received {coins_per_companion} coins each.")


from math import floor

companions = int(input())
days = int(input())
coins = 0
for current_day in range(1, days + 1):
    coins += 50
    if current_day % 10 == 0:
        companions -= 2
    if current_day % 15 == 0:
        companions += 5
    coins -= companions * 2
    if current_day % 3 == 0:
        coins -= companions * 3
    if current_day % 5 == 0:
        coins += companions * 20
        if current_day % 3 == 0:
            coins -= companions * 2
coins_per_companion = floor(coins / companions)   # int()  # //
print(f"{companions} companions received {coins_per_companion} coins each.")
