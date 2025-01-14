import math
def f(x, y):
    z1 = math.sin(x + 1) - y -1.2
    z2 = 2 * x + math.cos(y) - 2
    print("z1 = ", z1)
    print("z2 = ", z2)

x = int(input("Введите x: "))
y = int(input("Введите y: "))
f(x, y)
i = input()