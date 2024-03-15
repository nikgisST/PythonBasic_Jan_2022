number = int(input())
for current_number in range(number):
    given_number = int(input())
    if given_number == 88:
        print("Hello")
    elif given_number == 86:
        print("How are you?")
    elif given_number != 88 and given_number != 86 and given_number < 88:
        print("GREAT!")
    elif given_number > 88:
        print("Bye.")
