# movies= ["Pathaan", "Pushpa", "KGF", "RRR", "Drishyam"]
# stars=["SRK", "Allu Arjun", "Yash", "NTR", "Mohan Lal"]

# print(dict(zip(movies, stars)))

# for i, j in zip(movies, stars):
    # print (f"{i} and {j}")
    # for i in range(len(movies)):
        # print(movies[i], stars[i])
        
        
# Quiz by combining 2 lists

# x=dict(zip(movies, stars))
# score=0 #for counting score of quiz
# for i in x:
#     print(i)
#     ans = str(input("Your answer: "))
#     if ans==x[i]:
#         score+=1
#         print("Congratulations!")
#     else:
#         score+=0
#         print("haglas na bahava!")
    
# print("Your score is:" ,score)


'''text="India" #count frequency of chars
output=""
i occurs 2 time
n 1 time
d 1 time
'''
# text="India"
# num = {}
 
# for i in text:
#     if i in num:
#         num[i] += 1
#     else:
#         num[i] = 1
# print("Count of all characters in TEXT is :",str(num))




# Square of values in list

# a=[1,2,3,4,5,6]

# for i in a:print(i**2)
# # [i*i for i in a]



# fruits=[" MANGO ","CHERRY", "@#Bananas@!", "grapes"]

# write answer:

# def clean(x):
#     return x.strip(' @!%$#').capitalize()
# fruits=[" MANGO ","CHERRY", "@#Bananas@!", "grapes"]
# fruits=[clean(i) for i in fruits]
# print(fruits)


'''Write a program that walks through a folder tree and searches for
files with a certain file extension (such as .pdf or .jpg). Copy these
Files from whatever location they are in to a new folder.'''



# import os
# PATH = "/home/cyberenvy/Pictures/Wallpapers"
# # for listing all folder"
# # print(os.listdir(PATH))
# content=(os.listdir(PATH))

# # is the giver path a folder? check
# # os.path.isdir()

# for file in content:
#     if file.endswith(".png"):
#         print(file)