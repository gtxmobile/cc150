#-*- coding:utf-8 -*-
#ÅÐ¶ÏÁ½×Ö·û´®ÊÇ·ñ°üº¬ÏàÍ¬×Ö·û´®

def judgeang(str1,str2):
    bitvec=[0 for i in range(260)]
    asca=ord('a')
    unicnt=0;
    for c in str1:
        if not bitvec[ord(c)-asca]:
            unicnt+=1
        bitvec[ord(c)-asca]+=1
    comcnt=0
    for i in range(len(str2)):
        ascc=ord(str2[i])-asca
        if not bitvec[ascc]:
            print('false')
            return False
        bitvec[ascc]-=1
        if not bitvec[ascc]:
            comcnt+=1
            if comcnt==unicnt:
                return i==len(str2)-1
    return False
a1='adteqa'
a2='daqe'
print(judgeang(a1,a2))
