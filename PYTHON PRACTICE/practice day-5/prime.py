# lower=int(input('enter lower limit : '))
# upper=int(input('enter upper limit : '))
# for num in range(lower,upper+1):
#     if num > 1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#                 print(num)

num=int(input('enter the number : '))
if num > 1:
    for i in range(2,int(num/2)+1):
        if num%i==0:
            print('number is not prime .....')
            break
    else:
        print('number is prime number .....')
else:
    print('number is not prime number.... ')