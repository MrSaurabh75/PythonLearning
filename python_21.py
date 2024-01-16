# function arguments
# 1.Required Arguments
def avrage(a,b):
    print((a+b)/2)

avrage(2,3)

# 2.Defualt Arguments
def sum(x=10, y=34):
    print(x+y)
    
sum()

def sub(p=10, q=34):
    print(p-q)

sub(q=8)

# 3.Keyword Arguments

def mul(p=10, q=34):
    print(p*q)

mul(q=8,p=3)

# 4.Variable length Arguments
def avg(*num):
    s = 0
    for i in num:
       s= s+i
    print(s/len(num))

avg(2,5,3,6,2,8,7)

def Name(**name):
    print("Hello Mr.",name["fname"],name["mname"],name["lname"])

Name(fname = "Saurabh",mname = "Digambar",lname = "Chorge")

# return sattement
def multi(a,b):
    return a*b

print(multi(2,5))