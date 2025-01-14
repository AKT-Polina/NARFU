lst = [38, 41, 42, 45, 45, 43, 42, 39]
c = 0
print("Размеры участников команды:")
for i in lst:
    for j in lst:
        if i == j:
            c += 1
    if c < 2:
        print(i)
    c = 0

