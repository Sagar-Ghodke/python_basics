# from abc import ABC, abstractmethod

# class Programming(ABC): # abstract class
#     @abstractmethod
#     def training(self): # abstract method 
#         pass
#     @abstractmethod # abstract method
#     def placement(self): 
#         pass
    
# class Ashish (Programming): 
#     def training(self):
#         print("java trainng")
#     def placement(self): 
#         print("Java placement")
        
# class Ankush (Programming): 
#     def training(self): 
#         print("Python | Django") 
#     def placement(self): 
#         print("Python placement students")
        
# class cyber (Programming): 
#     def training(self): 
#         print("Machine learning") 
#     def placement(self): 
#         print("Data science placement")
# I
# obj1 = Ashish()
# obj1.training()
# obj1.placement()

# obj2 = Ankush()
# obj2.training()



# WAP for ticket booking

from abc import ABC, abstractmethod

class Irctc (ABC): #abstract class
    @abstractmethod
    
    def bookTicket(self): # abstract method
        pass
    
class MakeMyTrip (Irctc):
    def bookTicket(self):
        print("I Welcome To Yatra.com ")
        source = input("Enter a source station name")
        destination = input("Enter destination name")
        date = input("Enter date")

class Goibibo(Irctc):
    def bookTicket(self):
        print("welcome to goibibo")
        source = input("Enter a source station name")
        destination = input("Enter destination name")
        date = input("Enter date")
        
class Yatra(Irctc):
    def bookTicket(self):
        print("welcome to yatra")
        source = input("Enter a source station name")
        destination = input("Enter destination name")
        date = input("Enter date")
        
x=input("-------------------------------\n\
Welcome, Enter Your Prefered site for ticket booking of the following: \
    \n1.MakeMyTrip\
        \n2.Goibibo\
            \n3.Yatra\
                \n--------------------------------\n:")      

obj=x
obj.bookTicket()

        