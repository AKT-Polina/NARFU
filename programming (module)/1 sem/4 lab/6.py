import random as rnd
lst = []
for i in range(10):
    lst.append(rnd.randint(0, 1000))
print(lst)
print("Чётные числа:")
for i in lst:
    if i % 2 == 0:
        print(i, ", ", end = '')
print()
print("Числа заканчивающиеся нулём:")
for i in lst:
    if i % 10 == 0:
        print(i, ", ", end = '')
