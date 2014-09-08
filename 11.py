
a='abcadfaeratag'
def cntall(a):
    b=[0 for i in range(28)]
    asca=ord('a')
    for c in a:
        if b[ord(c)-asca]==1:
            print('false')
            return False
        else:
            b[ord(c)-asca]=1
    print('true')
    return True
cntall(a)
cntall('abdc')
