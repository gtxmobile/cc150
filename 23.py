import genlinklist
import random
head=genlinklist.genrl(20)
ri=random.randint(1,20)
delnod=head
i=0
while i!=ri:
    delnod=delnod.next
    i+=1
genlinklist.plnklist(head)
print(delnod.data)
delnod.data=delnod.next.data
delnod.next=delnod.next.next
genlinklist.plnklist(head)

