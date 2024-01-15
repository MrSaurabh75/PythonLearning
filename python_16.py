# Match Case Statement in Python

import os
os.system("python --version")

x = int(input("Enter a number :"))
match x:
    case 10:
        print("X is 10")
    case 20:
        print("X is 20")
    case 30:
        print("X is 30")
    case 40:
        print("X is 40")
    case 50:
        print("X is 50")
    case 60:
        print("X is 60")
    case _:
        print("Enter from a 10-20-30-40-50-60")

a = int(input("Enter a number : "))
match a :
    case _ if(a>10) and a<50:
        print("a is between 10-50")
    case _ if(a>50 and a<100):
        print("a is between 50-100")