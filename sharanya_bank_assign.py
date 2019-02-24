#!/usr/bin/env.python

'''
* open the account
* Deposit
* withdraw
* bal check
* quit
'''

balance = 0
def help_menu():
    print("Welcome to BOFA \n")
    print("Options:\n")
    print(" 1.Open the account\n 2. Deposit\n 3. WithDraw \n 4. Balance Check \n 5. Quit")


def validate_option():
    if (option < 1) or (option > 5):
        print("please enter a valid number")


def open_account():
    global balance
    balance = int(raw_input("enter the minimum balance to open the account"))
    print("Successfully opened the account")

def deposit():
    global balance
    deposit_amt = int(raw_input("enter the amount you want to deposit"))
    if deposit_amt <=0:
        print("Enter valid amount to deposit")
    else:
        balance += deposit_amt
        print("Successfully Deposited")

def withdraw():
    global balance
    withdraw_amt = int(raw_input("enter the amount you want to withdraw"))
    if balance >= withdraw_amt:
        balance -= withdraw_amt
        print("withdrawal successful")
    else:
        print("insufficient funds")


def balance_check():
    global balance
    print("Your current account balance is " + str(balance))




while True:
    help_menu()
    option = int(raw_input("Please enter your option"))
    validate_option()
    if option == 1:
        open_account()
    elif option == 2:
        deposit()
    elif option == 3:
        withdraw()
    elif option == 4:
        balance_check()
    elif option == 5:
        break
    else:
        continue









