price_bachelorette_party = float(input())
count_love_message = int(input())
count_wax_roses = int(input())
count_keychains = int(input())
count_caricatures = int(input())
count_lucky_surprice = int(input())
price_love_message = 0.60
price_wax_roses = 7.20
price_keychains = 3.60
price_caricatures = 18.20
price_lucky_surprice = 22
total_sum = count_love_message * price_love_message + count_wax_roses * price_wax_roses + count_keychains * price_keychains + count_caricatures *  price_caricatures + count_lucky_surprice * price_lucky_surprice
total_count = count_love_message + count_wax_roses + count_keychains + count_caricatures + count_lucky_surprice
if total_count >= 25:
    total_sum = total_sum - 0.35 * total_sum
total_sum = total_sum - 0.10 * total_sum
diff = abs(total_sum - price_bachelorette_party)
if total_sum >= price_bachelorette_party:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")






