# Exercise 6 : Library Management System
class Library:
    def __init__(self,tb,ib):
        self.tb=tb
        self.ib=ib
    def info(self):
        print("Library Status")
        print("--------------")
        print(f"{self.tb} out of {self.tb-self.ib} are available")

user = int(input("How many books are issued by students :"))
l = Library(1100,user)
l.info()