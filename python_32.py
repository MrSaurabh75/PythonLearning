# Set Methods
s1 = {1,2,3,4,5,6,7,8,9}
s2 = {11,12,13,14,15,2,6,8,9}

# 1.union() & intersection()
print(s1.union(s2))
print(s1.intersection(s2))

# 2.update() and intersection_update()
# s1.update(s2)
# print(s1)
# s1.intersection_update(s2)
# print(s1)

# symmetric_diffrence()
# s3 = s1.symmetric_difference(s2)
# print(s2)

# diffrence() and diffrence_update()
s3 = s1.difference(s2)
print(s3)