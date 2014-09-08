
from random import randint

A=[randint(1,30) for i in range(10)]
B=[randint(1,30) for i in range(10)]
A.sort()
B.sort()
print(A)
print(B)
ai=len(A)-1
A+=[0]*len(B)
bi=len(B)-1
alen=len(A)-1
while ai>-1 and bi>-1:
    if A[ai]>B[bi]:
        A[alen]=A[ai]
        ai-=1
    else:
        A[alen]=B[bi]
        bi-=1
    alen-=1
alen+=1
if ai==-1:
    A[:alen]=B[:bi+1]
else:
    A[:alen]=A[:ai+1]
print(A)

