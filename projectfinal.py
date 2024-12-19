# Function certificate high school
# Import Function
import time
from datetime import date
import os
from Crypto.Cipher import AES
import base64

# Generate AES encryption key
def generate_aes_key():
    return os.urandom(16)

# AES encryption
def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')

# AES decryption
def aes_decrypt(encrypted_data, key):
    data = base64.b64decode(encrypted_data)
    nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted_data.decode()

# Save key for decryption
def save_encryption_key(key):
    return key.hex()


# Add Username & Password
USERNAME = None
PASSWORD = None

def Create_Account():
    global USERNAME, PASSWORD
    print("Create a new account:")
    print("*" * 50)
    USERNAME = input("Enter a new Username: ")
    PASSWORD = input("Enter a new Password: ")
    print("Account created successfully!\n")


def login():
    global USERNAME, PASSWORD
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
        # Map certificate
        certificate = ""
    # Map certificate
        certificate += "*" * 100 + "\n"
        certificate += "*                                                                                                  *\n"
        certificate += "*                                      High School Certificate                                     *\n"
        certificate += "*                                                                                                  *\n"
        certificate += "*" * 100 + "\n"
        certificate += f"* Name: {self.firstname} {self.lasttname}".ljust(58) + f"* ID: {self.ID}".ljust(41) + "*\n"
        certificate += f"* Birthdate: {self.birthdate}".ljust(58) + f"* Nationality: {self.birth}".ljust(41) + "*\n"
        certificate += f"*".ljust(58) + f"* Phone Number: {self.phonenum}".ljust(41) + "*\n"
        certificate += f"*".ljust(99) + "*\n"
        certificate += "*" * 100 + "\n"
        return certificate


# Function Scinese
class nerd:

    # Input grade student Scinese
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
        report = ""
        report += f"*{'':<19}Lowest Grade{'':<7}Highest Grade{'':<15}Mark{'':<13}Status{'':<7}*\n"
        report += f"*{'Math:':<23}100{'':<16}200{'':<24}{self.math:<17}{'Pass' if self.math >= 100 else 'Fail':<12}*\n"
        report += f"*{'Scinese:':<23}50{'':<17}100{'':<24}{self.scinese:<17}{'Pass' if self.scinese >= 50 else 'Fail':<12}*\n"
        report += f"*{'Psychology:':<23}50{'':<17}100{'':<24}{self.psychology:<17}{'Pass' if self.psychology >= 50 else 'Fail':<12}*\n"
        report += f"*{'Pyhsics:':<23}50{'':<17}100{'':<24}{self.pyhsics:<17}{'Pass' if self.pyhsics >= 50 else 'Fail':<12}*\n"
        report += f"*{'Tecnology:':<23}50{'':<17}100{'':<24}{self.tecnology:<17}{'Pass' if self.tecnology >= 50 else 'Fail':<12}*\n"
        report += f"*{'English:':<23}50{'':<17}100{'':<24}{self.english:<17}{'Pass' if self.english >= 50 else 'Fail':<12}*\n"
        report += f"*{'Relgion:':<23}50{'':<17}100{'':<24}{self.relgion:<17}{'Pass' if self.relgion >= 50 else 'Fail':<12}*\n"
        report += f"*{'Arabic:':<23}50{'':<17}100{'':<24}{self.arabic:<17}{'Pass' if self.arabic >= 50 else 'Fail':<12}*\n"
        report += f"{'*' * 100}\n"

        # Average Calculation
        Avg = float((self.math + self.scinese + self.psychology + self.pyhsics + self.arabic + self.tecnology + self.english + self.relgion) / 9)

        # Time and Date
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        d = date.today()

        # Footer
        report += f"*{'Average:':<11}{int(Avg * 100) / 100:<46}*{'Time:':<6}{current_time:<34}*\n"
        report += f"*{'Result:':<11}{'Pass' if Avg >= 50 else 'Fail':<46}*{'Date:':<6}{str(d):<34}*\n"
        report += f"{'*' * 100}\n"

        return report


