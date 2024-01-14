# # Excercise No.1
# Question --> Create a python program that greet user with his name according to morning, evening and night

# Answer -->
import time
clock = time.strftime('%H:%M:%S')
print(clock)
clock1 = int(time.strftime('%H'))
print(clock1)
clock = time.strftime('%M')
print(clock)
clock = time.strftime('%S')
print(clock)

if(clock1>7 and clock1<12):
    print("Good Morning")
elif(clock1>=12 and clock1<17):
    print("Good Afternoon")
elif(clock1<20):
    print("Good Eveing")
else:
    print("Good Night")