# 'is' compares exact location of a object in memory
# '==' compares values of two objects

a = 4
b = '4'
print(a is b)
print(a == b)

c = 45
d= 45
print(c is d) #This prints true the c and d are stored in same location because python does not waste a memory to store the same int and string (constants) to store at different locations.  
print(c == d)

l1 = [1,2,3,4]
l2 = [1,2,3,4]
print(l1 is l2) #This prints false because the list is mutable so the python stores l1 and l2 in diffrent locations.
print(l1 == l2)

