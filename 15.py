


def repspa(str1):
    spacnt=0
    for a in str1:
        if a==' ':
            spacnt+=1
    b=[0 for i in range(spacnt*2+len(str1))]
    blen=len(b)-1
    for j in range(len(str1)-1,-1,-1):
        c=str1[j]
        if c==' ':
            b[blen]='0'
            blen-=1
            b[blen]='2'
            blen-=1
            b[blen]='%'
            blen-=1;
        else:
            b[blen]=c
            blen-=1;

    print(b)

a='fawe faewj faejio fawe '
repspa(a)
