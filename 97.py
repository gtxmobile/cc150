
from random import randint
a=[(randint(1,100),randint(1,100)) for i in range(10)]

def get1(x):
    return x[0]
def tuplesort(b):
    a=sorted(b,key=get1)
    print(a)
    unfit=[0]
    seq=[]
    for i in unfit:
        tmp=[]
        tmp.append(a[i])
       # print(tmp)
        for j in range(i+1,len(a)):
           # print(a[j],tmp[-1])
            if a[j][1]>tmp[-1][1]:
                tmp.append(a[j])
            elif j not in unfit:
                unfit.append(j)
        if len(tmp)>len(seq):
            seq=tmp
    print(seq)


tuplesort(a)
