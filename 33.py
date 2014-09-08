
import random

thres=5
stacks=[[]]
nindex=0
top=-1
staindex=[]
def push(a):
    global top
    global nindex
    stacks[nindex].append(a)
    top+=1
    if top==thres:
        top=-1
        stacks.append([])
        nindex+=1

def pop():
    global nindex
    global top
    if top==-1:
        if nindex==0:
            print("down overlap has no yuansu")
        else:
            top=thres-1
            nindex-=1
            stacks.pop()
    else:
        top-=1
    return stacks[nindex].pop()

def popAt():
    pass

for i in range(20):
    push(random.randint(1,30))

print(stacks)
for i in range(20):
    pop()
    print(stacks)
