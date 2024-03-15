goal = 10000
total_steps = 0
while total_steps < goal:
    her_steps = input()
    if her_steps == "Going home":
        last_steps = int(input())
        total_steps += last_steps
        break
    her_steps = int(her_steps)                      #current_steps = int(her_steps)
    total_steps += her_steps                        #total_steps += her_steps
difference = abs(total_steps - goal)
if total_steps >= goal:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
elif total_steps < goal:
    print(f"{difference}  more steps to reach goal.")