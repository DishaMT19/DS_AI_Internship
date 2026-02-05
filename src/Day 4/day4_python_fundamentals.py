# 1. Create a dictionary and print it

a = { "Fruit": "apple", "Age": 20, "City": "New York" }
print(a) 

# 2. Access and modify dictionary elements

student = {"Name":"Amit", "age":21,"courses":"Enigineering"}
print(student["Name"])
student["age"]=22
student["city"]="Delhi"
print(student)


# 3. Dictionary methods 

marks = {"Math":90, "Science":85, "English":88}
print(marks.get("Math"))
print(marks.get("History", "0"))
for  subject,score in marks.items():
    print(f"{subject}: {score}")
marks.update({"Science": 95})
print(marks)
marks.pop("English")


# 4. check and display purchase amounts

purchase ={
    "Alice": 250,
    "Bob": 150,
    "Charlie": 300
}

for name, amount in purchase.items():
    print(f"{name} spent  ₹ {amount}")  

print("total customer purchases:",len(purchase))


# 5. input dictionary from user and display

n = int(input("Enter number of customers: "))
user_purcahse = {}

for i in range(n):

    name = input("Enter customer name: ")
    amount = int(input(f"Enter purchase amount for {name}: "))
    user_purcahse[name] = amount

print("Customer Purchases:",user_purcahse)



# 6. find the customer with highest purchase amount

top_customer = min(user_purcahse, key=user_purcahse.get)
print(f"lowest customer: {top_customer} with ₹{user_purcahse[top_customer]}")



# 7.Sets and their operations

A={1,2,3}
B={3,4,5}
print(A|B) #union
print(A&B) #intersection
print(3 in A)
print(2 in B)


# Task 1

contact = {
    "Alice": 9874563210,
    "Bob": 8765432190,
    "Charlie": 7654321980
}

contact["David"] = 6543219870
contact["Bob"]=974596655

existing_contact  = contact.get("Bob", "Contact not found")
missing_contact = contact.get("Eve", "Contact not found")

print(" Contact List:")
for name, phone in contact.items():
    print(f"Contact: {name} | Phone: {phone}")

print("\n🔍 Safe Lookup Results:")
print(f"Alice: {existing_contact}")
print(f"Eve: {missing_contact}")


# Task 2

raw_logs=["ID01","ID02","ID01","ID05","ID02","ID08","ID01"]
unique_users=set(raw_logs)
print("Unique users are:",unique_users)
print("Is ID05 in the logs?", "ID05" in unique_users)
print("Length of original list:", len(raw_logs))
print("Length of the unique set:", len(unique_users))


# Task 3 

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

Common_interest = friend_a & friend_b
All_interests = friend_a | friend_b
Unique_interests = friend_a - friend_b

print("Common Interest :", Common_interest)
print("All interests",All_interests)
print("Unique interest",Unique_interests)
