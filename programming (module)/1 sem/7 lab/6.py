f = open('3.txt','r', encoding="utf-8") # открыnm файл на запись
lines = f.readlines()
max_len = len(lines[0])
num = 0
c = 0
for str in lines:
    if(max_len < len(str)):
        max_len = len(str)
        num = c
    c+=1

print("Длина самой большой строки: ", max_len)
print("Номер самой большой строки: ", num)
print("Самая длинная строка: ", lines[num])
f.close() # закрыть файл
