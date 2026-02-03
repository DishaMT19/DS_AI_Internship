age = 15
height = 5.4
_name = "Alice"
is_student = True

print(type(age))
print(type(height))
print(type(_name))
print(type(is_student))

# User input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = a + b
    print("Addition:", result)

elif operation == "-":
    result = a - b
    print("Subtraction:", result)

elif operation == "*":
    result = a * b
    print("Multiplication:", result)

elif operation == "/":
    if b != 0:
        result = a / b
        print("Division:", result)
    else:
        print("Error: Division by zero")

else:
    print("Invalid operation")






name=input("Enter your name: ")
print("Hello, " + name + "! Welcome!")


#conacting usng fstring

age = input("Enter your age: ")
print(f"My age is, {age} years.")




#task 1

name = input("Enter your name: ")
age = int(input("Enter your current age: "))
print(f"Hey {name}, you will be {age + 4} years old in 2030!")



#task 2


total_bill = float(input("Enter the total bill amount: "))
people = int(input("Enter the number of people: "))

share_per_person = total_bill / people

print(f"Total Bill: {total_bill}. Each person pays: {share_per_person}")

print(type(total_bill))
print(type(people))
print(type(share_per_person))


#task 3

item_name=str(input("enter the item name:"))
item_price=int(input("enter the item price:"))
item_qut=int(input("enter the Qty:"))
price=item_price*item_qut
in_stock=True
print(f"Item:{item_name}, Price:{item_price}, Qty:{item_qut},Total Price:{price},Available:{in_stock}")


 
