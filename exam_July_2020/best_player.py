import sys

name = input()
max_goals = - sys.maxsize
there_is_hat_trick = False
best_player = ""
while name != "END":
    current_goals = int(input())
    if current_goals > max_goals:
        max_goals = current_goals
        best_player = name                     #ЗА ДА НЕ ПРИНТИРА END !!!! ТУК ДЕФИНИРАМЕ ПОСЛЕДНОТО ИМЕЕЕЕЕЕЕ
    if 3 <= current_goals < 10:
        there_is_hat_trick = True
    elif current_goals >= 10:
        there_is_hat_trick = True
        break
    name = input()
print(f"{best_player} is the best player!")
if there_is_hat_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
elif not there_is_hat_trick:
    print(f"He has scored {max_goals} goals.")