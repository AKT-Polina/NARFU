n = int(input("Сколько чисел хотите ввксти? "))
nums = list()
for i in range(n):
    nums.append(int(input("Введите цифру: ")))

print(nums, " ваш массив")
num = int(input("Какую цифру хотите найти? "))
count = 0
for i in range(n):
    if(nums[i]==num):
        count+=1

print("Число ", num, " встречается ", count, " раз")
