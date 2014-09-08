
from random import randint

an=[''.join([chr(randint(85,89)) for i in range(4)]) for j in range(20)]

print(an)



def cmpang(a):
    print(sorted(list(a)))
    return ''.join(sorted(list(a)))

bv=sorted(an,key=cmpang)
print(bv)
