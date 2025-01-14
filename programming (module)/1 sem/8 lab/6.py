def camel(st):
    string=""
    for i in range(len(st)):
        if(i%2!=0):
            string += st[i].lower()
        else:
            string += st[i].upper()
    return(string)
    
print(camel("ilovemylittlepony"))
print(camel("PONY"))
