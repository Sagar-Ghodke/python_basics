# Regular expression in python----------> RegEx
# python re module provide support to regular expression
# Applications: 
#   to develop:
        # digital circuits
        # compilers and interpreter
        # tcp/ip protocols
        #validation logic
        # pattern matching & searching application like ctrl-f
        
# convert to bytecode for fast excutions


# match function
# full match function


# import re 
# count=0
# pattern= re.compile("python")
# matcher=pattern.finditer("A function in python is defined by a def statement. python The general syntax looks like this: def function- name (Parameter list): statements, i.e. the function body. The parameter python list consists of none or more parameters. Parameters are called arguments, if the function is called python.")

# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
    
# print("the number of  occurance :",count)




# import re
# count=0
# matcher=re.finditer("Hi","HiaHiHiaaaaaHi")
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("the no of occurances: ",count)


# import re
# obj=input("enter any character: ")
# objmatch=re.finditer(obj,"a7b @k9z")
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())
    
    
    
import re
a=input("enter string to perform match operation")
mtch=re.match(a,'pythonisveryimportant')
print(mtch)
if mtch!=None:
    print("match found at begining level")
    print(mtch.start(), "", mtch.end())
else:
    print("there is nko matching at begining level")


# import re
# a = input("enter string to perform match operation: ")
# mtch = re.fullmatch(a,"pythonisvery")
# print(mtch)
# if mtch!=None:
#     print("match found at begining level")
#     print(mtch.start()," ", mtch.end())
# else:
#     print("there is no matching at begining level")
        

'''Search()
findall()
sub()function'''

import re 
# a=input("enter a string to perform a operation : ")
# mtch=re.rearch(a,"pythonisssdynamiclanggg")
# print(mtch)
# if mtch!=None:
#         print(mtch.start(),"",mtch.end())
# else:
#         print("ther is np matching string:")

'''findall() function'''
# mtch=re.findall('[a-z0-9A-Z]',"abch3hdh5bk6")
# print(mtch)


'''sub()function'''
# obj=re.sub('0-9','*',"ab3gd6nky17")
# print(obj)



'''subn() function'''
# obj=re.subn('[0-9]','@','ab3gd6nk17')
# print(obj)
# print("the string is: ",obj[0])
# print("the number if replacement is : ", obj[1])


# WAP to validate a mobile number
# import re
# mo_no=input("enter a mobile number: ")
# obj=re.fullmatch("[0-9]\d{9}",mo_no)
# if obj!=None:
#         print("valid mobile number")
# else:
#         print("invalid mobile number")