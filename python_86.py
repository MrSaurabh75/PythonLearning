# Walrus operator 
a = True
print(a:=False)
# Walrus operator in while loop
x = [1,2,3,4,5,6,7,88]
while(n:=len(x))>0:
    print(x.pop())
# Walrus operator in if-else 
names = ["Saurabh","Mahesh","Laxman","Shiv","Rudra"]
if(name:=input("Enter Your Name: ")) in names:
    print(f"Hello {name}")
else:
    print(f"Invalid name {name}")