
def genpair(l,r,word,cnt):
    if l<0 or r<l:
        return False
    if l==0 and r==0:
        print(''.join(word)," ",end="")
    else:
        if l>0:
            word[cnt]='('
            genpair(l-1,r,word,cnt+1)
        if r>l:
            word[cnt]=')'
            genpair(l,r-1,word,cnt+1)


n=6
genpair(n,n,['']*2*n,0)


