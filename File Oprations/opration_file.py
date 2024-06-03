# File I/O
# open opration:
# syntax
# f = open("file_name","mode")
# data = f.read()
# f.close()

# Read Opration :
# f = open("myfile.txt","r")
# con = f.read()
# print(con)
# print(type(con))
# f.close()

# # Read Specific range of characters:
# f = open("myfile.txt","r")
# data = f.read(5)
# print(data)
# f.close()

# Use of readline()
# f = open('myfile.txt','r')
# data = f.readline()
# print(data)
# f.close()

# Use of readlines()
# f = open('myfile.txt','r')
# data = f.readlines()
# print(data)
# f.close()

# Write Opration : 
# There are tio types of write mode one is 'w' mode which is overwrite mode and another is 'a' mode which is append mode

# write mode:
# f = open('myfile.txt','w')
# write_data = f.write("Hello Mr.Saurabh Chorge")
# f.close()

# append mode:
# f = open('myfile.txt','a')
# append_data = f.write('\nEvery setback is the setup for comeback')
# f.close()

# with open("myfile.txt","r") as f:
#     data = f.read()
# print(data[::-1])

# import os 
# os.remove("myfile.txt")

# Practice Question

# 1.Create a new file practice.txt using python. Add the following data in it.
# Hi everyone
# we are learning File I/O
# using Java.
# I Like Programming
# i = ["Hi everyone","\nwe are learning File I/O","\nusing Java.","\nI Like Programming"]
# with open("practice.txt","w") as f:
#     f.writelines(i)

# with open("practice.txt","r") as f:
#     data = f.read()
# new_data = data.replace("Java","Python")
# print(new_data)
# with open("practice.txt","w") as f:
#     f.write(new_data)

# Write a program to replace all comment char. from a string
# write_data = "Hello a i am the comment charater \n having a comment in it \n deserve comment and \nus replacing comment"
# with open("practice.txt","w") as f:
#     f.write(write_data)
# with open("practice.txt","r") as f:
#     data = f.read()
# new_data = data.replace("comment","user")
# word = "raja"
# if(data.find(word)!=-1):
#     print("Present")
# else:
#     print("Not-Present")
# print(new_data)
# with open("practice.txt","w") as f:
#     f.write(new_data)

# write_data = ["I am writing this because","\nI am learning File I/O with java","\nhello world in java"]
# with open("sample.txt","w") as f:
#     f.writelines(write_data)
# with open("sample.txt","r") as f:
#     data = f.read()
# word = "raj"
# if(data.find(word)!=-1):
#     print(f"{word} is present")
# else:
#     print(f"{word} is not present")
# new_data=data.replace("java","python")
# print(new_data)
# with open("sample.txt","w") as f:
#     f.write(new_data)

# def check_word(word):
#     with open("sample.txt","r") as f:
#         data = f.read()
#     if(data.find(word)!=-1):
#         print(f"{word} is present")
#     else:
#         print(f"{word} is not present")
# check_word("raj")

# def check_word(word):
#     with open("sample.txt","r") as f:
#         data = f.read()
#     if(data.find(word)!=-1):
#         print(f"{word} is present")
#     else:
#         print(f"{word} is not present")
# def check_line(word):
#     data = True
#     line_no=1
#     with open("sample.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 break
#             line_no+=1
# check_line("File")

# with open("sample.txt","r") as f:
#     data = f.read()
# num = data.split(",")
# print(num)
# for i in num:
#     typecast_i = int(i)
#     if(typecast_i%2==0):
#         print(typecast_i)

# with open("sample.txt","r") as f:
#     data = True
#     line_no = 1
#     word="learning"
#     while data:
#         data = f.readline()
#         if(data.find(word)!=-1):
#             print("Present")
#         else:
#             print(-1)

# with open("sample.txt","r") as f:
#     data = f.read()
# num = data.split(",")
# count=0
# for i in num:
#     if(int(i)%2==0):
#         print(i)
#         count+=1
    
# print(f"Count is {count}")

