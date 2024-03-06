# Decorators : It is the function that takes a function as a argument and returns the modified function
def greet(fx):
    def mfx():
        print("Hello Mr")
        fx()
        print("Thanks For Visit")
    return mfx

@greet
def name():
    print("Saurabh")

name()


# With arguments
def greet(fx):
    def mfx(*args,**kwargs):
        print("Hello Mr")
        fx(*args,**kwargs)
        print("Thanks For Visit")
    return mfx
@greet
def add(a,b):
    print(a+b)

add(5,7)