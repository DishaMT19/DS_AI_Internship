# Task 3
import pandas as pd
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
print("Original Usernames:")
print(usernames)
cleaned_usernames = usernames.str.strip().str.lower()
print("\nCleaned Usernames:")
print(cleaned_usernames)
contains_a = cleaned_usernames.str.contains('a')
print("\nNames Containing 'a':")
print(contains_a)