
def getsub1(sset):
    maxn=i<<len(sset)
    allsub=[]
    for i in range(maxn):
        subset=[]
        k=i
        idx=0
        while k>0:
            if (k&1)>0:
                subset.append(sset[idx])
            k>>=1
            idx+=1
        allsub.appned(subset)
    return allsubsets

