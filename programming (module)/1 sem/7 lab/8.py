f = open('3.txt','r', encoding="utf-8") # открыnm файл на запись
lines1 = f.readlines()
file = open('4.txt','r', encoding="utf-8")
lines2 = file.readlines()
c=0
ravni = True
for line in lines1:
    if(line!=lines2[c]):
        print("Номер отличающейся строки: ", c)
        ravni=False
        break
    c+=1
if(ravni):
    print("Все строки совпадают")

f.close() # закрыть файл
file.close()
