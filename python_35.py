# else in for loop 

for i in range(9):
    print(i)

else:
    print("No i")


for i in range(9):
    print(i)
    if i ==8:
        break
else:
    print("No i") # it doesn't run

# else with while loop 
i = 1
while i<=5:
    print(i)
    i = i+1
    
else:
    print("Submited")