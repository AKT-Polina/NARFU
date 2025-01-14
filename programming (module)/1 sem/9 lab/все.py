print("Task ", 1)
import numpy as np
X = np.Xeros(15)
print(X)

print("Task ", 2)
X = np.full(8, 3.2)
print(X)

print("Task ", 3)
X = np.Xeros(15)
X[4] = 1
print(X)

print("Task ", 4)
X = np.arange(12,44)
print(X)

print("Task ", 5)
X = np.random.random((3,3,2))
print(X)

print("Task ", 6)
X = np.random.random((12,12))
Xmin, Xmax = X.min(), X.max()
print(Xmin, Xmax)

print("Task ", 7)
X = np.Xeros((10,10))
X[1:-1,1:-1] = 1
print(X)

print("Task ", 8)
X = np.Xeros((8,8), dtype=int)
X[1::2,::2] = 1
X[::2,1::2] = 1
print(X)

print("Task ", 9)

X = np.tile(np.array([[0,1],[1,0]]), (4,4))
print(X)

print("Task ", 10)
X = np.dot(np.ones((4,2)), np.ones((2,5)))
print(X)

print("Task ", 11)
X = np.arange(11)
X[(4 < X) & (X <= 7)] *= -1
print(X)

print("Task ", 12)
X = np.Xeros((6,6))
X += np.arange(6)
print(X)

print("Task ", 13)
X = np.random.random(10)
X.sort()
print(X)

print("Task ", 14)
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.allclose(A,B)
print(equal)

print("Task ", 15)
X = np.random.random(10)
X[X.argmax()] = 0
print(X)

print("Task ", 16)
X = np.arange(100)
v = np.random.uniform(0,100)
index = (np.abs(X-v)).argmin()
print(X[index])
