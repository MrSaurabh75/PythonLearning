# Write a Program to demonstrate a year entered by the user is leap year or not
# user = int(input("Enter a year : "))
# if(user%4==0 and user%100!=0 or user%400==0):
#     print(user," is a Leap Year")
# else:
#     print(user," isn't a Leap Year")

# Write a program to demonstrate a number entered by user is prime or not
# user = int(input("Enter a number : "))
# for i in range(2,user+1):
#     if (user%i)==0:
#         break
# if i==user:
#     print(user," is a prime number")
# else:
#     print(user," is not a prime number")

# Write a program to calculate the sum of even numbers from 1 t0 20
# sum = 0
# for i in range(1,21):
#     if i%2==0:
#         print(i)
#         sum+=i
# print("Sum of even numbers : ",sum)

# Write a program to find factorial of a number entered by user
# n = int(input("Enter a Number : "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(f"Factorial of {n} is {fact}")

# Write a program to reverse a number entered by user
# n = int(input("Enter a number : "))
# print(f"Enter Number is {n}")
# rev=0
# while(n>0):
#     rem = n%10
#     rev=rev*10+rem
#     n = int(n/10)
# print(f"Reverse Number is {rev}")

# Write a program to calculate the sum of digits of a number entered by user
# n = int(input("Enter a number : "))
# sum=0
# while(n>0):
#     rem = n%10
#     sum = sum+rem
#     n = int(n/10)
# print(f"Sum of digits of a number is {sum}")

# Write a program to check wheather the number is armstrong or not
# n = int(input("Enter a Number : "))
# sum=0
# num=n
# while(n>0):
#     rem=n%10
#     sum = sum+rem*rem*rem
#     n=int(n/10)
# if num==sum:
#     print(num," is armstrong")
# else:
#     print(num," is not armstrong")

# Program to find the GCD of two positive numbers.
# m = int(input("Enter a first positive Number : "))
# n = int(input("Enter a second positive Number : "))
# if m==0:
#     print(f"GCD is {n}")
# elif n==0:
#     print(f"GCD is {m}")
# while m!=n:
#     if m>n:
#         m = m-n
#     elif n>m:
#         n=n-m
# print(f"GCD of two numbers is {m}")

# Program to print multiplication table of the given number.
# num = int(input("Enter a Number : "))
# for i in range(1,10+1):
#     print(f"{num} X {i} = {num*i}")

# Write a program to check wheather the string is palindrome or not
# str = input("Enter a String : ")
# if str==str[::-1]:
#     print("String is palindrome !")
# else:
#     print("String is Not palindrome !")

# Write a program to check wheather the number is palindrome or not
# n = int(input("Enter a number : "))
# num=n
# rev=0
# while(n>0):
#     rem = n%10
#     rev = rev*10+rem
#     n = int(n/10)
# if num==rev:
#     print("Number is Palindrome")
# else:
#     print("Number is Not-Palindrome")

# Write a program to return prime numbers in a given list
# list1=[3,2,9,10,43,7,20,23]
# l=[]
# print("Prime Numbers in a list are : ")
# for a in list1:
#     prime=True
#     for i in range(2,a):
#         if a%i==0:
#             prime=False
#             break
#     if prime:
#         l.append(a)
# print(l)

# Print a pattern of * using loop
# *
# * * 
# * * *
# * * * *
# * * * * *
# for i in range(0,5):
#     for j in range(0,i+1):
#         print("* ",end="")
#     print("\r")

# Print a pattern 
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5 
# for i in range(0,5):
#     num = 1
#     for j in range(0,i+1):
#         print(num, end="")
#         num = num+1
#     print("\r")

# Print a pattern 
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# num = 1
# for i in range(0,4):
#     for j in range(0,i+1):
#         print(f"{num} ", end="")
#         num+=1
#     print("\r")