# Tuple --> 1.Tuples are ordered collection of data items. 2.They stored multiple items in a single variable. 3.Tuple items are seprated by commas and enclosed within a round brakets (). 4.Tuples are cannot alter means it is immutable once we created a tuple we cannot change it 
t = (1,2,3,4,5,6,7,89)
t2 = ("Saurabh","Laxman","Raj","Mahesh")
t3 = (1) 
t4 = (76,89,"Hello","World")
print(type(t))
print(type(t2))
print(type(t3)) #prints the type as int because python treated it a int to overcome that problem we have to give a comma after a single int like (1,)
print(t4)

if 78 in t:
    print("Present")
else:
    print("Not Present")
    print(t[:-1])