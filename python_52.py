# Lambda Function : It is useful in writing a anonymous function
# def double(x):
#     return x*2

# double = lambda x:x*2
# print(double(5))

# Write a lambda function to print the avreage of 3 subject marks
avg = lambda x,y,z:(x+y+z)/3
print(avg(70,69,46))

# Write a lambda function to print the cube of user entered number
cube = lambda x:x*x*x
print(cube(5))

def app(fx,value):
    return fx(value)
print(app(cube,5))

