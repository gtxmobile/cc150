
#-*- coding: utf-8 -*-
#著名的八皇后问题

#首先是检查该方案是否合理

rowcnt=16
col4row=[-1]*rowcnt
def check(row):
    for i in range(row):
        dif=abs(col4row[i]-col4row[row])
        if dif==0 or dif==row-i:
            return False
    return True
def plaquen(row):
    global rowcnt
    if row==rowcnt:
        printBoard()
        return True
    for i in range(rowcnt):
        col4row[row]=i
        if check(row):
            plaquen(row+1)

def printBoard():
    global rowcnt
    for i in col4row:
        for j in range(rowcnt):
            if j==i:print(j,end='');
            else: print('- ',end='');
        print()
    print()

plaquen(0)
print(col4row)
