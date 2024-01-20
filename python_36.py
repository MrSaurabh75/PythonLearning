# Exception Handling in python --> exception handling is the process of responding to unexpected events when a computer program runs. Exception handling deals with these  events to avoid the progra or sysytem crashing and without this process, exception would disrupt the normal oprations of a program
a = input("Enter a number : ")

try:
    for i in range(1,11):
        print(f"Multiplication table for {a} :")
        print(f"{int(a)} X {i}:{int(a)*i}")
except Exception as e:
    print(e)
    print("Invalid input")
