# import time
# time.sleep(2)
# n=int(input("Enter the number of rows: ")) 
# for i in range(1,n+1): 
#     print("* "*n) 

# time.sleep(2)
# n=int(input("Enter the number of rows: ")) #n=5
# for i in range(1,n+1): #i=1  , n=6
#     for j in range(1,n+1): # j=1
#         print(i,end=" ")
#     print()

# time.sleep(2)
# n=int(input("Enter the number of rows: ")) #5
# for i in range(1,n+1): #i=1
#     for j in range(1,n+1): #j=2
#         print(chr(64+i),end=" ")
#     print()

# time.sleep(2)
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end=" ")
#     print()
    
# time.sleep(2)
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,1+i): 
#         print("*",end=" ")
#     print()

# time.sleep(2)

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print("*"*i)
# time.sleep(2)

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(i,end=" ")
#     print()

# time.sleep(2)
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(j,end=" ")
#     print()

# time.sleep(2)
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(chr(64+i),end=" ")
#     print()

# time.sleep(2)
# '''import time
# n=int(input("Enter the number of rows: "))
# for i in range(3,n+1):6
#     time.sleep(1)
#     for j in range(1,n+2-i): 4
#         time.sleep(1)
#         print("*",end=" ")
#     print()'''

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end=" ")
#     print()

# time.sleep(2)
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(n+1-i,end=" ")
#     print()
# time.sleep(2)

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(n+1-j,end=" ")
#     print()

# time.sleep(2)
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(65+n-i),end=" ")
#     print()

# time.sleep(2)

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),"*"*i,end=" ")
#     print() 

# '''import time
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):   #i=1
#     print(" "*(n-i),end=" ")
#     for j in range(1, i+1):#3
#         time.sleep(1)
#         print("*",end=" ")
#     print()'''

# ''' y-axis
#     |
#     |          ^                   "
#     |    1 2 3 4     (col=j)
#     1          *   
#    -2        *   *    
#     3         
#     4       
#     ====================x-axis (i,j)=(2,2)
# (row=i)
# i=2
# j=4'''        





# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1, i+1):
#         print(i,end=" ")
#     print()

# time.sleep(2)

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1, i+1):
#         print(j,end=" ")
#     print()

# time.sleep(2)

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1, i+1):
#         print(chr(64+i),end=" ")
#     print()
# time.sleep(2)

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1, i+1):
#         print(chr(64+j),end=" ")
#     print()

# time.sleep(2)

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(i-1),end=" ")
#     for j in range(1, n+2-i):
#         print(i,end="")
#     print()
# time.sleep(2)
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(i-1),end=" ")
#     for j in range(1, n+2-i):
#         print(j,end="")
#     print()

# time.sleep(2)

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(i-1),end=" ")
#     for j in range(1, n+2-i):
#         print(chr(64+i),end="")
#     print()

# time.sleep(2)

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(i-1),end=" ")
#     for j in range(1, n+2-i):
#         print(chr(64+j),end="")
#     print()

# time.sleep(2)
'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i):
        print(i-j,end=" ")
    for k in range(0,i):
        print(k,end=" ")
    print()'''

""" n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i):
        print(chr(i-j+65),end=" ")
    for k in range(0,i):
        print(chr(k+65),end=" ")
    print() """
""" n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print() """

'''for k in range(1,n+1):
    print(" "*k,end=" ")
    for l in range(1,n+1-k):
        print("*", end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(i ,end=" ")
    print()

for k in range(1,n+1):
    print(" "*k,end=" ")
    for l in range(1,n+1-k):
        print(k, end=" ")
    print()'''


'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(chr(64+i) ,end=" ")
    print()'''

'''for k in range(1,n+1):
    print(" "*k,end=" ")
    for l in range(1,n+1-k):
        print(chr(64+k), end=" ")
    print() ''' 

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for k in range(1,n+1):
    for l in range(1,n+2-k):
        print("*",end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
for k in range(1,n+1):
    for l in range(1,n+2-k):
        print(k,end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
for k in range(1,n+1):
    for l in range(1,n+2-k):
        print(chr(64+k),end=" ")
    print()'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(1,i):
        print("*",end=" ")
    print()

for k in range(1,n+1):
    print(" "*(n-k),end=" ")
    for l in range(1,k+1):
        print("*",end=" ")
    print()'''

'''import time
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    time.sleep(1)
    for j in range(i,n+2-i):
        print(j,end=" ")
    print()

for k in range(1,n+1):
    print(" "*(n-k),end=" ")
    time.sleep(1)
    for l in range(1,k+1):
        print(k,end=" ")
    print()'''


#nterms = int(input("How many terms? "))

# first two terms
'''n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1'''



    
