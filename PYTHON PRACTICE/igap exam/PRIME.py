def isprime(n):
    flag=False
    if n==1:
        return flag
    else:
        for i in range(2,n): 

            if n%i==0:
                return flag
        else:
            flag=True
        return flag

n=int(input("enter the number : "))
value=isprime(n) 
print(value)