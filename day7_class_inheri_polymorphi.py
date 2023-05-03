
# 2. Class Methods:
# Inside method implementation if we are using only class variables (static variables),
# then such type of methods we should declare as class method.
# We can declare class method explicitly by using @classmethod decorator.
# For class method we should provide cls variable at the time of declaration 
# We can call class method by using classname or object reference variable.

# class Animal:
#     legs=4
#     @classmethod
#     def walk(cls, name):
#         print('{} walks with {} legs...'.format(name,cls.legs))
# Animal.walk('Dog')
# Animal.walk('Cat')



# Inner class:-
'''
When we declare class inside another class that are called as inner class
Why we should go for inner class?
When without existing one type of object there will be no chance to exist another type of object that time we should go for inner class
Syntax:- class classname:
            ----------
            
            class classname:
                 ----------
'''


# Garbage Collection in python
'''
As a programmer in C and C++ language we have responsibility to creating and deleting a objects.
In development time we know that where and when we have to create a object
but at the deleting time we forget to delete the object and at runtime of
application, so many unused objects take memory so memory related issues may
come over there.
In python we have garbage collection concept which running in background continuously to finding unused object and delete that objects also. I
By using garbage collector the probability of application failure due to memory issues is very less.'''

# Garbage collector program

# import gc 
# print(gc.isenabled())
# gc.disable() 
# print(gc.isenabled())
# gc.enable() 
# print(gc.isenabled())



# class Student:
#     roll_number = 101
#     num1 = 50
#     num2 = 100 # data member
#     print(self.num1+self.num2)
    
#     def add(self): #member function 
#         print(self.num1+self.num2)
#         self.name=input("Enter name:")
#         print(self.name)



# Destructors:-
'''
Destructor is a special type of method, for destructor we use __del__ 
Internally garbage collector and destructor maintaining very good co-ordination, how? Let see....

Before destroying object garbage collector call destructor to perform clean up operation 
like resources deallocation closing a database connection. Garbage collector waiting 
till the destructor completing its work because after that garbage collector destroy objects.
'''


'''# Destructor example'''

# class Sample:

#     def __init__(self): 
#         print("i am constructor")
#     def _del_(self): 
#         print("i am destructor i am calling for clean up code")
# obj = Sample()
# print("end")

# #------------------------------------------------------------------------------




# Inheritance in python
'''Extending property from one class to another class is called inheritance.
Directly we are getting here reusability concept

• Base class: A class which inherits its property to another is called base class or parent class.
• Derived class: A class in which properties are inherited called as derived class or child class.
'''
    # types of inheritance

    #     1. Single Inheritance
    #     2. Multilevel Inheritance
    #     4. Multiple Inheritance
    
    
# class Faculty: # parent class
#     def __init__(self, f_name, dpartment, f_id):
#         self.f_name = f_name
#         self.dpartment = dpartment
#         self.f_id = f_id
#     def print_info(self): 
#         print('faculty information=',self.f_name, self.dpartment, self.f_id)
        
# obj = Faculty("Ashish", "computer_science", 1001)
# obj.print_info()

# #-------------------------------------------------------------------------------------------
# class Cse (Faculty):#child class
#     pass #no statement
# obj = Cse("Jyoti mam", "computer_science", 1002) 
# obj.print_info()

# #--------------------------------------------------------------------------------------------
# class Me (Faculty): # child class
#     pass
# obj = Me("xyz mam", "science", 1003)
# obj.print_info()



'''# # Single level inheritance'''

# class College: # parent class 
#     def college_name(self): 
#         print("Modern College")
        
# class Student (College): # child class 
#     def student_info(self): 
#         print("Name: cyber envy") 
#         print("Branch: Mechanical")
        
# obj = Student()
# obj.college_name() 
# obj.student_info()



'''Multilevel inheritance '''

# class College: #first class first- level
#     def college_name(self):
#         print("Modern College")
        
# class Student (College): #second class second - level 
#     def student_info(self):
#         print("Name: cyber envy") 
#         print("Branch: Mechanical")
        
# class Exam (Student): #child class 
#     def subject(self):
#         print("Subject1: Designe Engineering")
#         print("Subject2: Math")
#         print("Subject3: C-Language")
        
# obj= Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()




'''polymorphism'''
# runtime polymorphism-late bindinf dynamic binding


# only operater overloading supported by oython

'''polymorphism example'''

# class Principal: 
#     def role (self): 
#         print("i am managing all activity of college")
# class Dean: 
#     def role (self):
#         print('Dean= I am decision taking person')
# class Hod:
#     def role(self):
#         print('Hod= I have responsibility of Teachers and Students')
# class Faculty:
#     def responsibility(self):
#         print('Faculty I have to complete syllabus successfully')

