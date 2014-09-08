#-*- coding: utf-8 -*-



constwei=0

def roal(inpu,weicnt):
    cnt0=0
    cnt1=0
    if weicnt<0:
        return 0
    odd=[]
    even=[]
    for i in inpu:
        if (i>>(constwei-weicnt))&0x1==1:
            odd.append(i)
        else:
            even.append(i)
    if len(odd)>=len(even):
        return (roal(even,weicnt-1))<<1|0
    else:
        return (roal(odd,weicnt-1))<<1|1


