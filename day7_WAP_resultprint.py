user="Sagar"
passw=123

choice =0 # global variable
print("\nFor Mech type 1\nFor cs: 2\nFor IT: 3\nFor ENTC: 4")
class Exam (object):
    def __init__(self):
        self.sname=None
        self.collegename=0
        self.classname = 0
        self.rollno =0
        self.login() # calling function
    def login(self): # constructor part (called function)
        
        username=input("Enter username") 
        password=input("Enter password")
        
        # login section
        if username is user and password is passw:
            print("Login successfully")
            self.getdata() # calling function
        else:
            print("Login fail try again")
            
# -------------------------------------------------------------------------------------
    print()
    # enter your profile details
    def getdata(self):
        self.sname =       input("Enter Your Name")
        self.collegename = input("Enter Your College Name")
        self.classname =   input("Enter Your Class Name")
        self.rollno =      input("Enter Your Roll Number")
        print()
        # --------------------------------------------------------end of profile data section
        # static subject declartion
        print(" choose any branch for giving exam")
        print("1. Mechanical Egineering")
        print("2. Information Technology")
        print("3. Computer Science")
        print("4. Civil Engineering")
        print()
        
        print("For mech: 1\nfor cs: 2\nfor IT: 3\n for ENTC: 4")
        choice = (print("\nFor mech type 1\nFor cs: 2\nFor IT: 3\nFor ENTC: 4")),int(input("Enter your Department: ")) # subject selection logic part
        if choice==1:
            self.mechanical() # calling function
        elif choice==2:
            pass
        elif choice==3:
            pass
        elif choice==4:
            pass
        else:
            print("you have entered wrong choice.")
            
        # called function part 
    def mechanical(self):
        print("1. First Semester") 
        print("2. Second Semester")
        print("Enter yourÏSemester Number")
        
        # logical part
        choice =int(input("Enter your choice: "))
        if choice == 1:
        #first_subj() # calling function
            print("Math")
        elif choice== 2: 
            pass #second_subj()
        
    def information(self):
        print("1. First Semester") 
        print("2. Second Semester")
        choice =int(input("Enter your choice"))
        if choice == 1:
            pass
        elif choice== 2:
            pass
        
    def computer (self):
        print("1. First Semester")
        print("2. Second Semester")
    choice =input("Enter your choice")
    if choice == 1:
        pass
    elif choice== 2:
        pass   
    
     
#object creation of class
obj = Exam()
obj.login()
# -----------------------------------------------------------------------------------end

# Examination Calculation part
class Calculation(object):
    def __init__(self):
        self.stat=0
        self.dmgt=0
        self.cg =0
        self.toc =0
        self.math=0
        self.total=0
        self.percentage=0
        self.ps = 0
        print()
        print("Do You Want To Put Examination Marks Enter Yes/No")
        print()
        Yes = input("Enter yes/no")
        if Yes == "yes":
            self.calculatemarks () # calling function
        else:
            print("Thank You For Visiting Here")
            print()
            
# taking a marks for subject
    def calculatemarks (self):
        self.stat = int(input("Enter Marks of Statistics:"))
        self.dmgt = int(input("Enter Marks of DMGT :"))
        self.cg = int(input("Enter Marks of CG :"))
        self.toc =int(input("Enter Marks Of TOC :"))
        self.math = int(input("Enter Marks Of Math1:"))
        print()
        
        if self.stat >=40 and self.dmgt>=40 and self.cg>=40 and self.toc>=40 and self.math>=40:
            self.ps="pass" 
            print("You are pass")
        else:
            self.ps="Fail" 
            print("You are fail")
            
        self.total = self.stat+self.dmgt+self.cg+self.toc+self.math
        self.percentage = self.total/5.0

obj1=Calculation()
# -------------------------------------------------------------------------------


# obj2=Assesment()
# obj2.result()

                            

                    
                        