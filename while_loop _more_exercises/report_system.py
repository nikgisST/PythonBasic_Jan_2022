expected_sum = int(input())
credit_card = 0
cash = 0
common_counter = 0
total_sum = 0
counter_credit_card = 0
counter_cash = 0
command = ""
while total_sum < expected_sum:
    command = input()
    if command == "End":
        break
    price = int(command)
    common_counter += 1
    if common_counter % 2 == 1:       # първо е плащане в брой
        if price > 100:
            print("Error in transaction!")
        elif price <= 100:
            cash += price
            counter_cash += 1
            print("Product sold!")
    elif common_counter % 2 == 0:      # след това е плащане с кредитна карта
        if price < 10:
            print("Error in transaction!")
        elif price >= 10:
            credit_card += price
            counter_credit_card += 1
            print("Product sold!")
    total_sum = credit_card + cash
if total_sum >= expected_sum or command != "End":
    print(f'Average CS: {cash / counter_cash:.2f}')
    print(f'Average CC: {credit_card / counter_credit_card:.2f}')
if command == "End" or total_sum < expected_sum:
    print("Failed to collect required money for charity.")



# expected_sum = int(input())
# common_counter = 0
# command = input()
# price = 0
# # method_to_pay = ""
# cash = 0
# credit_card = 0
# counter_cash = 0
# counter_credit_card = 0
# while command != "End":
#     price = int(command)
#     common_counter += 1
#     if common_counter % 2 == 1:
#         # method_to_pay = "Cash"
#         if price > 100:
#             print("Error in transaction!")
#         elif price <= 100:
#             expected_sum -= price
#             cash += price
#             counter_cash += 1
#             print("Product sold!")
#     elif common_counter % 2 == 0:
#         # method_to_pay = "Card"
#         if price < 10:
#             print("Error in transaction!")
#         if price >= 10:
#             expected_sum -= price
#             credit_card += price
#             counter_credit_card += 1
#             print("Product sold!")
#     if expected_sum <= 0:
#         break
#     elif expected_sum > 0:
#         command = input()
# if expected_sum <= 0 or command != "End":
#     print(f"Average CS: {cash / counter_cash:.2f}")
#     print(f"Average CC: {credit_card / counter_credit_card:.2f}")
# if command == "End" or expected_sum > 0:                 #else:
#     print("Failed to collect required money for charity.")