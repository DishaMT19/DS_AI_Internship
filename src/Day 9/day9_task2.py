# Task 2
import pandas as pd
grades = pd.Series([85, None, 92, 45, None, 78, 55])
print("Original Grades:")
print(grades)
print("\nMissing Values (True means missing):")
print(grades.isnull())
filled_grades = grades.fillna(0)
print("\nGrades After Filling Missing Values:")
print(filled_grades)
filtered_grades = filled_grades[filled_grades > 60]
print("\nScores Greater Than 60:")
print(filtered_grades)

