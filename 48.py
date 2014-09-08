#-*- coding utf-8 -*-

def findpath(r,he,buf,level):
    if not :return;
    tmp=he
    buf.append(r.data)
    for i in range(0,level,-1):
        tmp-=buf[i]
        if tmp==0: ptree(buf,i,level);
    c1=buf[::]
    c2=buf[::]
    findpath(r.left,he,c1,level+1)
    findpath(r.right,he,c2,level+1)

def ptree(buf,beg,end):
    for i in range(beg,end):
        print(buf[i]," ",end="")




