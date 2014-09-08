
def num2bin(a):
    fa=float(a)
    intpart=int(fa)
    flpart=fa-intpart
    intstr=''
    decstr=''
    while  intpart:
        intstr=str(intpart%2)+intstr
        intpart>>=1
    while flpart>0.0:
        print(flpart)
        flpart*=2
        if flpart>=1:
            decstr+='1'
            flpart-=1
        else:
            decstr+='0'


    print(intstr,'.',decstr)


num2bin('93.72')
