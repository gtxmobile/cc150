
path=[]

def get_path(x,y):
    p=point(x,y)
    path.append(p)
    if x==0 and y==0:
        return True
    suc=False

