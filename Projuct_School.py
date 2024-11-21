# Function certificate high school
# Import Function
import time
import calendar
from datetime import date

# Create Calendar
def Calendar():
    yy = 2024   # Year
    mm = 12     # Month
    # Disable the Calendar
    print(calendar.month(yy, mm))

# Add Username & Password
USERNAME = None
PASSWORD = None

def Create_Account():
    global USERNAME , PASSWORD
    print("Create a new account:")
    print("*" * 50)
    USERNAME = input("Enter a new Username: ")
    PASSWORD = input("Enter a new Password: ")
    print("Account created successfully!\n")
def login():
    global USERNAME , PASSWORD
    if USERNAME is None or PASSWORD is None:
        print("No account found. Please create an account first.\n")
        return False
    print("Log in to your account:")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == USERNAME and password == PASSWORD:
        print("Login successful! Access granted.\n")
        return True
    else:
        print("Invalid username or password. Access denied.\n")
        exit()

    
# Input information Student
class student:
    def __init__(self):
        self.firstname = str(input("Please Enter Your First Name: "))
        self.lasttname = str(input("Please Enter Your Last Name: "))
        self.birthdate = input("Please Enter Your Birthdate ... e.g DD/MM/YYYY: ")
        self.ID = int(input("Please Enter Your ID: "))
        self.birth = str(input("Please Enter Your Place of birth: "))
        self.phonenum = int(input("Please Enter Your Phone Number: "))
        

# Print info student
    def print_info(self):
        #Map certificate
        print("*" * 100)
        print("*                                                                                                  *")
        print("*                                      High School Certificate                                     *")
        print("*                                                                                                  *")
        print("*" * 100)
        print(f"* Name: {self.firstname} {self.lasttname}".ljust(58),f"* ID: {self.ID}".ljust(39),"*") 
        print(f"* Birthdate: {self.birthdate}".ljust(58),f"* nationality: {self.birth}".ljust(39),"*")
        print(f"*".ljust(58),f"* Phone Number: {self.phonenum}".ljust(39),"*")
        print(f"*".ljust(98),"*")

# Function Scinese
class nerd:

    # Input grade student nerd
    def __init__(self):

        self.math = int(input("Please Enter Your Math Grade: "))
        self.scinese = int(input("Please Enter Your Scinese Grade: "))
        self.psychology = int(input("Please Enter Your psychology Grade: "))
        self.pyhsics = int(input("Please Enter Your Pyhsics Grade: "))
        self.arabic = int(input("Please Enter Your Arabic Grade: "))
        self.tecnology = int(input("Please Enter Your Tecnology Grade: "))
        self.english = int(input("Please Enter Your English Grade: "))
        self.relgion = int(input("Please Enter Your Relgion Grade: "))

    # Print grade student nerd
    def print_Nerd(self):
        print(f"*" * 100)
        print(f"*".ljust(20),"Lowest Grade","".ljust(7),"Highest Grade".ljust(23),"Mark".ljust(15),"Status".ljust(16),"*")
        print(f"*","Math: ".ljust(23),"100","".ljust(16),"200".ljust(19),f"{self.math}".ljust(15),"Pass" if self.math >= 100 else "Fail","".ljust(10),"*")
        print(f"*","Scinese: ".ljust(23),"50","".ljust(17),"100".ljust(19),f"{self.scinese}".ljust(15),"Pass" if self.scinese >= 50 else "Fail","".ljust(10),"*")
        print(f"*","Psychology: ".ljust(23),"50","".ljust(17),"100".ljust(19),f"{self.psychology}".ljust(15),"Pass" if self.psychology >= 50 else "Fail","".ljust(10),"*")
        print(f"*","Pyhsics: ".ljust(23),"50","".ljust(17),"100".ljust(19),f"{self.pyhsics}".ljust(15),"Pass" if self.pyhsics >= 50 else "Fail","".ljust(10),"*")
        print(f"*","Tecnology: ".ljust(23),"50","".ljust(17),"100".ljust(19),f"{self.tecnology}".ljust(15),"Pass" if self.tecnology >= 50 else "Fail","".ljust(10),"*")
        print(f"*","English: ".ljust(23),"50","".ljust(17),"100".ljust(19),f"{self.english}".ljust(15),"Pass" if self.english >= 50 else "Fail","".ljust(10),"*")
        print(f"*","Relgion: ".ljust(23),"50","".ljust(17),"100".ljust(19),f"{self.relgion}".ljust(15),"Pass" if self.relgion >= 50 else "Fail","".ljust(10),"*")
        print(f"*","Arabic: ".ljust(23),"50","".ljust(17),"100".ljust(19),f"{self.arabic}".ljust(15),"Pass" if self.arabic >= 50 else "Fail","".ljust(10),"*")
        print(f"*" * 100)
        Avg = float((self.math + self.scinese + self.psychology + self.pyhsics + self.arabic + self.tecnology + self.english + self.relgion)/9)

        # Time
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S",t)

        # Date
        d = date.today()
        print(f"*","Average: ", f"{int(Avg * 100)/100}".ljust(46),f"* Time:",current_time,"".ljust(22),"*")
        print(f"* Result: ",f"Pass" if Avg >= 50 else "Fail","".ljust(42),f"* Date:",d,"".ljust(20),"*")
        print(f"*" * 100)
        Calendar()


