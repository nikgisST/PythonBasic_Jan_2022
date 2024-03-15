count_of_goods = int(input())
price_minibus = 0
price_truck = 0
price_train = 0
tons_minibus = 0
tons_truck = 0
tons_train = 0
for current_good in range(0, count_of_goods):
    tons = int(input())
    if tons <= 3:
        price_minibus = 200
        tons_minibus += tons
    elif tons <= 11:
        price_truck = 175
        tons_truck += tons
    elif tons >= 12:                      # ПРИ 12 И ПОВЕЧЕЕЕЕЕ >= !!!!!!!!!!!!
        price_train = 120
        tons_train += tons
total_tons = tons_minibus + tons_truck + tons_train
average_price = (price_minibus * tons_minibus + price_truck * tons_truck + price_train * tons_train) / total_tons
percent_tons_minibus = tons_minibus / total_tons * 100
percent_tons_truck = tons_truck / total_tons * 100
percent_tons_train = tons_train / total_tons * 100
print(f"{average_price:.2f}")
print(f"{percent_tons_minibus:.2f}%")
print(f"{percent_tons_truck:.2f}%")
print(f"{percent_tons_train:.2f}%")




