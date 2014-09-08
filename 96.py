

def findr(a,l,u,x):
    if l>u:
        return (False,u)
    m=(l+u)//2
    if a[m][0]==x:
        return (True,m)
    elif a[m][0]<x:
        return findr(a,m+1,u,x)
    else:
        return findr(a,l,m-1,x)
def findx(a,l,u,x):
    if l>u:
        return -1
    m=(l+u)//2
    if a[m]==x:
        return m
    elif a[m]<x:
        return findx(a,m+1,u,x)
    else:
        return findx(a,l,m-1,x)

a=[[i for i in range(j,10+j)] for j in range(10)]
for i in a:
    print(i)
x=10

flag,row=findr(a,0,len(a)-1,x)
if flag:
    print(row,0,a[row][0])
else:
    b=findx(a[row],0,len(a[row])-1,x)
    print(row,b,a[row][b])




