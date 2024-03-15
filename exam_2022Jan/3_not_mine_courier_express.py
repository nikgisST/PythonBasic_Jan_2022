weight = float(input())
type_of_service = input()
distance = int(input())
price_delivery = 0
total = 0
overprice = 0
sum = 0
if type_of_service == "standard":
    if weight < 1:
        #price_delivery_1 = 3
        sum = 0.03 * distance
    elif weight <= 10:
        #price_delivery_2 = 5
        sum = 0.05 * distance
    elif weight <= 40:
        #price_delivery_3 = 10
        sum = 0.10 * distance
    elif weight <= 90:
        #price_delivery_4 = 15
        sum = 0.15 * distance
    elif weight <= 150:
        #price_delivery_5 = 20
        sum = 0.20 * distance
elif type_of_service == "express":
    if weight < 1:
        #price_delivery_1 = 3
        sum = 0.03 * distance
        price_delivery = 0.03 * 0.80
    elif weight <= 10:
        #price_delivery_2 = 5
        sum = 0.05 * distance
        price_delivery = 0.05 * 0.40
    elif weight <= 40:
        #price_delivery_3 = 10
        sum = 0.10 * distance
        price_delivery = 0.10 * 0.05
    elif weight <= 90:
        #price_delivery_4 = 15
        sum = 0.15 * distance
        price_delivery = 0.15 * 0.02
    elif weight <= 150:
        #price_delivery_5 = 20
        sum = 0.20 * distance
        price_delivery = 0.20 * 0.01
overprice = weight * price_delivery
total = distance * overprice + sum
print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total / 100:.2f} lv.")



# weight = float(input())
# _type = input()
# distance = int(input())
# # standard rate per km in 0.00 lv
# rate = 0
# if weight < 1:
#     rate = 0.03
# elif weight < 10:
#     rate = 0.05
# elif weight < 40:
#     rate = 0.1
# elif weight < 90:
#     rate = 0.15
# elif weight < 150:
#     rate = 0.2
# total = distance * rate
# if _type == "express":
#     if weight < 1:
#         total += (0.8 * rate) * distance * weight
#     elif weight < 10:
#         total += (0.4 * rate) * distance * weight
#     elif weight < 40:
#         total += (0.05 * rate) * distance * weight
#     elif weight < 90:
#         total += (0.02 * rate) * distance * weight
#     elif weight < 150:
#         total += (0.01 * rate) * distance * weight
# print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total:.2f} lv.")
