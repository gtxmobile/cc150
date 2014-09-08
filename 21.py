import genlinklist

def rmlinkdup():
    head=genlinklist.genrl(20)
    tail=head
    cur=head
    while cur.next:
        print(cur.data,'->',end='')
        cur=cur.next
        tmp=head
        flag=0
        while tmp!=tail:
            if tmp.data==cur.data:
                flag=1
                break
            tmp=tmp.next
        if tmp.data==cur.data:
            flag=1
        if not flag:
            tail.next=cur
            tail=cur
    tail.next=None
    return head
node=rmlinkdup()
print()
while node.next:
        print(node.data,'->',end='')
        node=node.next
print(node.data)

