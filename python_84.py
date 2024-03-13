# # Time Module
# import time
# def UsingWhile():
#     i=0
#     while i<100:
#         i+=1
#         print(i)
# def UsingFor():
#     for i in range(100):
#         i+=1
#         print(i)        
# init=time.time()
# UsingWhile()
# print(time.time()-init)
# UsingFor()
# print(time.time()-init)

import time
print(4)
time.sleep(4)
print("This is printed after 4 seconds")

t = time.localtime()
forwarded_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(forwarded_time)