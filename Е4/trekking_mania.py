count_of_groups = int(input())
total_people = 0
mountain_musala = 0
mountain_mondblan = 0
mountain_kalimandjaro = 0
mountain_k2 = 0
mountain_everest = 0
for number in range(count_of_groups):
    count_of_people = int(input())
    if count_of_people <= 5:
        mountain_musala += count_of_people
    elif count_of_people <= 12:
        mountain_mondblan += count_of_people
    elif count_of_people <= 25:
        mountain_kalimandjaro += count_of_people
    elif count_of_people <= 40:
        mountain_k2 += count_of_people
    elif count_of_people > 40:
        mountain_everest += count_of_people
    total_people += count_of_people
#total_people = mountain_everest + mountain_mondblan + mountain_k2 + mountain_kalimandjaro + mountain_musala
print(f"{mountain_musala / total_people * 100:.2f}%")
print(f"{mountain_mondblan / total_people * 100:.2f}%")
print(f"{mountain_kalimandjaro / total_people * 100:.2f}%")
print(f"{mountain_k2 / total_people * 100:.2f}%")
print(f"{mountain_everest / total_people * 100:.2f}%")