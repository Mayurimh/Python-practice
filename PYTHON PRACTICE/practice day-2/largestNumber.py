#method 1
num1=float(input("enter a number : "))
num2=float(input("enter a number : "))
num3=float(input("enter a number : "))
if num1>=num2 and num1>=num3:
    print("largest number : ",num1)
elif num2>=num1 and num2>=num3:
    print("largest number : ",num2)
else:
    print("largest number : ",num3)

