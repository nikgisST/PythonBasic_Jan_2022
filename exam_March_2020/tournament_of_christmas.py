days = int(input())
#sport = input()
wins = 0
total_money = 0
you_are_the_winner = False
final_money = 0
total_wins = 0
total_lose = 0
for each_day in range(1, days + 1):
    # if each_day > 1:
    sport = input()
    total_money = 0
    counter_win = 0
    counter_lose = 0
    while sport != "Finish":
        text = input()
        if text == "win":
            counter_win += 1
            total_money += 20
        elif text == "lose":
            counter_lose += 1
            #total_money -= 0
        sport = input()
    if counter_win >= counter_lose:
        total_money += 0.10 * total_money
        total_wins += 1
    else:
        total_lose += 1
    # if counter_win == counter_lose:
    #     break
    final_money += total_money
if total_lose <= total_wins:
    final_money += + 0.20 * final_money
    you_are_the_winner = True
if you_are_the_winner:
    print(f"You won the tournament! Total raised money: {final_money:.2f}")
elif not you_are_the_winner:
    print(f"You lost the tournament! Total raised money: {final_money:.2f}")










# days_of_tournament = int(input())
# total_money = 0
# total_wins = 0
# total_lose = 0
# for days in range (days_of_tournament):
#     sport = input()
#     wins = 0
#     losses = 0
#     total_money_for_the_day = 0
#     while sport != "Finish":
#         result = input()
#         if result == "win":
#             total_money_for_the_day += 20
#             wins += 1
#         elif result == "lose":
#             losses += 1
#         sport = input()
#     total_wins += wins
#     total_lose += losses
#     if wins > losses:
#         total_money_for_the_day *= 1.1
#         total_money += total_money_for_the_day
#     elif wins < losses:
#         total_money += total_money_for_the_day
# if total_wins > total_lose:
#     total_money *= 1.2
#     print(f"You won the tournament! Total raised money: {total_money:.2f}")
# elif total_wins < total_lose:
#     print(f"You lost the tournament! Total raised money: {total_money:.2f}")
