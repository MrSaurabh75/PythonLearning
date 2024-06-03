import re
information='''
Mr. Saurabh Chorge
8998-8374-83
Address - Near Rnamla Hotel

Mr Adarsh Jadhav
9474.4747.85
Address - Near Bhuleswar Colony

Mrs Sahil Shinde
4574*4094*90
Address - Near Bhuleswar Colony

Mrs. Pranv Lala
4574&4094&90
Address - Near Bhuleswar Colony

Mr.Sushant Pawar
9457.2763.44
Address - Near Bhuleswar Colony

Mr Sushant Pawar
1212..2763.44
Address - Near Bhuleswar Colony

Sushant Pawar
400.2763.44
Address - Near Bhuleswar Colony

Sushant Pawar
500.2763.44
Address - Near Bhuleswar Colony
'''

# pattern = re.compile(r'\d\d\d\d.\d\d\d\d.\d\d')
# matches = pattern.finditer(information)
# for i in matches:
#     print(i)

# pattern = re.compile(r'\d\d\d\d[.-]\d\d\d\d[.-]\d\d')
# matches = pattern.finditer(information)
# for i in matches:
#     print(i)

# pattern = re.compile(r'[45]00[.-]\d\d\d\d[.-]\d\d')
# matches = pattern.finditer(information)
# for i in matches:
#     print(i)

# pattern = re.compile(r'[A-Z]\w\w\w\w\w\w\s[A-Z]\w\w\w\w\w')
# pattern2 = re.compile(r'[A-Z]\w\w\w\w\w\w')
# matches = pattern.finditer(information)
# matches2 = pattern2.finditer(information)
# for i in matches:
#     print(i)
# for j in matches2:
#     print(j)

# pattern = re.compile(r'Mr[s]?\.?\s[A-Z]\w+')
# matches = pattern.finditer(information)
# for i in matches:
#     print(i)

emails = '''
saurabhdc7575@gmail.com
sahilshide@gmail.com
wkdwqiugduweihf iuwe
dkehfuef @gmail.com
AdarshJadhav27@gmail.com
sushantpawar0707@university.edu
'''
# pattern = re.compile(r'[a-zA-z]\w+[0-9]?@[a-zA-Z]\w+\.(com|edu)')
# matches = pattern.finditer(emails)
# for i in matches:
#     print(i)

# Write a program to take the name of user and check it 
# name = input("Enter your name :")
# pattern = re.compile(r'[A-Za-z]\w+\s[A-Za-z]\w+')
# matches = pattern.finditer(name)
# for i in matches:
#     print(i.group())
  
# Write a program to check the password is validate or not
# import re 
# password = input("Enter the password to validate :")
# lower_case = re.compile(r'[a-z]')
# upper_case = re.compile(r'[A-Z]')
# digit= re.compile(r'\d')
# special_Char = re.compile(r'[@$#*]')
# if len(password)<8:
#     print("Invalid Password,Length is too short!")
# elif len(password)>20:
#     print("Invalid Password,Length is too Large!")
# elif not lower_case.search(password):
#     print("Invalid Password,Password does not contain a lower case character!")
# elif not upper_case.search(password):
#     print("Invalid Password,Password does not contain a upper case character!")
# elif not special_Char.search(password):
#     print("Invalid Password,Password does not contain a special character!")
# elif not digit.search(password):
#     print("Invalid Password,Password does not contain a digit character!")
# else:
#     print("Password is Valid!")

# Write a program to check the email is validate or not
# import re 
# email = input("Enter your e-mail : ")
# check_email = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
# if check_email.search(email):
#     print("Valid E-mail")
# else:
#     print("Invalid Email")

# Write a program to check the email is validate or not
# import re
# url = input("Enter URL : ")
# check_url = re.compile("((http|https)://)(www.)?"+"[a-zA-Z0-9@._:%\\+&#?//]"+"{2,256}\\.[a-z]"+"{2,6}\\b([a-zA-Z0-9@:%"+"._\\+~&#//=]*)")
# if check_url.search(url):
#     print("valid URL")
# else:
#     print("Invalid URL")

# Write a program to remove all leading zeros from a ip address
# import re
# ip1 = '233.344.008.89'
# ip2 = '233.004.08.89'
# result1 = re.sub(r'\.[0]*','.',ip1)
# result2 = re.sub(r'\.[0]*','.',ip2)
# print(result1)
# print(result2)

# Write a program to accept the string from user and show the five char. words from it
# import re 
# str = input("Enter the string :")
# obj = re.search(r'\w\w\w\w\w\w',str,re.I)
# print(obj.group())
