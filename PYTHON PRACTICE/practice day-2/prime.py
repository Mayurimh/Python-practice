a=int(input("enter a number : "))
flag=False
for i in range(2,a):
    if a%i==0:
        flag=True
        break
if flag==True:
    print("the number is prime number...")
else:
    print("the number is not prime number....")
