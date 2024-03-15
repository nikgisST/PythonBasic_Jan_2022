name_airline = str(input())
count_tickets_for_old_people = int(input())
count_tickets_for_kids = int(input())
n_price_for_old_people = float(input())
fee = float(input())
n_price_for_kids = n_price_for_old_people - n_price_for_old_people * 0.70
price_tickets_old_fee = fee + n_price_for_old_people
price_tickets_for_kids_with_fee = fee + n_price_for_kids
total_sum = count_tickets_for_kids * price_tickets_for_kids_with_fee + count_tickets_for_old_people * price_tickets_old_fee
profit = total_sum * 0.20
print(f"The profit of your agency from {name_airline} tickets is {profit:.2f} lv.")