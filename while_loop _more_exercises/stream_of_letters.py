command = input()
count_c = 0
count_o = 0
count_n = 0
word = ""
c_has_expired = False
o_has_expired = False
n_has_expired = False
new_word = False
while command != "End":
    if 65 <= ord(command) <= 90 or 97 <= ord(command) <= 122:
        if command == "c":
            count_c += 1
            if count_c == 1:
                c_has_expired = True
            elif count_c > 1:
                word += command
        elif command == "o":
            count_o += 1
            if count_o == 1:
                o_has_expired = True
            elif count_o > 1:
                word += command
        elif command == "n":
            count_n += 1
            if count_n == 1:
                n_has_expired = True
            elif count_n > 1:
                word += command
        else:
            word += command
    if c_has_expired and o_has_expired and n_has_expired:
        new_word = True
        print(word, end=" ")
    if new_word:
        word = ""
        c_has_expired = False
        o_has_expired = False
        n_has_expired = False
        count_c = 0
        count_o = 0
        count_n = 0
        new_word = False
    command = input()











#
# command = input()
# count_c = 0
# count_o = 0
# count_n = 0
# word = ""
# while command != "End":
#     must_be_added = False
#     if 65 <= ord(command) <= 90 or 97 <= ord(command) <= 122:
#         if command == "c":
#             if count_c >= 1:
#                 word += command
#             else:
#                 count_c += 1
#         elif command == "o":
#             if count_o >= 1:
#                 word += command
#             else:
#                 count_o += 1
#         if command == "n":
#             if count_n >= 1:
#                 word += command
#             else:
#                 count_n += 1
#         else:
#             word += command
#         if count_c >= 1 and count_o >= 1 and count_n >= 1:
#             print(f"{word}", end=" ")
#             word = ""
#             count_c = 0
#             count_n = 0
#             count_o = 0
#     command = input()
#
#
# command = input()
# c_counter = 0
# o_counter = 0
# n_counter = 0
# word = ""
# while command != "End":
#     mustBeAdded = False
#     if 65 <= ord(command) <= 90 or 97 <= ord(command) <= 122:
#         if command == "c":
#             if c_counter >= 1:
#                 word += command
#             else:
#                 c_counter += 1
#         elif command == "o":
#             if o_counter >= 1:
#                 word += command
#             else:
#                 o_counter += 1
#         elif command == "n":
#             if n_counter >= 1:
#                 word += command
#             else:
#                 n_counter += 1
#         else:
#             word += command
#         if c_counter >= 1 and o_counter >= 1 and n_counter >= 1:
#             print(f"{word}", end=" ")
#             word = ""
#             c_counter = 0
#             o_counter = 0
#             n_counter = 0
#
#
#
#
#
#
# symbol_is = input()
# count_c = 0
# count_o = 0
# count_n = 0
# word = ""
# c_has_expired = False
# o_has_expired = False
# n_has_expired = False
# new_word = False
# while symbol_is != "End":
#     if c_has_expired and o_has_expired and n_has_expired:
#         new_word = True
#         print(word, end=" ")
#     if new_word:
#         word = ""
#         c_has_expired = False
#         o_has_expired = False
#         n_has_expired = False
#         count_c = 0
#         count_o = 0
#         count_n = 0
#         new_word = False
#     if symbol_is == "c":
#         count_c += 1
#         if count_c == 1:
#             c_has_expired = True
#         elif count_c > 1:
#             word += symbol_is
#     elif symbol_is == "o":
#         count_o += 1
#         if count_o == 1:
#             o_has_expired = True
#         elif count_o > 1:
#             word += symbol_is
#     elif symbol_is == "n":
#         count_n += 1
#         if count_n == 1:
#             n_has_expired = True
#         elif count_n > 1:
#             word += symbol_is
#     else:
#         word += symbol_is
#
#
#
#
# command = input()
# counter_c = 0
# counter_o = 0
# counter_n = 0
# word = ""
# while command != "End":
#     letter = command
#     if letter == "c":
#         counter_c += 1
#         if counter_c == 1:
#             command = input()
#             continue
#         elif counter_c > 1:
#             word += letter
#     elif letter == "o":
#         counter_o += 1
#         if counter_o == 1:
#             command = input()
#             continue
#         elif counter_o > 1:
#             word += letter
#     elif letter == "n":
#         counter_n += 1
#         if counter_n == 1:
#             command = input()
#             continue
#         elif counter_n > 1:
#             word += letter
#     if counter_n == 1 and counter_o == 1 and counter_o == 1:
#         print(word, end=" ")
#     if letter == "End":
#         break
#     word += letter
#     command = input()
# print(word)
#
#
#
#
#

# line = input()
# asci_code = ''
# con_times = 0
# c_times = 0
# o_times = 0
# n_times = 0
# print_space = 0
# main_word = ''
# additional_word = ''
# while line != 'End':
#     asci_code = ord(line)
#     if (65 <= asci_code <= 90 or 97 <= asci_code <= 122) and asci_code != 99 and asci_code != 110 and asci_code != 111:
#         additional_word += line
#     elif asci_code == 99 and c_times > 0:
#         additional_word += line
#     elif asci_code == 99:
#         c_times += 1
#         con_times += 1
#         print_space += 1
#     elif asci_code == 110 and n_times > 0:
#         additional_word += line
#     elif asci_code == 110:
#         n_times += 1
#         con_times += 1
#         print_space += 1
#     elif asci_code == 111 and o_times > 0:
#         additional_word += line
#     elif asci_code == 111:
#         o_times += 1
#         con_times += 1
#         print_space += 1
#     if print_space == 3:
#         additional_word += ' '
#         print_space = 0
#     if con_times == 3:
#         c_times = 0
#         o_times = 0
#         n_times = 0
#         con_times = 0
#         main_word += additional_word
#         additional_word = ''
#     line = input()
# print(main_word)



# command = []
# secret = ''
# entry = ''
# while entry != 'End':
#     entry = input()
#     if not entry.isalpha():
#         continue
#     if (entry == 'c' or entry == 'o' or entry == 'n') and entry not in command:
#         command.append(entry)
#         entry = ''
#     if 'c' in command and 'o' in command and 'n' in command:
#         print(f'{secret}', end=' ')
#         secret = ''
#         command = []
#     else:
#         secret += entry




# c_count = 0
# o_count = 0
# n_count = 0
# message = ""
# while True:
#     letter = input()
#     if letter == "End":
#         break
#     if letter == "c" and c_count == 0:
#         c_count += 1
#     elif letter == "o" and o_count == 0:
#         o_count += 1
#     elif letter == "n" and n_count == 0:
#         n_count += 1
#     else:
#         if letter.isalpha():
#             message += letter
#     if c_count == 1 and o_count == 1 and n_count == 1:
#         print(f"{message} ",end = "")
#         message = ""
#         c_count = 0
#         o_count = 0
#         n_count = 0
