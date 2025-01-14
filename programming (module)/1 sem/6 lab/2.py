n1 = int(input("Сколько чисел хотите ввксти? "))
nums1 = list()
for i in range(n1):
    nums1.append(int(input("Введите цифру: ")))

print(nums1, " ваш массив")

n2 = int(input("Сколько чисел хотите ввксти? "))
nums2 = list()
for i in range(n2):
    nums2.append(int(input("Введите цифру: ")))

print(nums2, " ваш массив")

for i in range(n1):
    count = 0
    for j in range(n2):
        if(nums1[i]==nums2[j]):
            count+=1
    print(nums1[i], " число встречается во втором массиве ", count, " раз")
print("\n")
for i in range(n2):
    count = 0
    for j in range(n1):
        if(nums2[i]==nums1[j]):
            count+=1
    print(nums2[i], " число встречается в первом массиве", count, " раз")
