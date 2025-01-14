import random as rnd
lst = []
for i in range(100):
    num = rnd.randint(1, 10000)
    if num % 7 == 0 and num % 3:
        lst.append(num)
    elif num % 9:
        lst.append(num)

print(lst)

i = input()