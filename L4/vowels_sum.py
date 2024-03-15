text = input()
sum = 0
for letter in text:
    if letter == "a":
        sum += 1
    elif letter == "e":
        sum += 2
    elif letter == "i":
        sum += 3
    elif letter == "o":
        sum += 4
    elif letter == "u":
        sum += 5
print(sum)


# text = input()
# sum = 0
# text_length = len(text)
# for i in range(0, text_length):
#     letter = text[i]
#     if letter == "a":
#         sum += 1
#     elif letter == "e":
#         sum += 2
#     elif letter == "i":
#         sum += 3
#     elif letter == "o":
#         sum += 4
#     elif letter == "u":
#         sum += 5
# print(sum)