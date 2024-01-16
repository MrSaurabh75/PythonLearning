# List --> 1.List are ordered collection of data items 2.They store multiple items in a single variable 3.List items are seprated by commas and enclosed in a square brakets[] 4.List are changable means mutable we can alter a list after creation 
l = [1,2,3,4,5]
print(type(l))
print(l)

l2 = [1,2,"Saurabh"]
print(type(l2))
print(l2)
print(l2[0])
print(l2[1])
print(l2[2])

# finding element in a list
if 7 in l:
    print("Yes")
else:
    print("No")

# Jump index

print(l[:4:2])

# List Comprihention
lst=[i for i in range(4)]
print(lst) 

# Prime numbers 
prime =[i for i in range(50) if i%2==0]
print(prime)

