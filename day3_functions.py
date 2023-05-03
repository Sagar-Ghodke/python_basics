# What is function /
'''Function is a self contained block which is executed separately
If suppose we want to execute a single statement or group of statement again and again 
then there is no need write this statement each time, 
so we can define this statement as single unit so as per our requirement we can call it any number of times
So this unit is function
By using function program readability and reusability both will happen'''

# Two Types of Function
# 1. Built in function
# 2. User define function

# 1. Built in function:
        # Built in function:predefine function
        # already inside library
        # Eg:= type(), id(), input(), print(), eval()
        
        
'''types of argument passed in function: 4 types --->>>multiplw values at a time possible
1.defaulf
2.positional
3.keyword 
4.variable length'''

''' passsing fun as argument in python

 Python program to illustrate functions 
 can be treated as objects '''
    
# def shout(text): 
#     return text.upper() 
# print(shout('Hello')) 
# yell = shout 
# print(yell('Hello')) 

''' Python program to illustrate functions
can be passed as arguments to other functions'''

# def shout(text):
# 	return text.upper()

# def whisper(text):
# 	return text.lower()

# def greet(func):
# 	# storing the function in a variable
# 	greeting = func("Hi, I am created by a function passed as an argument.")
# 	print(greeting)

# greet(shout)
# greet(whisper)


# -------------------------------------------------------------------------------

# import time

# def msg(): # called function
#     print("hello world")
# msg() # calling function
# time.sleep(2)
# msg()
# time.sleep(2)
# msg()



# def add(num1,num2): 
#     return num1+num2
# result = add (2,3) # calling function 
# print("Result =", result)



# def info(firstname, lastname): # called function positional argument 
#     print('First name=', firstname) 
#     print('Last name=', lastname)
# info('sagar','ghodke') # calling function



# def arithmatic(a,b): # called function
#     r = a+b
#     n = a*b
#     m = a-b
#     return r,n,m
# result = arithmatic (10,5) #calling function 
# print("Result = ", result)



# def func(fname,lname): #called function 
#     print("Hi", fname)
#     print("Hi", lname)
# func(fname="cyber",lname="envy") #calling function

# fname = input("Enter first name") #by user input
# lname = input("Enter last name")
# func(fname, lname) #calling function

# keyword arguments:
# We can pass argument values by keyword.i.e by parameter name.
# here order is not matter but argument should be matched


'''default argument'''
# def func(city = "Nagpur"): # called function 
#     print("I am from ", city )
# func("Delhi") # calling function
# func("LA")
# func()



'''unknown argument'''
# def func (**name): # called function 
#     print("my name is ",name)
    
# func(fname = "cyber", Iname = "envy") # calling function


'''variable length argument/ variable number of argument'''
# def name (*name):
#     print(name)
# name("Ashish", "cyber", "Tushar", 1001)


'''# Anonymous Functions: Sometimes we can declare a function without any name, 
# such type of nameless functions are called anonymous functions or lambda functions 
# lambda argument_list: expression
# Note: Instant use or one time use of anonymous function'''


# s=lambda n:n*n
# print("The Square of 4 is ",s(4)) 
# print("The Square of 5 is :",s(5))

# val=lambda a,b:a+b 
# print("The Sum of 10,20 is: ", val(10,20)) 
# print("The Sum of 100,200 is: ", val(100,200))


#Note: ambda Function internally returns expression value and we are not required to write return
# When we want to pass func as argument then lambda func is best choice


# single line
# we can use lambda function with filter(), map(), reduce
# function alising is possible in python

'''Nested function'''

# def myname(): # outer function
#     print("my name is sagar")
# def myrollno(): # inner function 
#     print('my rollno is TMHC38') 
# myrollno() # calling function 
# myname() # outer calling function'''


# ---------------------------------------------------------------------------------------
'''Generator 
Decorator'''

# Generators
# This is function and which generate sequence wise value Here the declaration is similar as like normal declaration of function but for returning value it uses yield keyword
# Advantages
# 1. Generators are very easy
# 2. It improves memory utilization as well as performance
# 3. If we want to read data from large file then generator are best choice


# def myname(): #called function
#     yield 'p'
#     yield 'r'
#     yield 'a'
#     yield 's'
#     yield 'h'
#     yield 'a'
#     yield 'n'
#     yield 't'
# output= myname() # calling function
# print(type (output))
# # print(output)
# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))