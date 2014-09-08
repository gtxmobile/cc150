#-*- coding:utf-8 -*-
import random
class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
#随机生成一个链表

def genrl(n):
    head=Node(0);cur=head
    for i in range(n):
        cur.next=Node(random.randint(1,9))
        cur=cur.next
    return head

def plnklist(head):
    i=0
    while head.next and i<40:
        print(head.data,'->',end='')
        head=head.next
        i+=1
    print(head.data)

if __name__=='__main__':
    node=genrl(10)
    plnklist(node)
    plnklist(node)

def gensl(n):
    head=Node(0)
    cur=head
    for i in range(1,n):
        cur.next=Node(i)
        cur=cur.next
    return head
#生成一条大小为n的顺序链表

def makehuan(head,k):
    while k>0:
        head=head.next
        k-=1
    tail=head
    while tail.next:
        tail=tail.next
    tail.next=head



