fav_book = input()
current_book = input()
counter = 0
while current_book != fav_book:
    counter += 1
    if current_book == "No More Books":
        counter -= 1
        break
    current_book = input()
if current_book != fav_book:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")                          #counter - 1, защото "No More Books" не е книга, а команда
elif current_book == fav_book:
    print(f"You checked {counter} books and found it.")
#
#
# fav_book = input()
# counter = 0
# book_is_found = False
# current_book = input()
# while current_book != "No More Books":           #current_book != fav_book
#     if current_book == fav_book:
#         book_is_found = True
#         break
#     counter += 1
#     current_book = input()
# if book_is_found:                         #if book_is_found == True    #if book_is_found is True    #current_book == fav_book
#     print(f"You checked {counter} books and found it.")
# elif not book_is_found:                        #else:
#     print("The book you search is not here!")
#     print(f"You checked {counter} books.")


# searched_book = input()
# book_counter = 0
# next_book = input()
# while next_book != "No More Books" and next_book != searched_book:
#     book_counter += 1
#     next_book = input()
# if next_book == searched_book:
#     print(f"You checked {book_counter} books and found it.")
# else:
#     print("The book you search is not here!")    #print("The book you search is not here!\nYou checked {book_counter} books.")
#     print(f"You checked {book_counter} books.")
#
#
# searched_book = input()
# book_counter = 0
# no_more_books = False
# next_book = input()
# while next_book != searched_book:
#     if next_book == "No More Books":
#         no_more_books = True
#         break
#     book_counter += 1
#     next_book = input()
# if no_more_books:
#     print("The book you search is not here!")
#     print(f"You checked {book_counter} books.")
# else:
#     print(f"You checked {book_counter} books and found it.")
#
#
