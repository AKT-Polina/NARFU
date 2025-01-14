def add_text_to_file(st):
    from os.path import exists
    if(exists('MyFile.txt')):
        f = open('MyFile.txt','a') # открыnm файл на запись
        print("Строка добавлена к существующим")
        f.write(st)
        f.close() # закрыть файл
    else:
        f = open('MyFile.txt','a') # открыnm файл на запись
        print("Файл был создан")
        f.write(st)
        f.close() # закрыть файл
add_text_to_file("Hello")

