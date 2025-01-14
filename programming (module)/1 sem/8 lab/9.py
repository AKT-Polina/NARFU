def max_length_word(file):
    f = open(file,'r', encoding="UTF-8") # открыnm файл на запись
    lines = f.read()
    lines = lines.replace('\n', ' ')
    lines = lines.replace(',', '')
    lines = lines.replace('.', '')
    lines = lines.replace('!', '')
    lines = lines.replace('?', '')
    words = lines.split(' ')
    lens = []
    for word in words:
        lens.append(len(word))
    max_len = 0
    for i in lens:
        if(i >= max_len):
            max_len = i
    
    
    print("Содержимое файла: ",words)
    print("Наибольшая длина: ",max_len)
    print("Список слов: ")
    for word in words:
        if(len(word) == max_len):
            print(word)
    
max_length_word("title.txt")
