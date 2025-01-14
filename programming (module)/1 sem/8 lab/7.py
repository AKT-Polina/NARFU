def remove_braces(st):
    string=""
    c = False
    for i in st:
        if(i == '('):
            c = True
        elif(i == ')'):
            c = False
        elif(c):
            continue
        else:
            string += i
        
            
    return(string)
    
print(remove_braces('Шила(лишнее (лишнее) лишнее) в мешке не утаишь(лишнее)'))
