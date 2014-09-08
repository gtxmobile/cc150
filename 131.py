


def printklin(fn,k):
    xa=['']*k
    fd=open(fn,'r')
    i=0
    for l in fd:
        xa[i%k]=l
        i+=1
    if i<k:
        print(xa[:j])
    else:
        print(xa[(i%k)::],xa[:(i%k)])

printklin('1.txt',5)
