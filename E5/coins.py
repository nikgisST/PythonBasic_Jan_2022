# current_sum = float(input())
# current_sum = int(current_sum * 100)
# coins_counter = 0
# coins_counter += current_sum // 200
# current_sum %= 200
# coins_counter += current_sum // 100
# current_sum %= 100
# coins_counter += current_sum // 50
# current_sum %= 50
# coins_counter += current_sum // 20
# current_sum %= 20
# coins_counter += current_sum // 10
# current_sum %= 10
# coins_counter += current_sum // 5
# current_sum %= 5
# coins_counter += current_sum // 2
# current_sum %= 2
# coins_counter += current_sum // 1
# current_sum %= 1
# print(coins_counter)

money = float(input())
coins = 0
current_sum = 0
current_sum = round(money * 100, 2)
while current_sum > 0:                #while True:
    if current_sum // 200:            #while current_sum //
        coins += 1
        current_sum -= 200
    elif current_sum // 100:          #while current_sum //
        coins += 1
        current_sum -= 100
    elif current_sum // 50:           #while current_sum //
        coins += 1
        current_sum -= 50
    elif current_sum // 20:           #while current_sum //
        coins += 1
        current_sum -= 20
    elif current_sum // 10:           #while current_sum //
        coins += 1
        current_sum -= 10
    elif current_sum // 5:            #while current_sum //
        coins += 1
        current_sum -= 5
    elif current_sum // 2:            #while current_sum //
        coins += 1
        current_sum -= 2
    elif current_sum // 1:            #while current_sum //
        coins += 1
        current_sum -= 1
    # if current_sum <= 0:            #elif current_sum <= 0     #while current_sum <= 0:
    #     break
print(coins)

