
class CallHander:
    LEVEL=3
    NUM_FRESHERS=5
    employeels=['']*3
    callqueue=[]
    def getCallHandl(c):
        for i in range(c.rank,LEVEL):
            el=employeels[i]
            for e in el:
                if e.free:
                    return e
        return None

class Call:
    def __init__(self):
        self.rank=0
    def reply(self,message):
        pass
    def disconnect(self):
        pass

class Employer:
    def __init__(self,r):
        self.rank=r



class Fresher(Employer):
    def __init__(self):
        super(Fresher,self).__init__(0)

class TechLead(Employer):
    def __init__(self):
        super(Fresher,self).__init__(1)

class ProductManager(Employer):
    def __init__(self):
        super(Fresher,self).__init__(2)