# #.......................class declaration completed.................................
# def func(obj): # called func obj =1: Dean
#     obj.role() # calling func
    
# campus=[Principal(), Dean(), Hod(), Faculty()]

# for obj in campus: #obj =[0:princial(),1: Dean(), 2: Hod()]
#     func(obj) # calling fun'''




#The problem in this approach is if obj does not contain role() method then we will get Attribute 
# class Principal:
#     def role (self):
#         print("Principal= I am visiting in campus")
        
# class Dean:
#     def order(self): 
#         print('Dean= I am decision taking person')
        
# def call(obj): # called fun 
#     obj.role()
        
# obj = Principal() # creating object of principal class 
# call(obj) # calling fun

#But we can solve this problem by using has attr() function.
# here solution
# class Principal:
#     def role(self): 
#         print("Principal= I am visiting in campus")
# class Dean: 
#     def order(self):
#         print('Dean= I am decision taking person')
        
# def call (obj): # called function
#     if hasattr(obj, 'role'): 
#         obj.role()
#     elif hasattr(obj, 'order'):
#         obj.order()
        
# obj = Principal() # creating object of principal class 1 
# call(obj)# calling fun
# obj = Dean() # creating object of dean class 2 
# call(obj) # callling fun


# print('sagar'+'bhai')
# print(2+2)
# print(2.5+2.5)

#print('sagar'*3)
#operator overloading
#operator overloading internally implemented by using magic method

# class Deposit:
#     def __init__(self, cash): 
#         self.cash = cash
# d1=Deposit (1000)
# d2=Deposit (2000)
# print(d1+d2)

# magic method avilable for every operator To overload any operator we have to override that method in our classs
#the_add_ method is a magic method which gets called when we add two numbers using the + operator
# class Deposit:
#     def __init__(self, cash):
#         self.cash = cash
#     def _add_(self, other): #magic method
#         return self.cash + other.cash
# d1=Deposit (1000)
# d2=Deposit (2000)
# print("Total cash deposit amount=", d1+d2)


#in Python Method overloading is not possible.
#If we are trying to declare multiple methods with same name and #different number of arguments then Python will always consider only last method. '''

# class Arithmatic:
#         def add(self,a):
#             print(a)
#         def add(self,a,b):
#             print(a+b)
#         def add(self,a,b,c):
#             print(a+b+c)
# obj = Arithmatic()
# j.add(10)
# obj.add(10,20)
# obj.add(1,2,3) 


# To handel overloaded method in python
#if method with variable number of arguments required then we can handle with default argu
# class Arithmatic:
#         def add(self, a=None, b=None, c=None):
#             if a!=None and b!=None:
#                 print(a+b)
#             elif a!=None and b!=None and c!=None: 
#                 print(a+b+c)
#             else:
#                 print("enter atleast two argument")
# obj = Arithmatic()
# #obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)


# Constructure overlioading
#Constructor overloading is not possible in Python.
#If we define multiple constructors then the last constructor will be considered.
# class Arithmatic: 
#     def __init__(self):
#         print("There is no argument") 
#     def __init__(self,a): 
#         print("passing one argument") 
#     def _init__(self,a,b):
#         print("passing two arguments")
# obj = Arithmatic()
# obj = Arithmatic(10)
# obj = Arithmatic(2,2)



'''function over loading'''
# same name dufferent ARGUMENT
'''operator overloading'''
# same operator for duffernt purposes
# python suports operator overloading
'''ex. + operator does addition and also concatination of strings '''

'''method overloading'''
# corelating with inheritance
# parent class property by default availabe for child class, meance child can also use parent property
# if chind not happy with property he can redefine his own property as per requirement
# this is method overlading

# overring supports both method and constructure overriding


'''1'''
# class Father: # parent class 
#     def bike(self): 
#         print("Bike: harley Devidson")
#     def laptop(self):
#         print("Laptop: laptop with 2GB RAM and 500GB HDD 13 processor")
        
# class Aman(Father): # child class
#     def laptop(self): # method overiding
#         print("As per my programming software requarment this is not cool for me")
        
#         print("laptop with 8GB RAM and 1TB HDD 17")
# obj = Aman()
# obj.bike()
# obj.laptop()


'''2'''

# class Father:
#     def __init__(self):
#         print("Father:= i am on time at breakfast table")
# class Child (Father):
#     def __init__(self):
#         print("Child:= i will be late for breakfast")
# obj = Child()



'''3'''
# class Father:
#     def __init__(self):
#         print("Father:= i am on time at breafast table")
# class Child (Father):
#     def __init__(self):
#         # using super() method we can call parent class constructor 
#         print("Child:= i will be late for breakfast") 
#         super().__init__()
# obj = Child()

