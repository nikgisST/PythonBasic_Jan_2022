deposit = float(input())
months = int(input())
i = float(input())
annual_interest = deposit * i / 100
monthly_interest = annual_interest / 12
total_sum = deposit + months * monthly_interest
print(total_sum)
