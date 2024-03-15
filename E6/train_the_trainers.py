jury = int(input())
presentation = input()
average_student_grade = 0
counter = 0
sum = 0
while presentation != "Finish":
    grade = 0
    for degree in range(0, jury):
        grade += float(input())
    average_student_grade = grade / jury
    print(f"{presentation} - {average_student_grade:.2f}.")
    sum += average_student_grade
    counter += 1
    presentation = input()
total_average_grade = sum / counter
print(f"Student's final assessment is {total_average_grade:.2f}.")



