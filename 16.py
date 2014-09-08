
#matrix rotate
import random
a=[[random.randint(10,99) for j in range(10)] for i in range(10)]
def rotate(a,n):
    row=len(a)-1
    col=row
    for i in range(row//2):
        for j in range(i,col-i):
            tmp=a[i][j]

            a[i][j]=a[row-j][i] #left->up

            a[row-j][i]=a[row-i][col-j] #bottom->left

            a[row-i][col-j]=a[j][col-i] #right->bottom

            a[j][col-i]=tmp
for b in a:
    print(b)
print()
rotate(a,10)
for c in a:
    print(c)
