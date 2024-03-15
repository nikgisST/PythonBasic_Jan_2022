# n = int(input())
# counter = 0
# while counter < n:
#     counter += 1
#     star = " " * (n - counter) + counter * "* "
#     print(star)
#
# counter = n - 1
# while counter > 0:
#     star = " " * (n - counter) + counter * "* "
#     print(star)
#     counter -= 1


n = int(input())
for row in range(1, n + 1):
    print((n - row) * " ", end="")
    print("* ", end="")
    print((row - 1) * ("* "))

for row in range(n - 1, 0, -1):
    print((n - row) * " ", end="")
    print("* ", end="")
    print((row - 1) * ("* "))