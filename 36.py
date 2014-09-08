from random import randint

class BigStack:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self,a):
        print a
        if not len(self.s1):
            self.s1.append(a)
        else:
            while self.s1 and a<self.s1[-1]:
                self.s2.append(self.s1.pop())
            self.s1.append(a)
            while self.s2 and self.s2[-1]:
                self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop()
    def IsEmpty(self):
        return len(self.s1)==0
    def peek(self):
        return self.s1[-1]

bs=BigStack()
for i in range(1,20):
    bs.push(randint(1,100))
print bs.s1
