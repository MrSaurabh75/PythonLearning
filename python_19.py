# break and continoue statement

a = int (input("Enter a number : "))
for i in range(1,15):
    print(a,"X",i,"=",a*i)
    if(i==10):
        break

b = int(input("Enter a number : "))
for j in range(20):
    print(j)
    if(j==10):
        print("Skip the itration")
        continue
