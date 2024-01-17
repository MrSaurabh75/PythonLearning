# DOC Strings --> Python doc strings are the string that appear after the defination of a function,method,class or module
def square(num):
    '''
    This is a function returns a square of entered number
    '''
    return num**2

user = int(input("Enter a number : "))
print(square(user))
print(square.__doc__)

# PEP 8 (Python Enhancement Proposal)
# The Zen of Python --> A poem by tim Peters arise by entering import this in cmd 