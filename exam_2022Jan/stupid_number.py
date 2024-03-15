number = int(input())
is_valid = False
for i in range(2, number):
    if number % i == 0:
        break
    else:
        is_valid = True
if is_valid:
    print(f"{number} is similar")
else:
    print(f"{number} is not similar")