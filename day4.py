
# import os
# PATH = "/home/cyberenvy/"

'''
# for listing all folder"


# print(os.listdir(PATH))
content=(os.listdir(PATH))
sizes=[]
# is the giver path a folder? check
# print(os.path.isdir(PATH))
# x=os.path.getsize(PATH+file)
for file in content:
    x=os.path.getsize(PATH+file)
    print(file, x)

# for file in content:
#     if file.endswith(".png"):
#         print(file)
#'''



'''list files in folder in size'''

# content=(os.listdir(PATH))
# sizes=[]
# for file in content:
#     size = os.path.getsize(PATH+file)
#     sizes.append(size)
#     for i in content:
#         if i==4096:
#             PATH
# final=list(zip(content, sizes))
# print(final.sort(key =lambda x: x[1]),end=" ")
# print(final)



# python file exception


# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except:
#         print("Oops! That was no valid number.")
        
        
        
        
# username="Sagar"
# password=123

# while username=="Sagar"and password==123:
#     user=(input("Enter Name:"))
#     try:
#         passs = int(input("Please Enter password: "))
#         break
#     except:
#         print("Oops! invalid Password")
#     # passs=(input("Enter password"))
#     if user == username and passs==password:
#         print("login successful")
#         break
#     else:
#         print("wrong credentials")

# def clean(x):
#     return x.strip(' @!%$#').capitalize()
# fruits=[" MANGO ","CHERRY", "@#Bananas@!", "grapes"]
# fruits=[clean(i) for i in fruits]
# print(fruits)



'''sort by vowels at end of word'''
# x=["rises","sun",'tomato',"python"]
# o/p=["rssie","snu",...]

# def shuffle(x): 
#     vow=""
#     cons =""
#     for c in x:
#         if c in "aeiouAEIOU":
#             vow +=c
#         else:
#             cons +=c
#     return cons+vow
# # print(list(map(shuffle,x)))


'''note:append left not for list
'''

# from collections import deque
# x=deque(["rises","sun",'tomato',"python"])
# for i in x:
#     for j in i:
#         y=x.pop(0)
#         x.appendleft(y)       #"a","e","i","o","u"
#         print(x)


# x = deque(["rises"])
# for i in x:
#     # x.popleft()
#     # x.popleft()
#     # print(x)
# # deque([3, 4])

#     x.appendleft("a")
# # x.appendleft(1)
#     print(x)
# # # deque([1, 2, 3, 4])
