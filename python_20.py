# functions --> i.Built-In Function
#               ii.User Define Function
def avg(a,b):
    avrage = (a*b)/(a+b)
    print(avrage)

def maxmin(a,b):
    if(a>b):
        print(a," is grater")
    elif(a<b):
        print(a," is lesser")
    elif(b<a):
        print(b," is lesser")
    else:
        print(b," is grater")

x = int(input("Enter a first number : "))
y = int(input("Enter a second number : "))

avg(x,y)
maxmin(x,y)

