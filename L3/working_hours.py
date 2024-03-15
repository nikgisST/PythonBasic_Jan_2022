hour = int(input())
day = input()
is_working_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday"\
               or day == "Friday" or day == "Saturday"
if hour >= 10 and hour <= 18:
    if is_working_day:
        print("open")
if day == "Sunday"or hour < 10 or hour > 18:
    print("closed")

hour = int(input())
day = input()
not_working_day = day == "Sunday"
is_working_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" or\
                 day == "Thursday" or day == "Friday" or day == "Saturday"
if not_working_day:
    if 10 > hour > 18:
        print("closed")
    else:
        print("closed")
elif is_working_day:
    if 10 <= hour <= 18:
        print("open")
    else:
        print("closed")

# hour = int(input())
# day = input()
# if day == "Sunday":
#     if 10 > hour > 18:
#         print("closed")
#     else:
#         print("closed")
# elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
#     if 10 <= hour <= 18:
#         print("open")
#     else:
#         print("closed")