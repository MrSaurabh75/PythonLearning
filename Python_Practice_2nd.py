# Write a python program to show the year is leap or not
# year = int(input("Enter the year :"))
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("Leap Year")
# else:
#     print("Not-Leap year")

# Write a program to show the given nummber is prime or not
# num = int(input("Enter the number: "))
# for i in range(2,num+1):
#     if num%i==0:
#         break
# if(i==num):
#     print("Prime number")
# else:
#     print("Not Prime")

# Write a program to print sum of all numbers between 1 to 10
# sum=0
# for i in range(1,10):
#     sum = sum+i
# print(sum)

# Write a program to print even numbers from 1 to 20
# sum=0
# for i in range(1,21):
#     if(i%2==0):
#         sum = sum+i
# print(f"Sum of even numbers between 1 to 20 is {sum}")

# Write a program to find factorial of a number
# num = int(input("Enter the number: "))
# fac = 1
# for i in range(1,num+1):
#     fac = fac*i
# print(f"Factorial of a number {num} is {fac}")

# Write a program to print the given number in reverse
# num = int(input("Enter a number: "))
# rev=0
# while num>0:
#     rem = num%10
#     rev = rev*10+rem
#     num = int(num/10)
# print(rev)

# Write a program to find the sum of digits of a given number
# num = int(input("Enter the number:"))
# sum =0
# while(num>0):
#     rem = num%10
#     sum = sum+rem
#     num = int(num/10)
# print(sum)

# Write a Program to show the given number is armstrong or not
# num = int(input("Enter the number: "))
# nums=num
# sum=0
# while(num>0):
#     rem = num%10
#     sum = sum+rem**3
#     num = int(num/10)
# if(nums==sum):
#     print("Armstrong number")
# else:
#     print("Not Armstrong")

# Write a Program to find GCD
# m = int(input("Enter the 1st number:"))
# n = int(input("Enter the 2nd number:"))
# if m==0 and n ==0:
#     print("Invalid Input")
# if m==0:
#     print(f"GCD is {n}")
# if n==0:
#     print(f"GCD is {m}")
# while m!=n:
#     if m>n:
#         m=m-n
#     if n>m:
#         n=n-m
# print(f"GCD is {m}")

# Write a program to demostrate the given string is palindrome or not
# str = input("Enter a String:")
# if(str==str[::-1]):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Write a program to accept the string from user and remove vowels from it
# str = input("Enter a String: ") 
# for i in str:
#     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
#         continue
#     print(i,end="")

# Write a program to check the string is palindrome or not
# user = input("Enter a string : ")
# rev = user[::-1]
# if(user == rev):
#     print(f"Given String is palindrome ")
# else:
#     print("Not Palindrome")

# Write a python program to create a built in function 
# def add(a,b):
#     print(a+b)
# add(4,5)

# Write a recursive function to calculate the factorial 
# def fac(n):
#     if(n==1 or n==0):
#         return 1
#     return n*fac(n-1) 
# f = fac(5)
# print(f)  

# import re
# text = "Hello Python Programming"
# pattern = re.compile(r"[A-Za-z]\w+ing$")
# matches = pattern.finditer(text)
# for match in matches:
#     print(match.group())

# import re
# text = "Hello I am going to make a Program to find the five words from a string"
# pattern = re.compile(r"\w\w\w\w\w")
# ms = pattern.search(text)
# print(ms.group())

# import re
# text = "I am writing 8 a program to 89 search the numbers from a given6 string"
# pattern = re.compile(r'(\d\d|\d)')
# ms = pattern.finditer(text)
# for i in ms:
#     print(i.group())

# import re
# text = "I am writing a program to find saurabhdc7575@gmail.com the email address from sushantpawar@gmail.com the string"
# pattern = re.compile(r'[a-z]\w+[0-9]?[@]gmail.com')
# ms = pattern.finditer(text)
# for i in ms:
#     print(i.group())

# import re
# password = input("Enter your password to validate : ")
# lower_case = re.compile(r'[a-z]')
# upper_case = re.compile(r'[A-Z]')
# digit = re.compile(r'\d')
# special_char = re.compile(r'[@]')
# if len(password)<8:
#     print("Invalid Passwaord,It is too short")
# elif len(password)>20:
#     print("Invalid Passwaord,It is too long")
# elif not lower_case.search(password):
#     print("Invallid Password,It doesn't contain lower case charachter")
# elif not upper_case.search(password):
#     print("Invallid Password,It doesn't contain upper case charachter")
# elif not digit.search(password):
#     print("Invallid Password,It doesn't contain digit")
# elif not special_char.search(password):
#     print("Invallid Password,It doesn't contain special charchter")
# else:
#     print("Permission Granted!!!")

# Write the program to show ZeroDivisionError in python
# try:
#     a = int(input("Enter the 1st number :"))
#     b = int(input("Enter the 2nd number :"))
#     result = a/b
#     print(result)
# except ZeroDivisionError:
#     print("You cannot divide any number with zero")

# Write a program to show the funcctionality of raise statement
# try:
#     age = int(input("Enter Your age : "))
#     if(age<18):
#         raise Exception
#     else:
#         print("You can drive a car")
# except Exception:
#     print("You Cannot Drive age < 18")

# Write a Program to raise an user defined exception
# class Error(Exception):
#     pass
# class AgeSmallException(Error):
#     pass
# class InvalidAgeException(Error):
#     pass
# try:
#     age = int(input("Enter your age to validate : "))
#     if(age<18):
#         raise AgeSmallException
#     elif(age>100):
#         raise InvalidAgeException
#     else:
#         print("You are Eligible!")
# except AgeSmallException:
#     print("Age is to small!")
# except InvalidAgeException:
#     print("Age is to large!")
# finally:
#     print("Finally Cluse is running!")

# Write a program to except an number from a user and raise a error in try block if the number is out of range
# num = int(input("Enter the number : "))
# try:
#     if(num<1 or num>10):
#         raise ValueError(num)
# except ValueError:
#     print(f"{num} is out of range!")
# else:
#     print(f"{num} in a range!")

# 