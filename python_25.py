# Tuple Methods --> We cannot change existing tuple if we want to change it we have convert to copy it into a list then you can change it indirectly 
t = (1,2,3,45,3,6,3,3,7)
t2 = ("Mahesh","Ganesh")
temp = list(t)
temp.append("Saurabh")
print(temp)

# we can concatinate a tuple 
t3 = t + t2
print(t3)

#count()
print(t.count(3))

#index()
print(t.index(3,3,8))
print(t.index(45))

#len()
print(len(t))