# Function Arts
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
        report = ""
        report += f"*{'':<19}Lowest Grade{'':<7}Highest Grade{'':<15}Mark{'':<13}Status{'':<7}*\n"
        report += f"*{'Math:':<23}100{'':<16}200{'':<24}{self.math:<17}{'Pass' if self.math >= 50 else 'Fail':<12}*\n"
        report += f"*{'Relgion:':<23}50{'':<17}100{'':<24}{self.relgion:<17}{'Pass' if self.relgion >= 50 else 'Fail':<12}*\n"
        report += f"*{'English:':<23}50{'':<17}100{'':<24}{self.english:<17}{'Pass' if self.english >= 75 else 'Fail':<12}*\n"
        report += f"*{'Arabic:':<23}50{'':<17}100{'':<24}{self.arabic:<17}{'Pass' if self.arabic >= 75 else 'Fail':<12}*\n"
        report += f"*{'Geography:':<23}50{'':<17}100{'':<24}{self.geography:<17}{'Pass' if self.geography >= 50 else 'Fail':<12}*\n"
        report += f"*{'History:':<23}50{'':<17}100{'':<24}{self.history:<17}{'Pass' if self.history >= 50 else 'Fail':<12}*\n"
        report += f"*{'Tecnology:':<23}50{'':<17}100{'':<24}{self.tecnology:<17}{'Pass' if self.tecnology >= 50 else 'Fail':<12}*\n"
        report += f"*{'Scinetest Culture:':<23}50{'':<17}100{'':<24}{self.scinetest_culture:<17}{'Pass' if self.scinetest_culture >= 50 else 'Fail':<12}*\n"
        report += f"{'*' * 100}\n"

        # Average Calculation
        Avg = float((self.math + self.relgion + self.english + self.arabic + self.geography + self.history + self.tecnology + self.scinetest_culture) / 9)

        # Time and Date
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        d = date.today()

        # Footer
        report += f"*{'Average:':<11}{int(Avg * 100) / 100:<46}*{'Time:':<6}{current_time:<34}*\n"
        report += f"*{'Result:':<11}{'Pass' if Avg >= 50 else 'Fail':<46}*{'Date:':<6}{str(d):<34}*\n"
        report += f"{'*' * 100}\n"

        return report


########################################################################################################################################################################

# Create Username & Password
Create_Account()


def main():
    print("\nPlease choose your section:", "\n")
    print("1. certificate")
    
    section_choice = int(input("Please Enter the number: "))
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
            student_info = s.print_info()
            grades = n.print_Nerd()
            print("*" * 60)
            print("\nChoose encryption type:")
            print("1. AES")
            encryption_choice = int(input("Choose encryption type: "))
            # Encrypt based on choice
            if encryption_choice == 1:
            # AES encryption
                key = generate_aes_key()
                encrypted_data = aes_encrypt(f"{student_info}, {grades}", key)
                print(f"\nEncrypted Certificate (AES):\n{encrypted_data}")
                print(f"Encryption Key (Save this key to decrypt later): {save_encryption_key(key)}")

                # Ask for decryption key
                decryption_key_input = input("\nEnter the decryption key to view the unencrypted certificate: ")
                decryption_key = bytes.fromhex(decryption_key_input)
                try:
                # Decrypt the data
                    decrypted_data = aes_decrypt(encrypted_data, decryption_key)
                    print("\nDecrypted Certificate:")
                    print(decrypted_data)
                except Exception as e:
                    print(f"Error during decryption: {e}")
            else:
                print("Invalid choice. Please choose a valid encryption type.")
            
        elif section_choice2 == 2:
            s = student()
            print("*" * 60)
            z = NotNerd()
            print("*" * 60)
            s_info = s.print_info()
            g = z.print_NotNerd()
            print("*" * 60)
            print("\nChoose encryption type:")
            print("1. AES")
            encryption_choice = int(input("Choose encryption type: "))
            # Encrypt based on choice
            if encryption_choice == 1:
            # AES encryption
                key = generate_aes_key()
                encrypted_data = aes_encrypt(f"{s_info}, {g}", key)
                print(f"\nEncrypted Certificate (AES):\n{encrypted_data}")
                print(f"Encryption Key (Save this key to decrypt later): {save_encryption_key(key)}")

                # Ask for decryption key
                decryption_key_input = input("\nEnter the decryption key to view the unencrypted certificate: ")
                decryption_key = bytes.fromhex(decryption_key_input)
                try:
                # Decrypt the data
                    decrypted_data = aes_decrypt(encrypted_data, decryption_key)
                    print("\nDecrypted Certificate:")
                    print(decrypted_data)
                except Exception as e:
                    print(f"Error during decryption: {e}")
            else:
                print("Invalid choice. Please choose a valid encryption type.")
        else:
            print("Invalid choice! Please enter either 1 or 2.")
    else:
        print("\nPlease try again", "\n")


# Run the main function
run = main()
########################################################################################################################################################################

