l = [0, 1, 2, 3, 4, 5, 6, 7, 8]
k1 = 3
k2 = 6
l1 = []
l2 = []
l3 = []
print(l)
for i in range(k1):
    l1.append(l[i])
print("Первая часть списка ",l1)

for i in range(k2, len(l)):
    l2.append(l[i])
print("Третья часть списка ",l2)

for i in range(k1, k2):
    l3.append(l[i])
print("Середина списка ",l3)

l.clear()
l = l2 + l3 + l1
print(l)
