

n_1=0
n_2=0
def fab(n):
    global n_1
    global n_2
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fab(n-1)+fab(n-2)
        n_2=fab(n-2)
        return n_1+n_2

print(fab(10))
