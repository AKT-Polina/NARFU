f = open('3.txt','r', encoding="utf-8") # открыnm файл на запись
lines = f.readlines()
#lines = lines.split('\n')
#print("Количество английских символов: ",lines)
print("Первая строка: ", lines[0])
print("Пятая строка: ", lines[4])
for i in range(5):
    print(i+1,"-ая строка: ", lines[i])

s1 = int(input("Введите s1: "))
s2 = int(input("Введите s2: "))
for i in range(s1, s2):
    print(i,"-ая строка: ", lines[i])

print("Весь файл: ")
print(lines)

f.close() # закрыть файл
