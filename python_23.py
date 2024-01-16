# List Methods
list1 = [4,5,6,78,9,0,1,2,3,4,5,6,7]

# 1.list.sort()
list1.sort() #Acending order
print(list1)

list1.sort(reverse=True) #Decending order
print(list1)

# 2.index()
print(list1.index(4))

# 3.count()
print(list1.count(4))

# 4.copy()
m = list1.copy()
m[0]=45
print(list1)
print(m)

# 5.append()
list1.append(322)
print(list1)

# 6.insert()
list1.insert(1,499)
print(list1)

# 7.extend()
list2=[12000,1300,1400]
list1.extend(list2)
print(list1)

# Concatinate a list
list3 = list2+list1
print(list3)
