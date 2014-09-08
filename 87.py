
cents=[25,10,5,1]
def caln(n,denom,arr):
    if denom==1:
        arr.append(str(n)+'*1')
        print(arr)
        return 1
    ways=0
    for i in range(n//denom):
        if i>0:
            arr.append(str(i)+'*'+str(denom))
        arr2=arr[::]
        if i>0:
            arr.pop()
        ways+=caln(n-i*denom,cents[cents.index(denom)+1],arr2)
    return ways

print(caln(53,cents[0],[]))

