lst = [[1, 10], [2, 20], [3, 30], [4,40]]
lst1 = []

for i in lst:
    for j in i:
        lst1.append(j)

lst.clear()
lst = lst1
print(lst)   
i = input()