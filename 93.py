#-*- coding:utf-8 -*-
from random import randint

a=[randint(i,i+4) for i in range(2,100,4)]
ri=randint(1,len(a))
a=a[ri:len(a)]+a[:ri]
print(a)

def search(a,l,u,x):
    while l<=u:
        m=(l+u)//2
        if x==a[m]:
            return m
        if a[l]<a[m]:#分情况
            if x>a[m]:#在m-u之间 后半段
                l=m+1
            elif x>=a[l]:#在前半段 l-m之间
                u=m-1
            else:#在后半段 后半段的数据是先大后小并且在小的那段
                l=m+1
        elif x>a[l]:
            u=m-1
        elif x<a[m]:
            u=m-1
        else:
            l=m+1
    return -1
print(search(a,0,len(a)-1,30))

