num=int(input('enter a number : '))
sum=0
temp=num
while temp!=0:
    rem=temp%10
    sum=sum+pow(rem,3)
    temp=temp//10
    
if(sum==num):
    print('the number is Armstrong')
else:
    print('the number is not armstong')