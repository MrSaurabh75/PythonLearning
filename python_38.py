# Raising custom error 
a = int(input("Enter a number between 1 to 10 : "))
if(a<1 or a>10):
    raise ValueError("Please Enter a number between 1 to 10")

