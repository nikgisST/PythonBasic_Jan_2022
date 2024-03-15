count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegetarian_menu = int(input())
chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
delivery_price = 2.50
total_sum = count_chicken_menu * chicken_menu_price + \
      count_fish_menu * fish_menu_price + \
      count_vegetarian_menu * vegetarian_menu_price
dessert_price = total_sum * 20 / 100
final_price = total_sum + dessert_price + delivery_price
print(final_price)
