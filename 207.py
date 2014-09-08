def flstmdof2(a):
    a=sorted(a,key=len)
    a.reverse()
    for ai in a:
        for j in range(1,len(ai)-1):
            if ai[:j] in a and ai[j::] in a:
                return ai

a=['test','tester','testertest','testing','testdingtester']
print(flstmdof2(a))


