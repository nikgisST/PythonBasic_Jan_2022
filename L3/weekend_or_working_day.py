day = input()
is_working_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or \
                 day == "Friday"
is_weekend = day == "Saturday" or day == "Sunday"
if is_working_day:
    print("Working day")
elif is_weekend:
    print("Weekend")
else:
    print("Error")

# day = input()
# if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or \
#         day == "Friday":
#     print("Working day")
# elif day == "Saturday" or day == "Sunday":
#     print("Weekend")
# else:
#     print("Error")



# day = input()
# if day == "Monday":
#     print("Working day")
# elif day == "Tuesday":
#     print("Working day")
# elif day == "Wednesday":
#     print("Working day")
# elif day == "Thursday":
#     print("Working day")
# elif day == "Friday":
#     print("Working day")
# elif day == "Saturday":
#     print("Weekend")
# elif day == "Sunday":
#     print("Weekend")
# else:
#     print("Error")

