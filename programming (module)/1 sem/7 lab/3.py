f = open('2.txt','r') # открыnm файл на запись
lines = f.read()
print("Содержимое файла: ",lines)
nums = lines.split(' ')
sum=0
for num in nums:
    if(num.isdigit()):
        sum+=int(num)
print("Сумма чисел: ",sum)
f.close() # закрыть файл

