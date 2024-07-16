# using for loop

# num=int(input('enter number you want multiplication table : '))
# mul=1
# for i in range(1,11):
#     mul=num*i
#     print(num ," X"," ",i,'='," ",mul)

# using while loop

num=int(input('enter number you want multiplication table : '))
mul=1
if num <=0:
    print("for this number multiple table does not exist")
else:
    i=1
    while (i<=10):
        mul=num*i
        print(mul)
        i+=1
