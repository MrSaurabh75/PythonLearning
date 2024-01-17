# Recursion --> The function that calls itself again and again is called as recursive function and this process is called as recursion

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

