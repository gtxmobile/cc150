a=20
b=1000

tmp=a-b
sign=tmp>>31
maxn=(a+b+sign*tmp)/2
print(maxn)

#sign=tmp&0x80000000

