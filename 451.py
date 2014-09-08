#-*- coding:utf-8 -*-
#求一个节点的后继

def checkBST(n,minm=MIN,maxm=MAX):
    if n==None:
        return True
    if n.data <= minm or n.data>maxm:
        return False
    if not checkBST(n.left,minm,n.data) or checkBST(n.right,n.data,maxm):
        return False
    return True

