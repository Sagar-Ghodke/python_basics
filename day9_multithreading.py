# to apply mylti threading-task should be independent to each



# Main thred programs
# import threading
# print("Hellow world: ")


# print("hello world", threading.current_thread().getName())

# here current_thread() return Thread object
# here getName()method return current executing thred name


# Creating a thread without using any class
# from threading import *
# import threading
# import time

# def activate(): #user define method
#     for i in range(1,11):
#         time.sleep(2)
#         print("this is chid thread\n")
        
# t=Thread(target=activate)#creating thread object
# t.start() #starting of thread
# # ---------------------------------------------child thread=========

# for i in range(1,11):
#     time.sleep(2)
#     print("This is main thread",)


'''when we call start()method then thread will creeat
-------------------------------==================-------------------
(second way to create thread Class
Whenever we all start() methid then automatically run()
method will be executed and performs our job'''

# from threading import *
# import time
# class MyThread(Thread):
#     def run(self):
#         for i in range(10):
#             time.sleep(2)
#             print("Child Thread-1")
# obj_t=MyThread()
# obj_t.start()
# ----------------------------------Main thread section------------------------
# for i in range(10):
#     time.sleep(2)
#     print("Main Thread-1")

# Creating a Thread without extenting Thread classs:
    
# from threading import *
# class Mytest:
#     def display(self):
#         for i in range(10):
#             print("Child Thread \n")
# obj=Mytest
# t=Thread(target=obj.display)
# t.start()
# # ------------------------------------Main Thrad-------------------------
# for i in range(10):
#     print("Main Thread \n")



# with multithreding we can see same pragram
# from threading import *
# import time

# def add(num):
#     for n in num:
#         time.sleep(1)
#         print("Add=",2*n,"\n")
# def mul(num):
#     for n in num:
#         time.sleep(1)
#         print("Mul=",n*n,"\n")
# def sub(num):
#     for n in num:
#         time.sleep(2)
#         print("sub:",n-n)


'''Synchronization'''


    