from genlinklist import *

def findpalin():
    head=genrl(20)
    plnklist(head)
    makehuan(head,10)
    plnklist(head)
    n1=head.next
    n2=head.next.next
    n11=head
    while n1!=n2:
        n1=n1.next
        n2=n2.next.next
    while n1!=n11:
        n1=n1.next
        n11=n11.next
    print()
    print(n1.data)

findcircle()
