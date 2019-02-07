#Created by RBXII3. All rights reserved. source at https://rbxii3.tech/SSC
#Import functions. Some may be used later, such as turtle.
import math
import turtle
import time
import sys
from getpass import getpass

#Define core functions such as the password verificationnprompt, which involves a loopback.
def passwd():
    #Once an input is taken, prompt for a password to encode with. Uses the GetPass Library.
    key = getpass(prompt="Please enter a password: ")
    while key is None:
        key = getpass(prompt="No password entered. Please enter a password: ")
    #Verify password. If there is an error, give three attempts, and if all are failed, go back to the initial password prompt.
    keycheck = getpass(prompt="Please verify your passcode: ")
    if key != keycheck:
        keycheck = getpass(prompt="That wasn't right. You have 3 attempts remaining. Please try again: ")

    if key != keycheck:
        keycheck = getpass(prompt="That wasn't right. You have 2 attempts remaining. Please try again: ")

    if key != keycheck:
            keycheck = getpass(prompt="That wasn't right. You have 2 attempts remaining. Please try again: ")

    if key !=keycheck:
        passwd()
enc0de = 1302619218189215149113652396921922065199195722292105717218010524431236138152205321422251454191107198158215461741831271922398058195208141
#Introduction
print("Welcome to SSC, the simple symmetric cipher algorithm by RBXII3!")
print("This cipher is still in beta, so feel free to report issues at https://rbxii3.com/SSC")
#Input data. Code will enter a while loop if no data is entered for the primary input.
primary_data = input("Please input a piece of data to encode: ")
while primary_data is None:
        primary_data = input("No data entered. Please enter a piece of data to encode: ")
passwd()
hash = getpass(prompt="Please enter an encryption key over 64 characters long (numbers only, no spaces, optional step): ")
hashlength = len(hash)
if hashlength < 64:
    print("Hash too short, reverting to default hash:")
    hash = enc0de
if hash is None:
    print("No hash entered, reverting to default hash:")
print(enc0de)

#Time for some MATHS!!!!!!
#First we convert everything to decimal
