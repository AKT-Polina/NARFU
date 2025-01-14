import random

a = {random.randint(1, 100) for _ in range(20)}
b = {random.randint(1, 100) for _ in range(20)}
print(*(a - b) , end=' ')
