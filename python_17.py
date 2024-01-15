# Loops --> 

# 1.for loop
name = 'Saurabh'
for i in name :
    print(i)

list1 = [1,2,3,4,5,6,7,8,9,0]
for e in list1:
    print(e)

for k in range(60):
    print(k)
for k in range(1,60):
    print(k)
for k in range(50,60,5):
    print(k+1)
    
# Multiplication table
table = int(input("Enter a Number : "))
for m in range(1,11):
    print(table ," X ", m ," = ",(table*m))