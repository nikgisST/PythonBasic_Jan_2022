count_of_open_tabs = int(input())
salary = int(input())                #или с float, в условието не е пояснено --> #Заплата - число в интервала [500...1500]
penalty = 0
no_money_left = False                         # Ако не искам с булеви, този ред е излишен
for tabs in range(count_of_open_tabs):
    apps = input()                          # Винаги въвеждам тук променливата, която проверявам
    if apps == "Facebook":
        penalty = 150
        salary -= penalty
    elif apps == "Instagram":
        penalty = 100
        salary -= penalty
    elif apps == "Reddit":
        penalty = 50
        salary -= penalty
    else:
        penalty = 0
        salary -= penalty
    if salary <= 0:
        no_money_left = True                      # Ако не искам с булеви, този ред е излишен
        break
if no_money_left == True:                          #if salary <= 0:
    print("You have lost your salary.")
else:
    print(int(salary))

