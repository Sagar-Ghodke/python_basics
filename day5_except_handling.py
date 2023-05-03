# 1.SyntaxError
# 2.RuntimeError

# exceptional handling(run time error)

# try:
#     print(2/0)
# except ZeroDivisionError as message: # division by zero 
#     print("The description of exception:",message) 
    
    
    
#     # multiple except block
# try:
#     a=int(input("enter first integer no")) # $
#     b=int(input("enter second integer no")) 
#     print(a/b)
# except ZeroDivisionError as message:
#     print("plz ensure that you can't divide any no by zero: ", message)
# except ValueError as message:
#     print("Enter only interger no=>", message)  
    
    
    
#Handling multiple diffrent kinds of exception with single except block.
# try:
#     a=int(input("enter first integer no")) 
#     b=int(input("enter second integer no")) 
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print(message) 


# The concept of default except block, generly we used for writng normal message or showing no ''
# try:
#     a=int(input("enter first integer no")) 
#     b=int(input("enter second integer no")) 
#     print(a/b)
# except(ValueError, ZeroDivisionError) as message: 
#     print("Enter correct number: ", message) 
# except:
#     print("This is default part of except block")


#IMP: If we have requarment of multiple except block then in that switiation default except blo 
# should be in last other wise syntax error will encounter '''

'''
try:
    a=int(input("enter first integer no")) 
    b=int(input("enter second integer no")) 
    print(a/b)
except:
    print("This is default part of except block") 
except (ValueError, ZeroDivisionError) as message: 
    print("Enter correct number: ", message)
    
'''

# We can use else block if no error will genrate it is depend on our own need and neccessity '''
# try:
#     a=int(input("enter first integer no"))
#     b=int(input("enter second integer no")) 
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message: 
#     print("Enter correct number: ", message)
# else:
#     print("Everything is ok")
    
    
# Finally block will always executed whether try block genrate error or not '''
# try:
#     a=int(input("enter first integer no")) 
#     b=int(input("enter second integer no")) 
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message: 
#     print("Enter correct number: ", message) 
# finally:
#     print("I will allways executed")



# nested try except block
# try:
#     a = int(input("Enter first number"))
#     b = int(input("Enter second number"))
#     try:
#         print(a/b)
#     except ZeroDivisionError as msg: 
#         print(msg)
# except ValueError as msg: 
#         print(msg)


# user defined exception by raise keyword

# bank_bal = 1000
# if bank_bal<1000:
#     raise Exception("your account balance is below a accessing limit")
# else:
#     print("Your amount has withdrawn")







