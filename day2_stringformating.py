# String slicing

# name = "cyberenvy" #this is our sting
# print(name[0]) #p
# print(name[1]) #r
# print(name[-1])#T
# print(name[10])
# print(name[0:12:2]) # end-1, 12-1-11
# print(name[1:])
# print(name[:5])# 5-1=4
# print(name[:])
# print(name [1:4])


# time slicing

# import time
# print("Todays date is: ",time.ctime()[4:11],time.ctime()[20:40])



# name="sagar"
# age=21

# print("Hi, i am", name,"and my age is", age,"years old")
# print("Hi, i am " +name+ " and my age is " +str(age)+ " years old")
# print("i am %s and %i years old" %((name),(age)))
# print("i am {} and {} years old".format(name,age))
# print(f"i am {name} and {age} years old")



# string reversed
# data= "my name is sagar"[::-1]
# print(data)

# data="sagar"
# charlist=list(data)
# reversed=charlist.reverse()

# print(charlist)
# print(*charlist)
# print(*charlist,sep="")



# --------------------------------------------------------------------------------------
# word="python"
# print(word[::2])
#[::1]- as it is, [::2] skip by 1 value positive, [::3]-skip by 2, 3, 4 so on,
# [::-1] full reversed, [::-2] skip by 1 negative

# take string from user and check for palindrome 


# def isPalindrome(s1):
#     return s1 == s1[::-1]
# s1 = "marathi"

# ans1 = isPalindrome(s1)
 
# if (ans1):
#     print("Yes")
# else:
#     print("No")


# x=["apple", "banana", "cat", "dog"]
# print("the list contains: ",*x[:-1],"and",x[-1],sep=",")
# #print(f"the list contains: {x[:-1]} and {x[-1]}",sep=",") #sir's metho

# new_x=[]

# for i in range(0, len(x)-1):
#     new_x.append(x[i])
# print(*new_x, sep=",",end=" ")
# print("and", x[-1])
