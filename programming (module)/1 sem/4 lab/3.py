import random as rnd
lst = []
for i in range(10):
    lst.append(rnd.randint(0, 10))
print(lst)
print(lst[::-1])
