# Set Methods
s1 = {1,2,3,4}
s2 = {5,6,7,2,6,8,9}

# 1.union() & intersection()
# print(s1.union(s2))
# print(s1.intersection(s2))

# 2.update() and intersection_update()
# s1.update(s2)
# print(s1)
# s1.intersection_update(s2)
# print(s1)

# symmetric_diffrence()
# s3 = s1.symmetric_difference(s2)
# print(s3)

# diffrence() and diffrence_update()
# s3 = s1.difference(s2)
# print(s3)

# s3 = s2.difference_update(s2)
# print(s3)

# isdisjoint()
print(s1.isdisjoint(s2))

# issuperset()
print(s1.issuperset(s2))

# issubset()
print(s1.issubset(s2))

# add()
s2.add(12)
print(s2)

# remove() or discard()
# s2.remove(23)
# print(s2)
# s2.discard(23)
# print(s2)

# pop()
# s2.pop()
# print(s2)

# del()
# del s2 

# clear()
# s2.clear()

# if item exist
# if 2 in s2:
#     print("Yes")
# else:
#     print("None")