#Function Arts
class NotNerd:
    # Input grade student Arts
    def __init__(self):
        self.math = int(input("Please Enter Your Math Grade: "))
        self.relgion = int(input("Please Enter Your Relgion Grade: "))
        self.english = int(input("Please Enter Your English Grade: "))
        self.arabic = int(input("Please Enter Your Arabic Grade: "))
        self.geography = int(input("Please Enter Your Geography Grade: "))
        self.history = int(input("Please Enter Your History Grade: "))
        self.tecnology = int(input("Please Enter Your Tecnology Grade: "))
        self.scinetest_culture = int(input("Please Enter Your Scinetest Culture Grade: "))

        # Print grade student Arts
    def print_NotNerd(self):
        print("*" * 100)
        print(f"*".ljust(20),"Lowest Grade","".ljust(7),"Highest Grade".ljust(23),"Mark".ljust(15),"Status".ljust(16),"*")
        print(f"*","Math: ".ljust(23),"50","".ljust(17),"100".ljust(19),f"{self.math}".ljust(15),"Pass" if self.math >= 50 else "Fail","".ljust(10),"*")
        print(f"*","Relgion: ".ljust(23),"50","".ljust(17),"100".ljust(19),f"{self.relgion}".ljust(15),"Pass" if self.relgion >= 50 else "Fail","".ljust(10),"*")
        print(f"*","English: ".ljust(23),"75","".ljust(17),"150".ljust(19),f"{self.english}".ljust(15),"Pass" if self.english >= 75 else "Fail","".ljust(10),"*")
        print(f"*","Arabic: ".ljust(23),"75","".ljust(17),"150".ljust(19),f"{self.arabic}".ljust(15),"Pass" if self.arabic >= 75 else "Fail","".ljust(10),"*")
        print(f"*","Geography: ".ljust(23),"50","".ljust(17),"100".ljust(19),f"{self.geography}".ljust(15),"Pass" if self.geography >= 50 else "Fail","".ljust(10),"*")
        print(f"*","History: ".ljust(23),"50","".ljust(17),"100".ljust(19),f"{self.history}".ljust(15),"Pass" if self.history >= 50 else "Fail","".ljust(10),"*")
        print(f"*","Tecnology: ".ljust(23),"50","".ljust(17),"100".ljust(19),f"{self.tecnology}".ljust(15),"Pass" if self.tecnology >= 50 else "Fail","".ljust(10),"*")
        print(f"*","Scinetest Culture: ".ljust(23),"50","".ljust(17),"100".ljust(19),f"{self.scinetest_culture}".ljust(15),"Pass" if self.scinetest_culture >= 50 else "Fail","".ljust(10),"*")
        print(f"*" * 100)
        Avg = float((self.math + self.relgion + self.english + self.arabic + self.geography + self.history + self.tecnology + self.scinetest_culture)/9)

        # Time
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S",t)

        # Date
        d = date.today()

        print(f"*","Average: ",f"{int(Avg * 100)/100}".ljust(46),f"* Time:",current_time,"".ljust(22),"*")
        print(f"* Result: ",f"Pass" if Avg >= 50 else "Fail","".ljust(42),f"* Date:",d,"".ljust(20),"*")
        print(f"*" * 100)
        Calendar()

########################################################################################################################################################################
# School cafeteria
class cul:
    def __init__(self):
        self.Net_amount = int(input("\nPlease Enter value:"))
        print("\n")
        print("*" * 80)
        self.Value_Added_Tax = 0.16
        self.day = 20
    def print_info(self):
        vat_amount = self.Net_amount * self.Value_Added_Tax
        total_final = (vat_amount + self.Net_amount)

         # Time
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S",t)

        # Date
        d = date.today()

# Print Account School Cafeteria
        print(f"* User: AbdAlkarim Nairoukh".ljust(50), f"{current_time}".ljust(27), "*")
        print("*".ljust(50), f"{d}".ljust(27), "*")
        print("*" * 80)
        print(f"* Net amount".ljust(30), "Value Added Tax".ljust(30), "Amount","".ljust(9),"*")
        print(f"*   {self.Net_amount}".ljust(36), "16%".ljust(24), f"{total_final:.2f}".ljust(16),"*")
        print("*" * 80)

        if total_final >= 150:
            daily_pyment = total_final / self.day
            print(f"* Daily payment: {daily_pyment:.2f} per day for 20 days.".ljust(78), "*")
            print("*" * 80)
        else:
            print("\n")
        Calendar()
# Choose number 1 or 2 for certificate High School & School cafeteria
Create_Account()
def main():
    print("\nPlease choose your section:","\n")
    print("1. certificate")
    print("2. School cafeteria","\n", "*" * 30)
    section_choice = int(input("Please Enter number 1 or 2: "))
    print("*" * 50)

# Choose number 1 for certificate High School
    if section_choice == 1:
        login()
        print("\nPlease choose your section:", "\n")
        print("1. Scientific")
        print("2. Arts", "\n", "*" * 30)
        section_choice2 = int(input("Please Enter number 1 or 2: "))
        print("*" * 50)
        if section_choice2 == 1:
            s = student()
            print("*" * 60)
            n = nerd()
            print("*" * 60)
            s.print_info()
            n.print_Nerd()
        elif section_choice2 == 2:
            s = student()
            print("*" * 60)
            z = NotNerd()
            print("*" * 60)
            s.print_info()
            z.print_NotNerd()
        else:
            print("Invalid choice! Please enter either 1 or 2.")

# Choose number 2 for School cafeteria
    elif section_choice == 2:
        login()
        x = cul()
        x.print_info()
    else:
        print("\nPlease try again","\n")


# Run the main function
run = main()
########################################################################################################################################################################

