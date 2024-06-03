# Write a python program to check the year is leap year or not
# user = int(input("Enter the year :"))
# if(user%4==0 and user%100!=0 or user%400==0):
#     print(f"{user} Year is leap year!")
# else:
#     print(f"{user} not a leap year")

# Write a program to check the entered number by user is prime or not
# user=int(input("Enter the number : "))
# for i in range(2,user+1):
#     if(user%i==0):
#         break
# if(user==i):
#     print(f"{user} is a Prime Number")
# else:
#     print(f"{user} is not a Prime Number!")

# Program to print sum of all even numbers between 1 to 20
# sum=0
# for i in range(1,20+1):
#     if(i%2==0):
#         sum = sum+i
# print(f"Sum of 1 to 20 even numbers is {sum}")

# Write a program to find the factorial of a number
# user=int(input("Enter a number : "))
# fact = 1
# if(user==0 or user==1):
#     print(f"Factorial of {user} is 1")
# else:
#     for i in range(1,user+1):
#         fact=fact*i
#     print(f"Factorial of {user} is {fact}")

# Write a program to find out reverse of a given number
# user=1234
# rev=0
# while user>0:
#     rem=user%10
#     rev=rev*10+rem
#     print(f"{rem}",end="")
#     user=int(user/10)

# Write a program to print the sum of digits of a given number
# user = 1234
# sum=0
# while user>0:
#     rem = user%10
#     sum = sum+rem
#     user=int(user/10)
# print(f"{sum}")

# Write a program to check wheather the number is Armstrong or not
# user = int(input("Enter the number : "))
# u = user
# sum=0
# while user>0:
#     rem=u%10
#     sum = sum+rem*rem*rem
#     u = int(u/10)
# if user == sum :
#     print(f"{user} is a Armstrong Number")
# else:
#     print(f"{user} is not a Armstorng Number")

# Write a program to show the functionality of try,except,finally and else
# try:
#     age=int(input("Enter your age :"))
#     if(age<18):
#         raise Exception(age)
# except Exception:
#     print("Age is too small")
# else:
#     print("Yppu are eligible!")
# finally:
#     print("Running finally cluase")

# Write a programt to create a user defined exception
# class Error(Exception):
#     pass
# class AgeSmallException(Error):
#     pass
# try:
#     age = int(input("Enter your age : "))
#     if(age<18):
#         raise AgeSmallException(age)
# except AgeSmallException:
#     print(f"{age} is too small!")

# Create the program that calculates the time of a threads
# import threading
# import time
# def fun(sec):
#     print(f"Function is sleep for {sec}")
#     time.sleep(sec)
# time_cal = time.perf_counter()
# fun(4)
# fun(3)
# fun(2)
# time_cal2 = time.perf_counter()
# print(time_cal2-time_cal)

# Above code by creating the thread
# import threading
# import time
# def fun(sec):
#     print(f"Thread is sleep for {sec}")
#     time.sleep(sec)
# t1 = threading.Thread(target=fun,args=[4])
# t2 = threading.Thread(target=fun,args=[3])
# t3 = threading.Thread(target=fun,args=[2])
# time_cal=time.perf_counter()
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
# time_cal2=time.perf_counter()
# print(time_cal2-time_cal)

# Create a program that onw thread calculate the cube and snother thread square of number
# import threading
# import time
# def cube(num):
#     print(f"Cube of {num} is {num**3}")
# def square(num):
#     print(f"Square of {num} is {num**2}")

# a = int(input("Enter the number :"))
# b = int(input("Enter the number :"))
# t1 = threading.Thread(target=cube,args=[a])
# t2 = threading.Thread(target=square,args=[b])

# t1.start()
# t2.start()
# t1.join()
import threading
def even():
    for i in range(10,31):
        if i%2==0:
            print(i," is even")
def odd():
    for i in range(10,31):
        if(i%2!=0):
            print(i,' is odd')

t1 = threading.Thread(target = even)
t2 = threading.Thread(target=odd)
t1.start()
t2.start()