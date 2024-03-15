command = input()
is_voldemort = False
while command != "Welcome!":
    if command == "Voldemort":
        is_voldemort = True
        break
    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6:
        print(f"{command} goes to Hufflepuff.")
    command = input()
if is_voldemort:
    print(f"You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")


command = ''
name_char = ''
while command != 'Welcome!':
    command = input()
    name_char = len(command)
    if command == 'Welcome!':
        break
    if command == 'Voldemort':
        break
    if name_char < 5:
        print(f'{command} goes to Gryffindor.')
    elif name_char == 5:
        print(f'{command} goes to Slytherin.')
    elif name_char == 6:
        print(f'{command} goes to Ravenclaw.')
    else:
        print(f'{command} goes to Hufflepuff.')
if command == 'Voldemort':
    print('You must not speak of that name!')
else:
    print('Welcome to Hogwarts.')