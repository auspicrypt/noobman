from base64 import urlsafe_b64encode
from hashlib import md5
from time import sleep
from getpass import getpass
from os import system
from cryptography.fernet import Fernet
print("Welcome to Encryption/Decryption Service! This service uses a uses"
      " a user-defined passphrase. Please Enter a strong passphrase that"
      " is easy for you to remember and don't forget, go strong!!\n\n")

def passwordentry():
    passwordentry.mypassword = input("Passphrase:\t")
    print("\n")
    mypassword2 = input("Confirm Passphrase:\t")
    print("\n")
    if passwordentry.mypassword == mypassword2:
        print("Bravo! same passphrases!\n")
        del(mypassword2)
        system('cls')
        mainworking()
    else:
        print("Please Enter Same passphrase each time\n")
        passwordentry()

def secretmess():
    a = input("Enter Your Secret here:\n\n")
    secretmess.b = bytes(a, encoding = 'utf-8')

def mainworking():
    key2 = md5(bytes(passwordentry.mypassword, encoding = 'utf-8')).hexdigest()
    keytucker = bytes(key2, encoding = 'utf-8')
    key3 = urlsafe_b64encode(keytucker)                # look for this function
    mainworking.final_key = Fernet(key3)
    secretmess()
    mainworking.encrypted = mainworking.final_key.encrypt(secretmess.b)
    print("\nYour Secret is in safe hands now! Chillax!\n")
    # print(mainworking.encrypted)   # to print the encrypted message

def revealnow():
    system('cls')
    print("Enter your password here to see your encrypted message: \n")
    passw = getpass("Password:\n")
    passwx = str(passw)
    if passw == passwordentry.mypassword:
        decrypted = mainworking.final_key.decrypt(mainworking.encrypted)
        print("Your Secret Message:\n")
        print(str(decrypted, encoding = 'utf-8'))
        sleep(5)
    else:
        print("Wrong Password!")
        x = input("Do you wish to try again ?")
        if x in ('yes', 'y', 'Y', 'YES'):
            revealnow()
        else:
            print("Byee!! See you later!")
            print("Don't worry your secret is still safe!! ;)\n")
            sleep(3)
passwordentry()
reply = input(" Do you wish to see your encrypted message ??\n\n")
if reply in ('yes', 'Yes', 'Y', 'y', 'YES'):
    revealnow()
else:
    print("Byee!! See you later!")
    print("Don't worry your secret is still safe!! ;)\n")
    sleep(3)
