number_excursions_see = int(input())
number_excursions_mountain = int(input())
price_see = 680
price_mountain = 499
total_price = 0
unavailable_packet = False
command = ""
while command != "Stop":
    command = input()
    name_packet = command
    if name_packet == "sea":
        if number_excursions_see == 0:
            continue
        total_price += price_see
        number_excursions_see -= 1
    elif name_packet == "mountain":
        if number_excursions_mountain == 0:
            continue
        total_price += price_mountain
        number_excursions_mountain -= 1
    if number_excursions_see == 0 and number_excursions_mountain == 0:
        unavailable_packet = True
        break
if unavailable_packet:                         #if number_excursions_see == 0 and number_excursions_mountain == 0:
    print(f"Good job! Everything is sold.")
print(f"Profit: {total_price} leva.")



# num_trip_to_sea = int(input())
# num_trip_to_mountain = int(input())
# command = input()
# count_paket_for_sea = num_trip_to_sea
# count_paket_for_mountain = num_trip_to_mountain
# sea = 680
# mountin = 499
# win_sea = 0
# win_mountain = 0
# total_win = 0
# name_paket = input()
# while command != "Stop":
#     if name_paket == "Sea":
#         win_sea = 680
#         count_paket_for_sea = count_paket_for_sea - 1
#     elif name_paket == "mountain":
#         win_mountain = 499
#         count_paket_for_mountain = count_paket_for_mountain - 1
#     total_win = win_sea + win_mountain
#     if command == "Stop":
#         break
#     if count_paket_for_sea <= 0:
#         break
#     elif count_paket_for_mountain <= 0:
#         break
#     name_paket = input()
# if count_paket_for_sea == 0:
#     print(f"Good job! Everything is sold.")
#     print(f"Profit: {total_win} leva.")
# else:
#     print(f"Profit: {total_win} leva.")


# sea_counter = int(input())
# mountain_counter = int(input())
# my_choise_for_this_weekend_is = input()
# sea_price = 680
# mountain_price = 499
# total_profit = 0
# sea_travel_unavaible_yet = False
# mountain_travel_unavaible_yet = False
# you_have_sold_everything = False
# while my_choise_for_this_weekend_is != "Stop":
#     if sea_travel_unavaible_yet and mountain_travel_unavaible_yet:
#         you_have_sold_everything = True
#         break
#     if my_choise_for_this_weekend_is == "sea":
#         if sea_travel_unavaible_yet:
#             my_choise_for_this_weekend_is = input()
#             continue
#         sea_counter -= 1
#         total_profit += sea_price
#         if sea_counter == 0:
#             sea_travel_unavaible_yet = True
#     elif my_choise_for_this_weekend_is == "mountain":
#         if mountain_travel_unavaible_yet:
#             my_choise_for_this_weekend_is = input()
#             continue
#         mountain_counter -= 1
#         total_profit += mountain_price
#         if mountain_counter == 0:
#             mountain_travel_unavaible_yet = True
#     my_choise_for_this_weekend_is = input()
# if you_have_sold_everything:
#     print("Good job! Everything is sold.")
# print(f"Profit: {total_profit} leva.")