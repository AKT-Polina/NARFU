f = open('3.txt','r', encoding="utf-8") # открыnm файл на запись
lines = f.readlines()
r_lines = []
file = open('reverse.txt','w', encoding="utf-8")
for line in reversed(lines):
    for i in reversed(line):
        print(i, end='')
        file.write(str(i))
        

f.close() # закрыть файл
file.close()
