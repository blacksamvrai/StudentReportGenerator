# imported modules
import os
# global variables
name =""
mname = "  "
sname = ""
fullAddress = ""
IDnum = 0
IDnumHidden = 0
balance = 0
coursesHelp = {}
coursesCode = {}
RESULTSCSC = {"MAT101: Mathematics": ["A- | 88%", 30], "SCI121: SCIENCE": ["B  | 73%", 15], "CSC111: COMPUTER SCIENCE": ["B+ | 78%", 30],
            "BUS112: BUSINESS STUDIES": ["B- | 70%", 15]}
RESULTSCSCavg = {"MAT101":88, "SCI121":73, "CSC111":78,"BUS112":70}
FEESCSC = {"MATH": 1000, "SCIENCE": 1300, "COMPUTER PROGRAMMING": 2840, "BUSINESS SCIENCE": 2000}
FEESCSCt = {"MAT101": ["MATH", 1000], "SCI121": ["SCIENCE", 1300], "CSC111": ["COMPUTER SCIENCE", 2840],
            "BUS112": ["BUSINESS STUDIES", 2000]}

# clear screen method
def clear_screen():
    # print("\n" * 60)
    os.system('cls')


# Seperators
def seperatorTn():
    print('{0:^113}'.format("-"*35))

def seperatorBld():
    print('{0:^113}'.format("_"*35))

def fillInBlw():
    print('{0:^113}'.format("Please fill in the FORM below"))
    seperatorTn()
    # print("\n")

# form completed statement

def formCompltd():
    # print("\n")
    seperatorTn()
    print('{0:^113}'.format("Input Stored"))
    seperatorTn()

# id hidder function
def IDnumberHidder():
    global IDnum
    global IDnumHidden
    IDnum = input("Please enter your ID number: ")
    # id[:9].rjust(len(IDnum),"*")
    # print(IDnum)
    IDnumHidden =  IDnum[:9] + "*" * (len(IDnum) - 9)
    print("You have indicated that you ID Number is: ", IDnumHidden)


def welcomeRep():
    print("""
        ================================================================================================     
                                        WELCOME TO STUDENT ACADEMIC SYSTEM
                                               by Timothy Pietersen
        ================================================================================================                          """)
# learner form header
def learnerFormHeader():
    print("""        ________________________________________________________________________________________________     

                                            LEARNER INFORMATION FORM
        ________________________________________________________________________________________________                           
    """)
# learner form input
def learnerInput():
    global name
    global mname
    global sname
    clear_screen()
    welcomeRep()
    learnerFormHeader()
    fillInBlw()
    name = input("Please enter your Name: ")
    middleYesNo = input("Do you have any Middle Names[type: 'YES' / 'NO']: ").upper()
    if middleYesNo == 'YES':
        mname = input("Please enter your Middle Name(s): ")
    elif middleYesNo == 'NO':
        print("You have indicated that you have no Middle Name(s)")
        mname=''
    else:
        print("No Valid Selection made - Middle Name set to empty")
    sname = input("Please enter your Surname: ")
    IDnumberHidder()
    clear_screen()
    formCompltd()

# residential form header
def resFormHeader():
    print("""
        ________________________________________________________________________________________________     

                                            RESIDENTIAL INFORMATION FORM
        ________________________________________________________________________________________________                           
    """)

# student residential information form
def studentResInfo():
    global fullAddress
    resFormHeader()
    address = []
    print("Please Enter Full Address Below, Press 'Enter' on last line to Submit Address",end="\n")
    while True:
        addressLineAdd = input()
        if addressLineAdd:
            address.append(addressLineAdd) #could have used enumerate here
        else:
            break
    fullAddress = '\n'.join(address)
    clear_screen()
    formCompltd()

# Course Selector Header
def crSelForm():
    print("""
        ________________________________________________________________________________________________     

                                                Course Selection Form
        ________________________________________________________________________________________________                           
    """)
def idValidation(a):
    global IDnum
    if a == IDnum:
        return True
    else:
        return False
