#Import core libraries: math, os, binascii, base64, getpass from getpass
import math
from  getpass import getpass
import os
import binascii
import base64

#Define colored printing functions
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

#Introduction to the script, press enter to continue
prGreen("Welcome to ISC, the Inferior Security Algorithm!")
prGreen("All code used was created by RBXII3, with the exception of any libraries, which can be viewed by editing this file.")
prGreen("The program is still in Alpha, and is extremely instable, so feel free to request mergers at https://github.com/psharma04/ISC-Algorithm")
raw_input("Press Enter to continue...")

#Take data, passphrase
dataRaw = raw_input("Please enter the data to encrypt: ")
if dataRaw == None:
    prRed("Error: No data entered. Killing script...")
    exit
passphraseRaw = getpass(prompt="Please enter a password: ")
if passphraseRaw == None:
    print "Error: No data entered. Killing script..."
    exit


#Convert to Hex. Uses binascii. LIFESAVER!!!!!!!!!
dataHex = binascii.hexlify(dataRaw)
passHex = binascii.hexlify(passphraseRaw)

#Might add Base64 encode here

#Convert hex to integer so we can do maths.
dataInt = int(dataHex, 16)
passInt = int(passHex, 16)
