quantity_food = int(input())
total_food = 0
quantity_food = quantity_food * 1000
command = input()
while command != "Adopted":
    food = int(command)
    total_food += food
    # if total_food > quantity_food:
    #     break
    command = input()
diff = abs(total_food - quantity_food)
if quantity_food >= total_food:
    print(f"Food is enough! Leftovers: {diff} grams.")
elif quantity_food < total_food:
    print(f"Food is not enough. You need {diff} grams more.")
