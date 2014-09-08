import math
def contfac0(n):
    cnt2=0
    cnt5=0
    for i in range(1,n+1):
        tmp=i
        while(tmp%2==0):
            cnt2+=1
            tmp/=2
            #print(tmp)
        while(tmp%5==0):
            cnt5+=1
            tmp/=5
    print(min(cnt2,cnt5))

contfac0(50000)
