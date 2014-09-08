#-*- coding:utf-8 -*-
#求一个节点的后继

def succesor(node):
    if not node:
        return None
    if node.right or not node.p:
        ln=node.right
        while ln.left:
            ln=ln.left
        return ln
    np=node.p
    while np:
        if node==np.left:
            return np
        node=np
        np=np.p
    return None
