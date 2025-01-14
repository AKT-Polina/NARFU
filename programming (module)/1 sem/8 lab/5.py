def read_from_last(count, file):
    from os.path import exists
    if(exists(file)):
        f = open(file,'r') # открыnm файл на запись
        lines = f.readlines()
        c = 0
        for i in reversed(lines):
            if(c < count):
                print(i)
                c += 1
        f.close() # закрыть файл
    else:
        print("Файл не существует")
read_from_last(3,"MyFile.txt")

