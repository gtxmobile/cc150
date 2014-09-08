import random

def setmn0(m,n):
    mn=[[random.randint(0,9) for i in range(n)] for j in range(m)]
    bj=[0 for i in range(m+n)]
    for i in range(m):
        print(mn[i])
        for j in range(n):
            if mn[i][j]==0:
                bj[i]=1
                bj[m+j]=1
    for k in range(m+n):
        if bj[k]==1:
            if k<m:
                mn[k]=[0 for l in range(n)]
            else:
                for j in range(m):
                    mn[j][k-m]=0
    print()
    for km in mn:
        print(km)

setmn0(8,10)
