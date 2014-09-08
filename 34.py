
#hanno recursion

def moveDisks(n,orign,dest,buf):
    if n>0:
        moveDisks(n-1,orign,buf,dest)
        moveTopTo(orign,dest)
        moveDisks(n-1,buf,dest,orign)

def moveTopTo(orign,dest):
    top=orign.pop()
    if len(dest) and dest[-1]<=top :
        print "error",top
    else:
        dest.append(top)
        #print "Movedisk ",top," from "+"to"

orign=range(20,1,-1)
print orign
buf=[]
des=[]
moveDisks(19,orign,des,buf)
print des
print buf,orign


