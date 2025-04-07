import time as t # Fo use method sleep()
import os # To clean console
from workWithUsersDB import checkUserCredentials

def clearConsole():
    os.system('cls')

def enterLoginAndPassword():
    login = input('Input your login: ')
    password = input('Input your password: ')
    if accountVerification(login, password):
        print(f"Successful authorization! Welcome, {login}!"), t.sleep(4)
    else:
        print("Incorrect login or password! Try again!"), t.sleep(5), enterLoginAndPassword()

def accountVerification(login, password):
    return checkUserCredentials(login, password)


