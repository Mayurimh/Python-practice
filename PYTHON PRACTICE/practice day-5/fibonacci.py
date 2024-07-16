
seq=int(input('enter value : '))
# a=0
# b=1
# sum=0
# while sum < seq:
#        print(a)
#        nth = a + b
#        # update values
#        a = b
#        b= nth
#        sum+= 1

a,b=0,1
count=0
fab=[]
while count<seq:
    fab.append(a)# print(a)
    sum=a+b
    a=b
    b=sum
    count+=1
    
print(fab)

