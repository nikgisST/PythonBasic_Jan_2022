count_rolls_paper = int(input())
count_rolls_plat = int(input())
glue_liters = float(input())
percent_discount = int(input())
rolls_paper_price = 5.80
plat_price = 7.20
glue_price = 1.20
price_1 = count_rolls_paper * rolls_paper_price
price_2 = count_rolls_plat * plat_price
price_3 = glue_liters * glue_price
total_price = price_3 + price_2 + price_1
final_price = total_price - (percent_discount / 100 * total_price)
print(f"{final_price:.3f}")