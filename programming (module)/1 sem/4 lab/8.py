import random as rnd
lst = []
for i in range(10):
    lst.append(rnd.randint(0, 10))
print(lst)

c = 0
count = 0
for i in lst:
    for j in lst:
        if i == j:
            c += 1
    if c > 1:
        count += 1
    c = 0
print("Количество различных элментов:", count)
