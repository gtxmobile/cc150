#-*- coding:utf-8 -*-
from random import randint
from operator import lt
an=[''.join([chr(randint(100+j,100+j+1)) for i in range(randint(0,4))]) for j in range(20)]
for i in range(len(an)):
    if randint(0,1)==0:
        an[i]=''
while 1:

    b=randint(0,len(an)-1)
    if an[b]!='':
        x=an[b]
        break;
print(x)
for i in range(len(an)):
    print(i,an[i],',',end='')
print()
cishu=0
def search(an,l,u,x):
    global cishu
    if l<=u:
        m=(l+u)//2
        #print(m)
        if an[m]=='':
            m=notblank(an,l,m-1)
        if m==-1:
            return search(an,(l+u)//2+1,u,x)
        elif x==an[m]:
            print(an[m],m)
            return m
        elif lt(x,an[m]):#·ÖÇé¿ö
            return search(an,l,m-1,x)
        else:
            return search(an,m+1,u,x)
    return -1
def notblank(a,l,u):
    if l>u:
        return -1
    m=(l+u)//2
    print('b',m)
    if a[m]=='':
        m=notblank(a,m+1,u)
        print('da',m)
    if m==-1:
        m=notblank(a,l,m-1)
        print('xiao',m)
    if m==-1:
        return -1
    return m
t1='ab'
t2='bb'
#print(notblank(an,0,len(an)-1))
print(search(an,0,len(an)-1,x))
