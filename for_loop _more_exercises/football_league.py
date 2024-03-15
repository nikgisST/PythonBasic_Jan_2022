capacity_stadium = int(input())
fans = int(input())
counter_A = 0
counter_B = 0
counter_V = 0
counter_G = 0
percent_A = 0
percent_B = 0
percent_V = 0
percent_G = 0
total_percent_fans = 0
sum = 0
for every_fan in range(0, fans):                          # от 0 до броя ФЕНОВЕ, а не капацитета
    sector = input()
    if sector == "A":
        counter_A += 1
        percent_A = counter_A / fans * 100
    elif sector == "B":
        counter_B += 1
        percent_B = counter_B / fans * 100
    elif sector == "V":
        counter_V += 1
        percent_V = counter_V / fans * 100
    elif sector == "G":
        counter_G += 1
        percent_G = counter_G / fans * 100
    sum = percent_A + percent_G + percent_B + percent_V
    #sum_rounded = round(sum,2)
    if sum >= 100:          #sum_rounded
        break
    # elif fans > capacity_stadium:
total_percent_fans = fans / capacity_stadium * 100
print(f"{percent_A:.2f}%")
print(f"{percent_B:.2f}%")
print(f"{percent_V:.2f}%")
print(f"{percent_G:.2f}%")
print(f"{total_percent_fans:.2f}%")


# sum = 99.99999999999999999988888888
# sum_rounded = round(sum)
# print(sum)