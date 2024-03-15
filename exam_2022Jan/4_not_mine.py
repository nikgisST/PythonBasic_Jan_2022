count_student = int(input())
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
sum = 0
total_evaluations = 0
for current_student in range(1, count_student + 1):
    exam_grade = float(input())
    sum += exam_grade
    total_evaluations += 1                # колкото са броя студенти, но все пак да броим колко оценки се въртят
    if 2 <= exam_grade < 3:
        count_1 += 1
        #sum += exam_grade
    elif exam_grade < 4:
        count_2 += 1
        #sum += exam_grade
    elif exam_grade < 5:
        count_3 += 1
        #sum += exam_grade
    elif exam_grade >= 5:
        count_4 += 1
        #sum += exam_grade
percent_1 = count_1 / count_student * 100
percent_2 = count_2 / count_student * 100
percent_3 = count_3 / count_student * 100
percent_4 = count_4 / count_student * 100
average = sum / total_evaluations
print(f"Top students: {percent_4:.2f}%")
print(f"Between 4.00 and 4.99: {percent_3:.2f}%")
print(f"Between 3.00 and 3.99: {percent_2:.2f}%")
print(f"Fail: {percent_1:.2f}%")
print(f"Average: {average:.2f}")



