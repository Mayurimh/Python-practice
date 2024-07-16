def Compound_interest(principal,rate,time):
    amount=principal*(pow((1+rate/100),time))
    CI=amount-principal
    print("the compound interest is ",CI)

Compound_interest(10000,10.25,5)