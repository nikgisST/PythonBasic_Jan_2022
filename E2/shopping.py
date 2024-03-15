budget = float(input())
count_video_cards = int(input())
count_processor = int(input())
count_RAM_memory = int(input())
video_cards_price = 250
purchased_video_cards = count_video_cards * video_cards_price
processor_price = 0.35 * purchased_video_cards
RAM_memory_price = 0.10 * purchased_video_cards
total_price = purchased_video_cards + count_processor * processor_price + count_RAM_memory * RAM_memory_price
if count_video_cards > count_processor:
    discount = total_price * 0.15
else: #elif count_video_cards <= count_processor:
    discount = 0
needed_money = total_price - discount
difference = abs(needed_money - budget)
if needed_money <= budget:
    print(f"You have {difference:.2f} leva left!")
else: #elif needed_money > budget:
    print(f"Not enough money! You need {difference:.2f} leva more!")