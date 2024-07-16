# scripting is writing programs to automated tasks and python by itself is 
# scipting language...
# library  
# 1.os 


# import os 
# def directory():
#     cwd=os.getcwd()
#     print(cwd)
# def file_path(filename):
#     path=os.path.abspath((filename))
#     print(path)

# directory()
# filename="sample.txt"
# file_path(filename)

# 2.time

# import time

# abc=time.time()
# print(abc)

# localtime=time.localtime(abc)
# print(localtime)
# print(localtime.tm_year)
# print(localtime.tm_mon)
# print(localtime.tm_mday)
# print(time.ctime(abc))

# 3.smtplib
# this is protocol used to email 

# import smtplib

# smtobj=smtplib.SMTP('smtp.gmail.com',587)
# smtobj.ehlo()
# smtobj.starttls()
# smtobj.login('immayurimh09.16@gmail.com','#password')
# smtobj.sendmail("immayurimh09.16@gmail.com",'mayurimhavale@gmail.com','subject:this mesg for checksmtp \n this is simple message')
# smtobj.quit()


# def function(*args):
#     for i in args:
#         print(i)

# function(12,23,34,45,'mayuri')


# def function(*args,**kargs):
#     for i in kargs.items():
#         print(i)

# function(a=12,b=23,c=34,d=45,e='mayuri')


# nested function 

def func1():
    x=10
    def func2(x):
        return x+1
    return func2(x)
p=func1()
print(p)