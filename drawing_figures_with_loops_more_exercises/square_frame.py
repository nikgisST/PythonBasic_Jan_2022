number = int(input())
result = "+ " + (number - 2) * "- " + "+"
print(result)
for rows in range(0, number - 2):
  result_2 = "| " + (number - 2) * "- " + "|"
  print(result_2)
print(result)


number = int(input())
count = 0
while count < number:
    count += 1
    if count == 1 or count == number:
        start_end = "+ " + (number - 2) * "- " + "+"
        print(start_end)
    else:
        middle = "| " + (number - 2) * "- " + "|"
        print(middle)

