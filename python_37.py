# finally 

def div(x,y):
    try:
        c=x/y
        print(c)
    except:
        print(f"You entered {y} which is not allow")
    finally:
        print("Finally Block")


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
div(a,b)

