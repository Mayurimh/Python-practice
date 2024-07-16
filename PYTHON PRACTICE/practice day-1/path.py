import os.path
def filepath(p):
    arr=[]
    alpha=[]
    digit=[]
    special=[]
    for char in path:
        if char.isalpha():
            alpha.append(char)
        elif char.isdigit():
           digit.append(int(char))
        else:
            special.append(char) 
    x=len(alpha)
    y=len(digit)
    z=len(special)
    d=dict()
    d['alphabet']=x
    d['digit']=y
    d['specialcharacters']=z
    print('number of alphabets : ',x)
    print('number of digits : ',y)
    print('number of special character : ',z)
    print()
    return d

# path ='practice day-1\mayurimhavale123@.txt'
path=input(('enter the path : '))
check_file=os.path.isfile(path)
print(check_file)
dictionary=filepath(path)
print('dictionary is : ',dictionary)

