
from random import randint

def getm(a,m):
    subm=[]
    for i in range(m):
        j=randint(i,len(a)-1)
        subm.append(a[j])
        a[j]=a[i]
    print(subm)

ra=[randint(1,100) for i in range(30)]
print(ra)
getm(ra,10)
