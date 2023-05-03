
# transfer functions:
#     break 
#     continue 
#     pass


'''
print table 1to20
'''
# a=[1,2,3,4,5,6,7,8,9,10]
# x=1
# for i in a:
#     x=+1
#     print(i*1)



'''
print
1 5
2 4
4 2
5 1
'''
# for i,j,k in zip (range(1,6), range (5,0,-1), range (11,16)): 
#     if i==3 and j==3: 
#         continue
#     print(i," ",j," ",k)


'''
accept from user
n=int(input(""))
o/p=
A=user entered uppercase
b=lower
6=digit
@=special
'''

# input=input("enter a value: ")

# if input.isupper()==True:
#     print("upper")
# elif input.islower()==True:
#     print("lower")
# elif input.isdigit()==True:
#     print("digit")
# else:
#     print("special")


'''using ASCII value'''

# ch =ord(input("Enter any charecter")) # ord function used to convert in ASCII code
# if ch>=65 and ch<=91:
#     print("your entered charecter is in upper case") 
# elif ch>=97 and ch<=122:
#     print("your entered charecter is in lower case")
# elif ch>=48 and ch<=57:
#     print("your entered charecter is digit") 
# else:
#     print("your entered charecter is in special symbols")
    
    
'''
note: cant use break and continue conditional statements without loops
'''
#using else block 
# mycart=[10,20,68,60,70] 
# for item in mycart:
#     if item>400:
#         print("This is not in my budget")
#         continue 
#     print(item)
# else:
#         print("you have purchased everything")




# count =0
# for i in range(9): #i=3
#     if i%2 == 0: #0==
#         print(i)
#     else:
#         print(i)
#         count +=1
# print("count", count)



# name = "cyber"
# #01234567
# i =0
# for x in name : #x
#     if x == 'n': 
#         print("The character present at index no ",i," value=:",i)
#         break
# i=i+1 # update by one i





# count =0 #count =
# odd =0 #odd =
# for i in range(1,20,2): #i=
#     if i%2==0: #
#         count=count+1
#     else:
#         odd = odd+1
# print("count", count) 
# print("odd number =", odd)




# for ch in 'cyberenvy': # ch=0,1 print(ch)
#     if ch=='h' or ch == 'j':
#         break
#         print('Current Letter :', ch)





# # A user will have to enter name until 

# name=""
# while name!="sagar":
#     name=input("Enter your Name:")
# print("Thanks for entering valid name")



'''user login'''

# username="Sagar"
# password="123"

# while username=="Sagar"and password=="123":
#     user=(input("Enter Name:"))
#     passs=(input("Enter password"))
#     if user == username and passs==password:
#         print("login successful")
#         break
#     else:
#         print("wrong credentials")




# WAP for change calculation with respect to Total amount

Amount = int(input("Please Enter Amount for Withdraw :"))

print(" 2000 notes= ", Amount //2000) 
print(" 500 notes= ", (Amount % 2000)//500)
print(" 200 notes= ", ((Amount % 2000) %500 ) // 200)
print(" 100 notes= ",(((Amount % 2000) % 500) %200 )//100)
print(" 50 notes= ", ((((Amount % 2000) % 500) %200 ) %100) //50)
print(" 20 notes= ", (((((Amount % 2000) % 500) %200 ) %100) %50)//20)
print(" 10 notes= ", ((((((Amount % 2000) % 500) %200 ) %100) %50) %20)//10)
print(" 5 notes= ", (((((((Amount % 2000) % 500) %200 ) %100) %50) %2) %10//5))