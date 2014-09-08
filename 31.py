
stacksize=100
stack=[0]*3*100

from genlinklist import *

stackindex=[-1]*3
top=0
def push(stacknum,a):
    index=stackindex[stacknum]
    sn=Node(a,None,index)
    stackindex[stacknum]=top
    stack[top]=sn
    top+=1

def pop(stacknum):
    index=stackindex[stacknum]
    stackindex[stacknum]=stack[index].prev
    stack[index]=None
    return stack[index].value

def isEmpty(int stanum):
    return stackindex[stanum]==-1

def peek(int stanum):
    return stack[stackindex[stanum]].value

