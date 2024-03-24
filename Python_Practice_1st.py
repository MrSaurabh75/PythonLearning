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