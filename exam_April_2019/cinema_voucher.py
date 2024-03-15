voucher_sum = int(input())
ticket_counter = 0
goods_counter = 0
spend_money = 0
while voucher_sum > 0:
    goods = input()
    if goods == "End":
        break
    else:
        if len(goods) > 8:                                       #checking if lenght is more than 8 letters
            spend_money = ord(goods[0]) + ord(goods[1])
            if spend_money > voucher_sum:
                break
            voucher_sum -= spend_money
            ticket_counter += 1
        elif len(goods) <= 8:
            spend_money = ord(goods[0])
            if spend_money > voucher_sum:
                break
            voucher_sum -= spend_money
            goods_counter += 1
print(f"{ticket_counter}")
print(f"{goods_counter}")


voucher_value = int(input())
command = input()
price = 0
items_bought = 0
tickets_bought = 0
total_sum = 0
while command != "End":
    len_command = len(command)
    first_letter = command[0]
    second_letter = command[1]
    first_digit = ord(first_letter)
    second_digit = ord(second_letter)
    if len_command > 8:
        price = first_digit + second_digit
        if price > voucher_value:
            break
        tickets_bought += 1
    else:
        price = first_digit
        if price > voucher_value:
            break
        items_bought += 1
    voucher_value -= price
    command = input()
print(tickets_bought)
print(items_bought)