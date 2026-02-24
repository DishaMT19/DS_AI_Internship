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