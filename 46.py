#-*- conding: utf-8 -*-

#分情况讨论一下
#如果两节点同为一个节点的左子树，同为右子树的情况也是一样的

#方法1直接递归遍历
def f1(root,p,q):
    if not root:
        return None
    if root==p or root==q:
        return root
    left=f1(root.left,p,q)
    right=f1(root.right,p,q)
    if not left and not right:
        return root
    if not left:
        return left
    if not right:
        return right
    return None

#cc150的解法

#首先定义个covers方法 查找子树中有多少个目标节点

def covers(root,p,q):
    ret=0
    if root=None:
        return ret
    if root==p or root==q:
        ret+=1
    ret+=covers(root.left,p,q)
    if ret==2:
        return ret
    ret+=covers(root.right,p,q)

def lca(r,p,q):
    if p==q and (r==p or r==q):return r;
    cntl=covers(r.left,p,q)
    if cntl==2:
        if r.left==p or r.left==q:return r.left;
        else: return lca(r.left,p,q);
    elif cntl==1:
        if root==p: return p;
        elif root==q: return q;
    cntr=covers(r.right,p,q)
    if cntr==2:
        if r.right==p or r.right==q:return r.right;
        else: return lca(r.right,p,q);
    elif cntr==1:
        if root==p: return p;
        elif root==q: return q;
    if cntl==1 and cntr==1:
        return r
    else:
        return None




