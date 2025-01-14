def capital (lst):
    a = []
    for i in lst:
        a.append(i.title())
    return a 
 
lst =  ["катя", "маша", "таня", "саша"]
lst = capital(lst)
print(lst)
i = input()