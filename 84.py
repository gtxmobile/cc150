
def getPerm(word):
    pers=[]
    if word==None:
        return None
    if len(word)==0:
        pers.append(" ");
    else:
        c=word[0]
        remain=word[1::]
        remper=getPerm(remain)
        for per in remper:
            for i in range(len(per)):
                pers.append(insertcat(per,c,i))
    return pers

def insertcat(word,c,i):
    return word[0:i]+c+word[i::]


print(getPerm("abfaewfad"))

