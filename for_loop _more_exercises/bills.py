month = int(input())
bill_water = 20
bill_wifi = 15
average_cost = 0
total_bill_electricity = 0
total_bill_water = 0
total_bill_wifi = 0
total_others = 0
for every_month in range(0, month):
    bill_electricity = float(input())
    total_bill_electricity += bill_electricity
    total_bill_water = month * bill_water
    total_bill_wifi = month * bill_wifi
    others = (bill_wifi + bill_water + bill_electricity) + 0.20 * (bill_wifi + bill_water + bill_electricity)
    total_others += others
    average_cost = (total_bill_electricity + total_bill_water + total_bill_wifi + total_others) / month
print(f"Electricity: {total_bill_electricity:.2f} lv")
print(f"Water: {total_bill_water:.2f} lv")
print(f"Internet: {total_bill_wifi:.2f} lv")
print(f"Other: {total_others:.2f} lv")
print(f"Average: {average_cost:.2f} lv")
