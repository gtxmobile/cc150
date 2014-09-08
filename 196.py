
num2str=['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen']
shistr=[]
ershistr=['','Ten','Twenty','Thirty']
def ptho(n):
    if (n/100 > 1):
        print(num2str[int(n/100)],' Hundred and ')
    n%=100
    if(n<20):
        print(num2str[n])
    else:
        print(ershistr[int(n/10)]+'')
        n%=10
        print(num2str[n])

def pnum(n):
    if n>999:
        high=int(n/1000)
        low=n%1000
        ptho(high)
        print('Thousand,')
    else:
        low=n
    ptho(low)

pnum(1234)
