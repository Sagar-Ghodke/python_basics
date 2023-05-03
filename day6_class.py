# in class wants to represent data so using --->variable

'''Types of variable to decleare inside class:'''
# 1.instance variable: delceare at object level (using self variable in constructure)
# sysnanomous name to object

# 2. static vriable: decleare at class level
# inside class
# outside method
# access by:class name(recomended as we can access and modify too) or object(only access)

# 3.Local variable: decleareat function level


''' 3 types of method to decleare at class:'''
#     Class method
#     Static method
#     Instance Method


'''object'''
    # its instance of class.
    # basic runtime entity of objectet oriented system
    # by using object we can communicated with data member and member function of class   

# Syntax of object :-
#                       referencevariablename = classname()
# Ex:                   obj = Student()


''' Self variable:-'''
# 1. by using self variable we pointing to the current object
# 2. self is a default argument
# 3. self is like this keyword in java
# 4. instead of writing self we can write any other name
# 5. in class level or in function first argument must be self
    
'''Constructor'''
# 1. Here in python the name of the constructor is __init__(self).
# 2. Constructor call automatically whenever we create object or we can say that at the time of creation of object.
# 3. By using constructor we initialize the object.
# 4. There is no mandatory to declare a constructor inside class but if we are not going to declare constructor so python provide default constructor.
# 5. Constructor will execute only one time when we create a object.
# 6. Always we have to pass one argument in constructor(self)
    
    
'''Types of variable'''

''' Instance variable:-'''
# Instance is a synonymous name to object or we can say that any value that varied from object to object that are called as instance variable
# Ex:- 50 is a instance of type int
# For every object a separate copy of instance variable created
# We can declare instance variable using self keyword inside a constructor


'''example'''    
'''1'''   

# class Student:
#     roll_number=101
#     num1= 50
#     num2=100 # data member
#     def add(self): #member function
#         print(self.num1+self.num2) 
#         self.name=input("Enter name:") 
#         print(self.name)
    
# obj=Student()
# obj.add()
# print(obj.roll_number)

#add, mul, div, sub by using class 
#SI, Factorial, Fibnacci'''



'''2'''

# class New:
#     x=10 # data member inside of class
    
#     def display(self): # data member function of class 
#         print('hello python')
# obj = New()
# obj.display()
# print(obj.x)
# #print(obj.a)



'''3'''

# class NewClass:
#     def __init__(self): #constructor 
#         print("my name is constructor and i allways execute first")
        
#     def show(self): #member function inside of class 
#         print('welcome to class level programming')
# obj = NewClass()
# obj.show()
# #obj2 = NewClass()


'''4'''

# class Hod:
#     def __init__(self): # constructor 
#         self.name='sonali' #data member 
#         self.empid=1001
#         self.age=21
#     def info(self): # instance method 
#         print("My name is ", self.name) 
#         print("My Age is: ", self.age) 
#         print("My emp id: ", self.empid)
# obj = Hod() #object create
# obj.info()



'''5'''

# class Hod:
#     def __init__(self, name, age, rollno): # parameterize constructor
#         self.name=name
#         self.age = age
#         self.rollno=rollno
#     def show(self):
#         print('name', self.name)
#         print('age ', self.age)
#         print('rollno', self.rollno)
        
# obj=Hod('Arjun',45,101)
# obj.show()



'''6'''
#declaring instance variable inside a constructor by using self variable.
# class Student:
#     def __init__(self):
#         self.s_name ="cyber"
#         self.l_name ="envy" # instance variable
#         self.s_rollno = 101
#         self.s_branch = "CS"
#         self.s_mb=1234567890
        
# obj = Student()
# print(obj.__dict__)


'''7'''
# #declaring instance variable inside a instance method by using self variable.
# class Student:
#     def __init__(self):
#         self.s_name = "cyber"
#         self.s_rollno= 101
#         self.s_branch="CS"
        
#     def getdata(self): # instance method 
#         self.s_mb = 28282828282
        
# obj=Student() # untill and unless we call the method it will not not added to the object
# #obj.getdata()
# print(obj.__dict__)



# declaring instance variable outside a class by using object
# class Student:
#     def __init__(self):
#         self.s_name ="cyber"
#         self.s_rollno= 101
        
#     def getdata(self):
#         self.s_mb = 28282828282
        
# obj = Student()
# obj.getdata()
# obj.s_branch = "CS" # adding instance variable by using object
# print(obj.__dict__)


'''8'''
#accessing and deleting instance variable from the class
# class Student:
#     def __init__(self):
#         self.s_name =input("Enter your name")
#         self.s_rollno= 101
        
#     def getdata(self):
#         self.s_mb = 28282828282
    
# obj=Student()
# obj.getdata()
# obj.s_branch = "CS" # adding instance variable by using object
# del obj.s_rollno    # deleteing a instance variable
# print(obj.s_name)
# print(obj.__dict__)




'''for every object a seprate copy of instance variable created but in case of static variable only 
one copy will be created and it is accessble for every object of the class'''

# class College:
#     collegename="DPU College" #static variable (1 memory)
        
#     def __init__(self):
#         self.studentname = "Sagar" #instance varible (3 seprate memory)
        
# principal =College() # object creation
# teacher = College()
# accountant =College()

# print("principal=", principal.collegename, "....", principal.studentname)
# print("teacher", teacher.collegename, "....", teacher.studentname)
# print("accountant=", accountant.collegename, "....", accountant.studentname)


# College.collegename="Sinhgad" # second way to add static variable  
#                           #(changes for all as same mmemory location)
# principal.studentname="sonali" #creates separate memory locations for all 
#                                      #hence will be printed only once


# print("principal=", principal.collegename, "|", principal.studentname)
# print("teacher=", teacher.collegename, "|", teacher.studentname)
# print("accountant=", accountant.collegename, "|", accountant.studentname)




'''instance method example'''
# class Student:
#     def __init__(self, name, rollno, mob): 
#         self.name=name # instance variable 
#         self.rollno=rollno
#         self.mob=mob
        
#     def display (self): # instance method 
#         print(self.name," ", self.rollno, " ", self.mob)
# stud = Student ("cyber", 1001, 6464646464) 
# stud.display()



'''# static method'''

# class Student:
#     # by using class name we can access static method 
    
#     @staticmethod # decorator 
#     def get_personal_detail (firstname, lastname): 
#         print("your personal detail=", firstname, lastname)
        
#     @staticmethod
#     def contact_detail (mobil_no, rollno):
#         print("your contact detail-", mobil_no, rollno)
        
# Student.get_personal_detail("cyber", "envy")
# Student.contact_detail (5456454646, 1001)