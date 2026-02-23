# 1

number =[10,20,30,40]
coordinates= (5,10)
print(number)
print(coordinates)


# 2

a=[100,200,300,400,500,600,700,800,900]

print(a[-3:-1])
print(a[-1:-3])
print(a[1:4:2])
print(a[1:7:2])
print(a[-4:-3:2])

# 3

marks = [80,85,75,96]
marks.append(88)
marks.pop()
marks.append(92)
marks.sort()
print(marks)
marks.reverse()
print(marks)



# task 1


inventory = ["Apples", "Bananas", "Carrots", "Dates"]
print("Current Inventory:", inventory)
inventory.append("Eggs")
print("After Adding Eggs:", inventory)
inventory.remove("Bananas")
print("After Removing Bananas:", inventory)
inventory.sort()
print("Final Updated Inventory:", inventory)



# task 2

temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print( temperatures [0])
print( temperatures [-1])
print(temperatures [3:6])
print(temperatures [-3:])


# task 3

screen_res = (1920, 1080)
print(f"Current Resolution: {screen_res[0]}x{screen_res[1]}")
#screen_res[0] = 1280
print("Tuples cannot be modified!")
