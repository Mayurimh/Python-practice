year=int(input("year : "))
if year%4==0 and year%100==0:
    print("the year is leap year...")
# elif year%100==0:
    # print("the year is leap year...")
else:
    print("the is not leap year....")