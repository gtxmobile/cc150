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
        if a[l]<a[m]:#�����
            if x>a[m]:#��m-u֮�� ����
                l=m+1
            elif x>=a[l]:#��ǰ��� l-m֮��
                u=m-1
            else:#�ں��� ���ε��������ȴ��С������С���Ƕ�
                l=m+1
        elif x>a[l]:
            u=m-1
        elif x<a[m]:
            u=m-1
        else:
            l=m+1
    return -1
print(search(a,0,len(a)-1,30))