# course Selector Method
def courseSelector():
    global coursesHelp
    global coursesCode
    global IDnumHidden
    global coursesHelp
    global coursesCode
    crSelForm()
    # print('{0:^113}'.format("This is a short help screen for COURSE SELECTION FORM"))
    print('{0:^90}'.format("Please note that the system will print out all available courses"))
    coursesHelp = {"BSCCS": "Bsc Computer Science", "BCOMGEN": "Bcom General", "BAPSY": "BA Psychology"}
    coursesCode = ["BSCCS", "BCOMGEN", "BAPSY"]
    print(coursesHelp)
    print("Our System has picked up your ID number as: ",IDnumHidden)
    idNumCourseIdentify = input("Please confirm your Identity Number to retrieve registered Course:  ")
    while not idValidation(idNumCourseIdentify):
        clear_screen()
        idNumCourseIdentify = input("Please confirm your Identity Number to retrieve registered Course:  ")
    clear_screen()
    studentAccount()

# student account header
def studentStatmentForm():
    print("""
        ________________________________________________________________________________________________     

                                                Student Account Statement
        ________________________________________________________________________________________________                           
    """)
def studentAccount():
    global coursesHelp
    global coursesCode
    studentStatmentForm()
    global balance
    global FEESCSC
    global FEESCSCt
    # find a way to link your college courses to the modules fees
    balance = sum(FEESCSC.values())

    print("Our System has indicated that you are registered for: ",coursesHelp.get(coursesCode[0]))
    print("\n",'{0:^113}'.format("!!Your Account Statement is as follows!!").upper(),"\n")
    displayAccount()

def depositValidation(a):
    if int(a) >= 1:
        return True
    else:
        return False

def deposit():
    global balance
    amount = int(input("Enter amount to be Deposited: "))
    balance = balance - amount
    while not depositValidation(amount):
        clear_screen()
        amount = int(input("-" * 50, "\n""Amount Deposited:", 'R{:.2f}'.format(0), "Enter amount to be Deposited: "))
    clear_screen()
    print("-" * 50, "\n""Amount Deposited:", 'R{:.2f}'.format(amount))
    if balance > 0:
       displayAccount()
    else:
        print("\n")
        print("-" * 50, "\n""Current Balance:", 'R{:.2f}'.format(balance))
        print("\n"*2)
        print("Student account for ID number:",IDnumHidden,"has been Settled.")
        print("\n","_"*50)
        idNumReportConf = input("Please confirm your Identity Number to retrieve your Final Report:  ")
        while not idValidation(idNumReportConf):
            clear_screen()
            idNumReportConf = input("Please confirm your Identity Number to retrieve your Final Report:  ")
        clear_screen()
        # print("Our System has indicated that you are registered for: ",coursesHelp.get(coursesCode[0]))

    reportPrintOut()
# remove course module function
def removeModule():
    global balance
    global FEESCSC

def displayAccount():
    global balance
    print("-" * 40, "\n", '{:<8} {:<20} {:<10}'.format('Module', 'Details', 'Amount'),"\n","-" * 40,"\n",sep="")
    for m, v in FEESCSCt.items():
        det, amt = v
        print('{:<8} {:<20} R{:<10}'.format(m, det, amt))
    print("\n""Current Balance on Student Account is: ", 'R{:.2f}'.format(balance), "\n", "-" * 43, sep="")
    deposit()

def reportHeader():
    print("""
        ________________________________________________________________________________________________     

                                                        Report
        ________________________________________________________________________________________________                           
    """)

def reportPrintOut():
    reportHeader()
    global name
    global mname
    global sname
    global fullAddress
    global IDnumHidden
    global RESULTSCSCavg
    print("\n")
    print("Student: ",name+mname,sname,"\n")
    print("Address: ",fullAddress,"\n")
    print("I.D Number: ",IDnumHidden,"\n")
    print("-" * 85, "\n", '{:<16} {:>20} {:>43}'.format('Module', 'Result', 'Credits'), "\n", sep="")

    for m, v in RESULTSCSC.items():
        det, amt = v
        print('{:<30} {:<45} {:<-20}'.format(m, det, amt))

    avgModules = sum(RESULTSCSCavg.values())/4
    print("\n")
    print("Your inclusive grade score Average for all modules is: ",'{:0}%'.format(avgModules))
    print("\n","We are glad to present",name+mname,sname,"with his Results for the year of 2019","\n","You have achieve the above Results and would like to Congratulate you on the hard work during this year","\n","- School Registrar")


def report_printer():
    learnerInput()
    studentResInfo()
    courseSelector()
    # studentAccount()

report_printer()
