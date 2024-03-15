start = int(input())
end = int(input())
# 2345
s1 = start // 1000 % 10
s2 = start // 100 % 10
s3 = start // 10 % 10
s4 = start % 10
# 6789
e1 = end // 1000 % 10
e2 = end // 100 % 10
e3 = end // 10 % 10
e4 = end % 10
for i in range(s1, e1 + 1):
    if i % 2 == 0:
        continue
    for j in range(s2, e2 + 1):
        if j % 2 == 0:
            continue
        for k in range(s3, e3 + 1):
            if k % 2 == 0:
                continue
            for l in range(s4, e4 + 1):
                if l % 2 == 0:
                    continue
                print(f"{i}{j}{k}{l}", end=" ")


start = int(input())
end = int(input())
# 2345
s1 = start // 1000 % 10
s2 = start // 100 % 10
s3 = start // 10 % 10
s4 = start % 10
# 6789
e1 = end // 1000 % 10
e2 = end // 100 % 10
e3 = end // 10 % 10
e4 = end % 10
for i in range(s1, e1 + 1):
    for j in range(s2, e2 + 1):
        for k in range(s3, e3 + 1):
            for l in range(s4, e4 + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    print(f"{i}{j}{k}{l}", end=" ")


start = int(input())
end = int(input())
str_start = str(start)
str_end = str(end)
for i in range(int(str_start[0]), int(str_end[0]) + 1):
    if i % 2 == 0:
        continue
    for j in range(int(str_start[1]), int(str_end[1]) + 1):
        if j % 2 == 0:
            continue
        for k in range(int(str_start[2]), int(str_end[2]) + 1):
            if k % 2 == 0:
                continue
            for l in range(int(str_start[3]), int(str_end[3]) + 1):
                if l % 2 == 0:
                    continue
                print(f'{i}{j}{k}{l}', end=' ')