# Conditional Oprators 
a = int(input("Enter a 1st number"))
b = int(input("Enter a 2nd number"))
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)

# if-else statement
a = int(input("Enter a number : "))
if(a<0):
    print("Number is negative")
elif(a>0):
    print("Number is positive")
    if(a<=10):
        print("number is bet 1-10")
        print("Sure!")
        