import random

stack=[]
minstack=[]
top=-1
mintop=-1
def push(a):
    stack.append(a)
    global top
    global mintop
    top+=1
    if mintop==-1:
        minstack.append(a)
        mintop+=1
    else:
        if a<=minstack[mintop]:
            minstack.append(a)
            mintop+=1

def pop():
    global top
    global mintop
    tmp=stack.pop()
    top-=1
    if tmp==minstack[mintop]:
        minstack.pop()
        mintop-=1
        if stack[top]<=minstack[mintop]:
            minstack.append(stack[top])
            mintop+=1
    return tmp

def min():
    return minstack[mintop]
for i in range(100):
    push(random.randint(59,80))
print(stack)
print(minstack)
for i in range(len(stack)):
    pop()
    print(minstack)



