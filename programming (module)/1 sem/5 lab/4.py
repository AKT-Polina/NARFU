import random as rnd
def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False
        
l1 = []
l2 = []

for i in range(10):
    l1.append(rnd.randint(0,100))
    l2.append(rnd.randint(0,100))
print(l1)
print("Чётные числа из первого списка: ")
for i in l1:
    if is_even(i):
        print(i)
print(l2)
print("Нечётные числа из второго списка: ")
for i in l2:
    if not is_even(i):
        print(i)
i = input()