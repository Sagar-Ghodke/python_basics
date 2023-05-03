'''file handling in python'''
'''
note : file must be close while operating
'''
# r:= read mode
# w:= write mode
# a:= append :original+add

# close() ----> close file after handddling done

# with statement: no need t0 write close ()stateent


'''examples'''

# f = open("myfile.txt", "w")
# print("name of file", f.name) 
# print("file mode", f.mode)
# print(" readeble ",f.readable())
# print(" writeable ", f.writable())
# print(" file has closed", f.closed)
# f.close()
# print(" file has closed", f.closed)


# with open("myfile.txt", "w") as f:
#     f.write("amit\n")
#     f.write("ashish\n")
#     f.write("Prashant\n")
#     print("\n Data writing done.")
#     print("file closed: ", f.closed)
# print("file closed: ",f.closed)



# operation with CSV file

# import csv
# f = open("student.csv","a",newline="")
# a =csv.writer (f) # here it will return csvwriter object 
# # a.writerow(["studentID", "rollno", "name", "mobileno"])
# # studentid= 1
# # rollno=1001
# # name= "prashant"
# # mobileno =646464646
# studentid=int(input("Enter student id: "))
# rollno = int(input("Enter your roll number"))
# name = input("Enter your name")
# mobileno= int(input("Enter your mobile no"))
# a.writerow([studentid, rollno, name, mobileno])
# print("student record has saved ")





# WAP input column name:= Id, name, rollno, emaild, address, mobileno, p1, p2, p3,p4, p5, total, percentage,result
# Input = name, rollno, emaild, address, mobileno
# input = p1, p2, p3,p4, p5
# calculate: = total, Percentage
# condition:= if you will pass in all paper then result will be = pass else Fail 40


# import csv

# f = open("student2.csv","a",newline="")
# a =csv.writer (f)
# # a.writerow(["studentID","name","rollno","Email","Address", "mobileno","P1","p2","p3","p4","total","percentage","result"])
# studentid=1
# studentid+=1

# name = input("Enter your name")
# rollno = int(input("Enter your roll number"))
# email = (input("Enter your email"))
# address = (input("Enter your address "))
# mobileno= int(input("Enter your mobile no"))
# p1=int(input("p1:"))
# p2=int(input("p2:"))
# p3=int(input("p3:"))
# p4=int(input("p4:"))

# total=p1+p2+p3+p4
# percentage=total/4
# result=""
# if p1 and p2 and p3 and p4>40:
#     result="pass"
# else:
#     result="fail"
    
# a.writerow([studentid,name,rollno,email,address, mobileno,p1,p2,p3,p4,total,percentage,result])
# print("student record has saved ")





# WAP to send invitation to friends for xyz function



# try:
#     num=int(input("\nEnter number of members you wants to invite: "))
# except ValueError as message:   #accept only int value
#     print("Please enter a valid number: ") 
    
# msg=input("Enter the invitation msg: ")
# # msg="You are invited to the xyz function please do come."


# with open("members.txt", "w") as f:
#     print("\nPlease enter the name of the person you wants to invite: ")
    
#     for i in range(num):
#         f.write(f"{input('Name: ')}\n")
#     print("\nMembers added.\nSending Invitation...")
    
# with open("members.txt",) as f:
#     x=f.readlines()
#     new_x=list(x)
    
#     with open("invitation.txt", "w") as f:
#         f.write(f"INVITATION BOX:                                  Total Messages={num}\n\n\n")
        
#         for i in new_x:
#             f.write(f"Hi,{i+msg}\nThank you\n\n\n")
# print("\nInvitation has sent.")




    
# quiz by file handling



# try:
#     num=int(input("\nEnter number of ques: "))
# except ValueError as message:   #accept only int value
#     print("Please enter a valid number: ") 


# with open("questions.txt", "w") as f:
#     print("\nAdd questions for the test: ")
    
#     for i in range(num):
#         f.write(f"{input('Question: ')}\n")
#     print("\nQuestions added.\n")
    
# with open("answers.txt", "w") as f:
#     print("\nAdd answers of the test questions in sequence: ")
    
#     for i in range(num):
#         f.write(f"{input('Answer: ')}\n")
#     print("\nAnswers added.\n")

'''user can either add ques from the interface or into the text file which is much easier'''
    
with open("questions.txt") as f:
    questions=list(f.readlines())
    
with open("answers.txt") as f:
    answers=list(f.readlines())
    
def clean(x):  #remove \n from string
    return x.strip('\n')
questions=[clean(i) for i in questions]
answers=[clean(i) for i in answers]

x=dict(zip(questions, answers)) #mearge two lists
score=0 #for counting score of quiz

for i in x:
    print(f"\nQues: {i}")
    ans =(input("Your answer: "))
    if ans==x[i]:
        score+=1
        print("Correct answer!")
    else:
        score+=0
        print("hugg diya na bro!")
    
print("\nTest is over. Your score is:" ,score)  
