f = open('1.txt','r') # открыnm файл на запись
lines = f.readlines()
print("Считанные числа: ",lines)
#print("Второе число",a)
a = int(lines[0])
b = int(lines[1])
print("Сумма чисел: ", (a+b))
f.close() # закрыть файл
r = open('2.txt','w')
r.write(str(a+b))
