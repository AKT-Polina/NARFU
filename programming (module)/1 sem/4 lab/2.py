a = int(input("Введите первый член арифметической прогрессии: "))
p = int(input("Введите разность арифметической прогрессии: "))
prog = []
for i in range(10):
    a -= p
    prog.append(a)

print(prog)
