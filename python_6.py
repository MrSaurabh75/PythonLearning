# Variables --> Variables are the container that holds data like integer,float,boolean,
a = 12
# a is a name of variable and value is 12
b = 13
c = 12.78
x = "Saurabh"
y = True
z = None
print(a)
print(b)
print(c)
print("The type of a is ",type(a))
print("The type of a is ",type(c))
print(a+b)
print(x)
print("The type of x  is ",type(x))
print("The type of y  is ",type(y))
print("The type of z  is ",type(z))

#Complex number
i = complex(8,4)
print(i)

# Sequence Data : 
'''
list --> i. List is collection of a diffrent data elements
         ii.List is mutable means you can change list
         iii.List is inclose in square breces 
'''
list1 = [1,2,3,"Saurabh","Raj","Laxman","Mahesh",[12,34,5,6]]
print(list1)

'''
tuple --> i.A tuple is a orderd collection of data
          ii.Tuple is immutable means you cannot change tuple
          iii.Tuple is inclose in round breces 
'''
tuple1 = (("Saurabh","Raj",1,2,3,("Laxman","Mahesh")))
print(tuple1)

# Mapped data :
'''
dict -->i.Dictionary is collection of key-value pairs
        ii.Dictionary is a unorderd collection of data elements
        iii.Dictionary is inclose in curly breces 
'''
dict1 = {"RollNo":45,"Name":"Saurabh","Class":"12th A","Age":18}
print(dict1)

# Note :- In python anything is a object 