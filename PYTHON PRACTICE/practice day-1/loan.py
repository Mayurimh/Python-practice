def EMI(l,r,t):
    r=r/(12*100)
    t=t*12
    emi=t
    # emi=l*r*(pow((1+r),)
    return emi
# P x R x (1+R)^N / [(1+R)^N-1]
loan=int(input('enter loan here : '))
ann_rate_inter=float(input('enter rate : '))
tenure=int(input('enter year : '))
monthly_install=EMI(loan,ann_rate_inter,tenure)
print('montly EMI : ',monthly_install)