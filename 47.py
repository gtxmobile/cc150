
#-*- coding: utf-8 -*-

def isSubTree(tl,ts):
    if not tl:
        return False
    if tl.data=ts.data:
        if bianli(tl,ts):
        return True
    else:
        return bianli(tl.left,ts)|bianli(tl.right,ts)

#对于大树中的每个节点都遍历小树一遍
def bianli(tl,ts):
    if not ts:
        return True
    if not tl:
        return False
    if tl.data!=ts.data:
        return False
    return bianli(tl.left,ts.left) & bianli(tl.right,ts.right)

