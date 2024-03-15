number = int(input())
#valid = 100 <= number <= 200 or number == 0
if not (100 <= number <= 200 or number == 0):
    print("invalid")

number = int(input())
is_range = number >= 100 and number <= 200
is_zero = number == 0
valid = is_range or is_zero
if not valid:
    print("invalid")


number = int(input())
valid = number >= 100 and number <= 200 or number == 0
if not valid:
    print("invalid")


number = int(input())
valid = 100 <= number <= 200 or number == 0
if not valid:
    print("invalid")