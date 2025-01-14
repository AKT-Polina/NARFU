from collections import Counter  
for word, count in Counter(input().split()).items():  
    print(word, "встречается", count, "раз")
