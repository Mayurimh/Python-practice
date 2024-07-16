num=int(input('enter the number: '))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print('factorial is ',fact)

def fact(num):
    if num==0:
        return 1
    else:
        return num*(fact(num-1))
if num<0:
    print('the factorial for less than 1 does not exist...')
else:
    print('factorial is ',fact(num))