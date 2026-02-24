# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 10:39:37 2026

@author: disha
"""
# Task 1


import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Price": [250000, 270000, 300000, 320000, 350000, 400000, 450000, 500000,600000, 750000, 900000, 1200000], 
    "City": ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Bangalore","Bangalore", "Mumbai", "Delhi", "Delhi", "Mumbai", "Delhi"]
}
df = pd.DataFrame(data)
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=6, density=True, alpha=0.6)
df["Price"].plot(kind="kde")
plt.title("Histogram + KDE of House Prices")
plt.xlabel("Price")
plt.ylabel("Density")
plt.grid(True)
plt.show()
skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)
city_counts = df["City"].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(city_counts.index, city_counts.values)
plt.title("Count Plot of City")
plt.xlabel("City")
plt.ylabel("Count")
plt.grid(axis="y")
plt.show()





# Task 2


import pandas as pd
import matplotlib.pyplot as plt
data = {
    "SquareFootage": [600, 750, 900, 1100, 1300, 1500, 1700, 2000, 2300, 2600],
    "Price":         [35, 45, 55, 70, 85, 95, 110, 140, 160, 190],  
    "City": ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi",
             "Bangalore", "Bangalore", "Mumbai", "Delhi", "Mumbai"]
}
df = pd.DataFrame(data)
plt.figure(figsize=(7, 5))
plt.scatter(df["SquareFootage"], df["Price"])
plt.title("Scatter Plot: SquareFootage vs Price")
plt.xlabel("Square Footage")
plt.ylabel("Price (in Lakhs)")
plt.grid(True)
plt.show()
plt.figure(figsize=(7, 5))
df.boxplot(column="Price", by="City")
plt.title("Boxplot: City vs Price")
plt.suptitle("")  
plt.xlabel("City")
plt.ylabel("Price (in Lakhs)")
plt.grid(True)
plt.show()
print("Observation: As SquareFootage increases, Price seems to increase.")




# Task 3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "SquareFootage": [600, 750, 900, 1100, 1300, 1500, 1700, 2000, 2300, 2600],
    "Bedrooms":      [1, 2, 2, 3, 3, 3, 4, 4, 4, 5],
    "Bathrooms":     [1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
    "Price":         [35, 45, 55, 70, 85, 95, 110, 140, 160, 300]  # outlier at 300
}
df = pd.DataFrame(data)
corr_matrix = df.corr(numeric_only=True)
print("Correlation Matrix:\n")
print(corr_matrix)
plt.figure(figsize=(7, 5))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()
high_corr_pairs = []
for i in range(len(corr_matrix.columns)):
    for j in range(i + 1, len(corr_matrix.columns)):
        value = corr_matrix.iloc[i, j]
        if value > 0.8:
            high_corr_pairs.append((corr_matrix.columns[i], corr_matrix.columns[j], value))

print("\nHighly correlated pairs (> 0.8):")
for pair in high_corr_pairs:
    print(pair)
plt.figure(figsize=(6, 4))
sns.boxplot(y=df["Price"])
plt.title("Boxplot for Outliers in Price")
plt.ylabel("Price")
plt.show()





