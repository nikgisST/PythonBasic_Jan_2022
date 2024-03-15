command = input()

while command != "End":
    if command == "SoftUni":
        command = input()
        continue
    for i in range(len(command)):
        print(command[i]*2, end="")

    print(" ")
    command = input()



word = input()
while word != "End":
    new_word = ""
    if word == "SoftUni":
        word = input()
        continue
    else:
        for current_symbol in word:
            new_word += current_symbol * 2
        print(new_word)
    word = input()