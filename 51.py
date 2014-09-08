
def msubn(m,n,i,j):
    maxn=~0
    left=maxn-(1<<j)+1
    right=maxn-(1<<i)+1
    mask=left|right
    return (n&mask)|(m<<i)

