
# -*- coding:utf-8 -*-
from random import randint
def fmindis(a,w1,w2):
    print(a)
    print(w1,w2)
    mindis=3000
    dis1=-1000
    dis2=-1000
    diff=0
    for i in range(len(a)):
        if w1==a[i]:
            dis1=i
            diff=dis1-dis2
            if diff<mindis:mindis=diff;
        elif w2==a[i]:
            dis2=i
            diff=dis2-dis1
            if diff<mindis:mindis=diff;
    print(mindis)
    return mindis

ar=[randint(1,100) for i in range(200)]
fmindis(ar,ar[34],ar[69])
