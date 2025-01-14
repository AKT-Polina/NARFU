f = open('1.txt','r') # открыnm файл на запись
lines = f.read()
print("Содержимое файла: ",lines)
ch = input("Введите искомый символ: ")
count = 0
for i in lines:
    if(i==ch):
        count+=1
if(count>0):
    print("Yes")
else:
    print("No")
    
f.close() # закрыть файл

