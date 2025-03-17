# if condition
# 4 spaces has to be given
# if condition:
#    statement 

isExist = True
if isExist:
    print("dont copy!!!")
print("Executed")
# to come out of the loop just delete 4 spaces

num1, num2 = 10, 30
if num1 > num2:
    print("num1 is greater")

else:
    print("num2 is greater")

############################

n1 = int(input("enter number1:\n"))
n2 = int(input("enter number2:\n"))
n3 = int(input("enter number3:\n"))

#if n1 > n2 and n1 > n3:
 #   print(f"number1 (n1) is greatest")
#else:
 #   if n2 > n1 and n2 > n3:
  #      print(f"number2 (n2) is greatest")
   # else:
    #    print(f"number3 (n3) is greatest")

if n1 > n2 and n1 > n3:
    print(f"number1 (n1) is greatest")
elif n2 > n1 and n2 > n3:
    print(f"number2 (n2) is greatest")
else:
    print(f"number3 (n3) is greatest")

