start = int(input())
end = int(input())
for barcode in range(start, end + 1):
    start_as_string = str(start)
    end_as_string = str(end)
    is_valid_barcode = True
    barcode_as_str = str(barcode)
    for index, digit in enumerate(barcode_as_str):
        if int(digit) % 2 == 0:
            is_valid_barcode = False
            break
        if int(digit) < int(start_as_string[index]):
            is_valid_barcode = False
            break
        if int(digit) > int(end_as_string[index]):
            is_valid_barcode = False
            break
    if is_valid_barcode:
        print(barcode, end=' ')


# start_number = input()
# end_number = input()
# start_number_first_digit = int(start_number[0])
# start_number_second_digit = int(start_number[1])
# start_number_third_digit = int(start_number[2])
# start_number_forth_digit = int(start_number[3])
# end_number_first_digit = int(end_number[0])
# end_number_second_digit = int(end_number[1])
# end_number_third_digit = int(end_number[2])
# end_number_forth_digit = int(end_number[3])
# for first_digit in range(start_number_first_digit, end_number_first_digit + 1):
#     for second_digit in range(start_number_second_digit, end_number_second_digit + 1):
#         for third_digit in range(start_number_third_digit, end_number_third_digit + 1):
#             for forth_digit in range(start_number_forth_digit, end_number_forth_digit + 1):
#                 if first_digit %2 ==0 or second_digit %2 ==0 or third_digit %2 ==0 or forth_digit %2 ==0:
#                     continue
#                 print(f"{first_digit}{second_digit}{third_digit}{forth_digit}", end = " ")


# start_number = int(input())
# end_number = int(input())
# is_odd = False
# for current_number in range(start_number, end_number + 1):
#     current_number_as_string = str(current_number)
#     for index, digit in enumerate(current_number_as_string):
#         if int(digit) % 2 == 1:
#             is_odd = True
#         elif int(digit) % 2 == 0:
#             is_odd = False
#             break
#         if is_odd:
#             print(current_number)
#         current_number += 1

# for current_digit in current_number_as_string:
#     if int(current_digit) % 2 == 1:
#         is_odd = True
#     elif int(current_number) % 2 == 0:
#         is_odd = False
#         break
# if is_odd:
#     print(current_number)


# start_number = int(input())
# end_number = int(input())
# edinici_start = start_number % 10
# if edinici_start % 2 == 0:
#     edinici_start += 1
# desetici_start = (start_number//10)%10
# if desetici_start % 2 == 0:
#     desetici_start += 1
# stotici_start = (start_number//100)%10
# if stotici_start % 2 == 0:
#     stotici_start += 1
# hilqdni_start = (start_number//1000)%10
# if hilqdni_start % 2 == 0:
#     hilqdni_start += 1
# edinici_end = end_number % 10
# if edinici_end % 2 == 0:
#     edinici_end -= 1
# desetici_end = (end_number//10)%10
# if desetici_end % 2 == 0:
#     desetici_end -= 1
# stotici_end = (end_number//100)%10
# if stotici_end % 2 == 0:
#     stotici_end -= 1
# hilqdni_end = (end_number//1000)%10
# if hilqdni_end % 2 == 0:
#     hilqdni_end -= 1
# for h in range (hilqdni_start, hilqdni_end + 1, 2):
#     for s in range (stotici_start , stotici_end + 1, 2):
#         for d in range (desetici_start , desetici_end + 1, 2):
#             for e in range (edinici_start, edinici_end + 1, 2):
#                 print(f"{h}{s}{d}{e}", end = " ")
