start = input()
end = input()
middle = input()
counter = 0
for first_letter in range(ord(start), (ord(end) + 1)):
    if first_letter == ord(middle):
        continue
    for second_letter in range(ord(start), (ord(end) + 1)):
        if second_letter == ord(middle):
            continue
        for third_letter in range(ord(start), (ord(end) + 1)):
            if third_letter == ord(middle):
                continue
            counter += 1
            print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}", end=" ")
print(f"{counter}")


# for first_letter in range(97, 122 + 1):
#     if ord(middle) == first_letter:
#         continue
#     for second_letter in range(97, 122 + 1):
#         if ord(middle) == first_letter:
#             continue
#         for third_letter in range(97, 122 + 1):
#             if ord(middle) == first_letter:
#                 continue
#             print(f"{str(first_letter)}{str(second_letter)}{str(third_letter)}")


# for first_letter in range(int(start), int(end) + 1):
#     if ord(middle) == first_letter:
#         continue
#     for second_letter in range(int(start), int(end) + 1):
#         if ord(middle) == first_letter:
#             continue
#         for third_letter in range(int(start), int(end) + 1):
#             if ord(middle) == first_letter:
#                 continue
#             print(f"{first_letter}{second_letter}{third_letter}")
#
