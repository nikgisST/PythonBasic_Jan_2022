command = input()
upper_letter = []
for i in range(len(command)):
    if command[i].isupper():
        upper_letter.append(i)
print(upper_letter)