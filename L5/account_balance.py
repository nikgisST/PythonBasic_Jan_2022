command = input()
total_sum = 0
while command != "NoMoreMoney":
    money = float(command)
    if money < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {money:.2f}")
    total_sum += money
    command = input()
# print(f"Total: {total_sum:.2f}")
print("Total: " + str(f"{total_sum:.2f}"))            #print("Total: " + str(round(total_sum, 2))) НЕ Е ВЯРНО С ROUND!!!!!!!

