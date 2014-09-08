import genlinklist


def nthnode(n):
    head=genlinklist.genrl(20)
    cur=head
    tail=head
    for i in range(n):
        print(tail.data,'->',end='')
        tail=tail.next
    while tail.next:
        print(tail.data,'->',end='')
        tail=tail.next
        cur=cur.next
    return cur
print()
print(nthnode(10).data)
