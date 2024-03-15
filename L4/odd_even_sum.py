number = int(input())
# i = 1 -> 10           # Първата позиция е четно, ако range(0, number) =0, а ако range(1, number + 1) първата позиция е нечетна =1
# i = 2 -> 50
# i = 3 -> 60
# i = 4 -> 20
even_sum = 0
odd_sum = 0
for i in range(0, number):              #(number)     #(1, number + 1)
    current_num = int(input())
    if i % 2 == 0:
        even_sum += current_num
    elif i % 2 == 1:
        odd_sum += current_num
if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
elif not even_sum == odd_sum:
    diff = abs(even_sum - odd_sum)
    print("No")
    print(f"Diff = {diff}")
