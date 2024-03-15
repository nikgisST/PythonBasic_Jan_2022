hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())
time_for_exam = hour_of_exam * 60 + minutes_of_exam
time_for_arrival = hour_of_arrival * 60 + minutes_of_arrival
diff = abs(time_for_arrival - time_for_exam)
if time_for_arrival == time_for_exam:
    print("On time")
elif time_for_arrival > time_for_exam:
    print("Late")
    hours = diff // 60
    minutes = diff % 60
    if diff > 59:
        print(f"{hours}:{minutes:02d} minutes before the start")
    else:
        print(f"{minutes} minutes before the start")
elif time_for_arrival < time_for_exam:
    if diff <= 30:
        print("On time")
        print(f"{diff} minutes before the start")
    else:
        print("Early")
        hours = diff // 60
        minutes = diff % 60
        if diff > 59:
            print(f"{hours}:{minutes:02d} minutes before the start")
        else:
            print(f"{minutes} minutes before the start")
