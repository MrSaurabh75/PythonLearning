# Enumerate Function

mylist=[11,2,3,34,5,56,6,45]
for index,i in enumerate(mylist):
    print(i)
    if(index==3):
        print("You are at third")  

myString = ["Saurabh","Digambar","Chorge"]
for index,i in enumerate(myString):
    print(i)
    if(index==0):
        print(f"Hello {i}")
    