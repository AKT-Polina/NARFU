def first_last(let, st):
    indexes = []
    count = 0
    c=0
    for i in st:
        if(i == let):
            indexes.append(count)
            c+=1
        count+=1
    if(c == 0):
        typle=(-1, -1)
    elif(c == 1):
        typle=(indexes[0], -1)
    else:
        typle=(indexes[0], indexes[-1])
    return(typle)

print(first_last("l", "HelloHllo"))
