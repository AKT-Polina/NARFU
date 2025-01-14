f = open('3.txt','r', encoding="utf-8") # открыnm файл на запись
lines = f.read()
#print("Содержимое файла: ",lines)
import re
text = re.sub('^[a-zA-Z]', '', lines)
print("Количество английских символов: ",len(re.findall('[a-zA-Z]',lines)))

words = lines.split(' ')
print("Кол-во слов: ", len(words))

lines = lines.split('\n')
print("Количество строк: ", len(lines))



f.close() # закрыть файл

