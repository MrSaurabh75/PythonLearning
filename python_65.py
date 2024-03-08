# Static Method 
class Math:
    def __init__(self,num):
        self.num=num
    def addNum(self,n):
        self.num=self.num+n
    @staticmethod
    def add(a,b):
        return a+b

m = Math(5)
print(m.num)
m.addNum(6)
print(m.num)
print(m.add(5,6))
