# Local and Global variables
# Local Variables are the variables that has a scope within the function in which they are defined.
# Globle Variables are the variables that has a scope in entire program.

x = 12
def scope():
    y = 10
    print(f"Globle Variable : {x}")
    print(f"Local Variable : {y}")

scope()
print(f"Globle Variable : {x}")
# print(f"Local Variable : {y}") gives an error : name 'y' is not defined

