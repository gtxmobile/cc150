import genlinklist
from genlinklist import *

a=genlinklist.genrl(10)
b=genlinklist.genrl(10)

result=Node(0)
re=result
carry=0
genlinklist.plnklist(a)

genlinklist.plnklist(b)

while a or b:
    if not a:
        a=Node(0)
    if not b:
        b=Node(0)
    he=a.data+b.data+carry
    re.data=he%10
    carry=he//10
    a=a.next
    b=b.next
    if (not a) and (not b):
        if carry:
            re.next=Node(carry)
        break
    re.next=Node(0)
    re=re.next


genlinklist.plnklist(result)

