# number = int(input())
# if -100 <= number <= 100 and number != 0:
#     print("Yes")
# else:
#     print("No")

number = int(input())
if number >= -100:
    if number <= 100:
        if number != 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")


# number = int(input())
# if number >= -100 and number <= 100 and number != 0:
#     print("Yes")
# else:
#     print("No")