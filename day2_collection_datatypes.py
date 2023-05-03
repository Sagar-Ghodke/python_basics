# python collection datatypes? 4types
# 1.list:(when requirement is not fixed)
    # orderwise
    # heterogenous
    # represeted in []
    # duplicate data alloued
    # list by nature growable
    # mutable
    
# mylist = ["prashant", "Ashish", "Rahul", "ankit","komal", "ankush", "Ashish",77, "sagar", "vishnu", "poornima"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist [1])
# print(mylist [2])
# print(mylist[-1])
# print(mylist [2:5]) # n=5,n-1=4
# print(mylist[:5]) # n=5 n-1=4 ر
# print(mylist [1:]) # n=8, n-1-8-1-7
# print(mylist [1:8:2])#1,3,5,7'''



# mutation
# mylist[1]="ram"
# print(mylist)

# appending
# mylist.append("sita")
# mylist.append("laxman")
# print(mylist)


# mylist.insert(2,"ritu")
# print(mylist)


# mylist.remove("jyotsna")
# print(mylist)


# newlist=mylist.copy()
# print(newlist)

# multidimentional list dictionary

# mylist = [['prashant', 'jha'], ['85.56'], [440022,"yyy"]]
# print("example of multidimensional list: ")
# print(mylist)
# #print (mylist [row][col])
# print(mylist[0][0])
# print (mylist[0][1])
# print (mylist [1][0])
# print (mylist [2][0])
# print (mylist [2][1])

# list1= ['prashant', 'jha']
# print(list1*2)#print 2 times
# list2=[290,29]
# print(list1+list2) #adds 2 lists

# delete values of list or list as whole
# list=[213,'sagar',' jyotsna']
# del list[2]
# print(list)

# clear values in list
# list=[213,'sagar',' jyotsna']
# print(list)
# list.clear()
# print(list)


# add name in list
# name="sagar"
# print(name)
# mylist=list(name) 
# print(mylist) #['s', 'a', 'g', 'a', 'r']




# --------------------------------------------------------------------------------------------

# 2.tuple (when requirement is completely fixed)
    # orderwise
    # heterogenous
    # represeted in []
    # duplicate data alloued
    # list by nature growable
    # immutable-cannot change values
    
# mytuple=("prashant", "Ashish", "Rahul", "sandip", "komal", "ankush", "rajesh")
# print(mytuple)
# print(type(mytuple))
# mytuple[2]="sunil" 
# print (mytuple)


# print(mytuple [0])
# print(mytuple [1])
# print(mytuple [2])
# print(mytuple [-1])
# print(mytuple [2:5]) # n=5,n-1=4
# print(mytuple [:5]) # n=5 n-1=4 ر
# print(mytuple [1:]) # n=8, n-1-8-1-7
# print(mytuple [1:8:2])#1,3,5,7'''

# print(mytuple*2)#print 2 times


# -----------------------------------------------------------------------------------

# 3.Dictionary
# d={ 
#     "when india had independance? ": 1947,
#     "india won cricketcup in which year?":1983,
#     "5+5=?":10
# }
# score=0 #for counting score of quiz
# for i in d:
#     print(i)
#     ans = int(input("Your answer: "))
#     if ans==d[i]:
#         score+=1
#         print("Congratulations!")
#     else:
#         score+=0
#         print("haglas na bahava!")
    
# print("Your score is:" ,score)


    