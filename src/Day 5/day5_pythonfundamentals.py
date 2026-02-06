# 1
def greet():
    print("Hello, World!")
greet()    

# 2

def add_numbers(a, b):
    return a + b
result = add_numbers(5, 3)
print("The sum is:", result)

#3 returning multiple values

icecream= "Chocolate"
def food():
    fruit = "Apple"
    vegetable = "Carrot"
    print("fruit:", fruit)
    print("vegetable:", vegetable)
    print("icecream:", icecream)
food()

# 4

import math
import random
import datetime
number = 36
square_root = math.sqrt(number)
random_number = random.randint(1, 100) 
current_time = datetime.datetime.now()
print("Square root of", number, "is:", square_root)
print("Random number between 1 and 100:", random_number)
print("Current date and time:", current_time)


# Task 1 

def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area, perimeter = calc_rectangle(length, width)

print(f"Area: {area}\n Perimeter: {perimeter}")





