
#-*- coding:utf-8 -*-
#这是个好题 有一个五面的骰子 获取7以内的随机数

from random import randint

def rand5():
    return randint(1,5)
def rand7():
    a=1
    for i in range(3):
        r5=rand5()
        if r5==3:
            continue
        elif r5<3:
            a|=(1<<i)
    print(a)
    return a
for i in range(10):
    rand7()
