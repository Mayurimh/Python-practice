
num=int(input("enter the number : "))
sum=0
temp=num

while temp!=0:
    remainder=temp%10
    sum=sum+(remainder**3)
    temp=temp//10
    
if(sum==num):
    print("the number is armstrong..")
else:
    print("the number is not armstrong...")