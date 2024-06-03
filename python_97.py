# thread
# Normal Method
# import threading
# import time
# def fun(sec):
#     print(f"Stops for {sec}sec")
#     time.sleep(sec)
# time1 = time.perf_counter()
# fun(5)
# fun(4)
# fun(3)
# fun(1)
# time2 = time.perf_counter()
# print(time2-time1)

# Treading Method
# import threading
# import time
# def fun(sec):
#     print(f"Started a tread of {sec}sec")
#     time.sleep(sec)
# t1 = threading.Thread(target=fun,args=[5])
# t2 = threading.Thread(target=fun,args=[4])
# t3 = threading.Thread(target=fun,args=[3])
# t4 = threading.Thread(target=fun,args=[1])
# time1 = time.perf_counter()
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# time2 = time.perf_counter()
# print(time2-time1)

