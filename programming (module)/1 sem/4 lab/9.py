lst = [0, 1, 2, 3, 4, 5, 6]
print(lst)
lst1 = []
for i in range (0, len(lst) -1, 2):
    tmp = lst[i]
    lst[i] = lst[i + 1]
    lst[i + 1] = tmp
print(lst)
