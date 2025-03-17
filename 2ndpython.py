a = 10
b = 20
c = 30

# arthimetic
print(a+b)
print(b*a)
print(b-a)
print(b/a)
print(a//b)

# comparison
print("-------------------------------")
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a != b)

# logical poerator
print("-------------------------------")
print("-------------------------------")
print(a > b and a > c)
print(a > b or a > c)

print("-------------------------------")
print("-------------------------------")

first_name = "bhanu" #variable
last_name = "prakash"
fn = first_name + last_name
print(fn) # print is built in function

print("-------------------------------")
print("-------------------------------")

#assignment

count =10
count += 1
count -= 5
print(count)

print("-------------------------------")
print("-------------------------------")

#identity 
# is operator is used to compare the id of two values
num1 = ["abc"]
num2 = ["abc"]
print(num1 is num2)
print(id(num1))
print(id(num2))

# "in" oprator or membership operator used to find the file or something is present in that folder
import os
print(os.listdir()) 