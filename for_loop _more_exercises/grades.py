students = int(input())
grade_1 = 0
grade_2 = 0
grade_3 = 0
grade_4 = 0
sum = 0
value_grades = 0
for current_grade in range(0, students):
    grades = float(input())
    value_grades += grades                    # СЪБИРА СТОЙНОСТИТЕ НА ВСИЧКИ ОЦЕНКИ !!!!
    sum += 1
    if 2 <= grades < 3:        #if grades < 3:            # Минава, но ако няма горна граница някой път може да гръмна !!
        grade_1 += 1
    elif 3 <= grades < 4:      #elif grades < 4:
        grade_2 += 1
    elif 4 <= grades < 5:      #elif grades < 5:
        grade_3 += 1
    elif grades >= 5:
        grade_4 += 1
percent_1 = grade_1 / sum * 100
percent_2 = grade_2 / sum * 100
percent_3 = grade_3 / sum * 100
percent_4 = grade_4 / sum * 100
average_grade = (value_grades) / students
print(f"Top students: {percent_4:.2f}%")
print(f"Between 4.00 and 4.99: {percent_3:.2f}%")
print(f"Between 3.00 and 3.99: {percent_2:.2f}%")
print(f"Fail: {percent_1:.2f}%")
print(f"Average: {average_grade:.2f}")

