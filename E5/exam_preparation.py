unpleased_grades = int(input())
unpleased_grades_counter = 0
count_grades = 0
sum = 0
last_problem = ""
has_failed = True
while unpleased_grades_counter < unpleased_grades:
    command = input()
    if command == "Enough":
        has_failed = False
        break
    current_grade = int(input())
    if current_grade <= 4:
        unpleased_grades_counter += 1
    sum += current_grade
    count_grades += 1
    last_problem = command

if has_failed:
    print(f"You need a break, {unpleased_grades} poor grades.")
else:
    print(f"Average score: {sum / count_grades:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_problem}")

