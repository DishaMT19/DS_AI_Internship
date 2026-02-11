# -*- coding: utf-8 -*-
# Task 1
import pandas as pd
products = pd.Series([700, 150, 300],index=['Laptop', 'Mouse', 'Keyboard'])
print("Full Product List:")
print(products)
print("\nPrice of Laptop:")
print(products['Laptop'])
print("\nFirst Two Products:")
print(products.iloc[0:2])

