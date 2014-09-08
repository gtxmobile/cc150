
from genlinklist import *
qlist=[]
ququ=[]
def mkll4tree(root):
    ququ.append(root)
    while ququ:
        llen=len(ququ)
        a=[]
        flag=-1;
        for i in range(llen):
            cur=ququ.pop(0)
            n=Node(cur.data)
            flag+=1
            if flag:
                a[flag-1].next=n
            a.append(n)

            if root.left:ququ.append(root.left)
            if root.right:ququ.append(root.right)
        qlist.append(a)

