
from random import *

def fmaxseq(a):
    he=0
    bidx=0
    maxe=0
    maxb=0
    maxsum=0
    for i in range(len(a)):
        he+=a[i]
        if he<0:
            he=0
            bidx=i+1
        elif he>maxsum:
            maxsum=he
            maxb=bidx
            maxe=i
    print(maxsum,a[maxb:maxe+1])

a=[randint(-10,20) for i in range(10)]
print(a)
fmaxseq(a)


