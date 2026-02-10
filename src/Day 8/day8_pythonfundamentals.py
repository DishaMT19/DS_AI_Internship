# -*- coding: utf-8 -*-
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

c = np.array([[20,30,40],
              [10,30,50],
              [70,80,90]])

d = np.array([])

print("1d array:",b)
print("2d array:",a)
print("3d array:",c)
print("0 array:",d)

result = a + b
print(result)
# Vectorized vs Loop example
arr = np.random.rand(1000000)
# Vectorized
squared = arr ** 2
print(squared)

arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(reshaped)

a = np.array([[1, 2, 3]])
b = np.array([[4, 5, 6]])

vstack = np.vstack((a, b))
print(vstack)

hstack = np.hstack((a, b))
print(hstack)


## Statistical function in Numpy

data = np.array([[10, 20, 30],
                 [40, 50, 60]])

print(np.mean(data))
print(np.mean(data, axis=0))
print(np.mean(data,axis=1))

##linspace 

arr = np.linspace(0, 2, 5)
print("Linspace :\n",arr)

# floor, ceil, round, and trunc

arr = np.array([1.2,2.8,-3.7])

print("\n")
print("Original:\n", arr)
print("Floor   :", np.floor(arr))
print("Ceil    :", np.ceil(arr))
print("Round   :", np.round(arr))
print("Trunc   :", np.trunc(arr))
