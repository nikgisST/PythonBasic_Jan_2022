count_locations = int(input())
total_gold = 0
average_gold = 0
for current_location in range(1, count_locations + 1):
    if current_location >= 2 :
        total_gold = 0
    dreaming_average = float(input())
    days = int(input())
    for current_day in range(1, days + 1):
        gold = float(input())
        total_gold += gold
    average_gold = total_gold / days
    if average_gold >= dreaming_average:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    elif average_gold < dreaming_average:
        print(f"You need {(dreaming_average - average_gold):.2f} gold.")
