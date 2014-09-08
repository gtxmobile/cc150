n=100

def cont2(n):
    nstr=str(n)
    numof2=0
    nlen=len(nstr)
    for i in range(nlen):
        #print(nstr[i])
        if nstr[i]>'2':
            numof2+=10**(nlen-i-1)
        elif nstr[i]=='2':
            print(nstr[i+1:])
            numof2+=int(nstr[i+1:])
        else:
            pass
    print(numof2)
cont2(n)
