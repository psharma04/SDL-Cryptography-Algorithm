#Import core libraries: math, os, binascii, base64, getpass from getpass, randint and seed from random
import math
import os
import binascii
import base64
from  getpass import getpass
from random import randint
from random import seed

#Define simple/common colored printing functions
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

#Introduction to the script, press enter to continue
prYellow("Welcome to ISC, the Inferior Security Algorithm!")
prYellow("All code used was created by RBXII3, with the exception of any libraries, which can be viewed by editing this file.")
prYellow("The program is still in Alpha, and is extremely instable, so feel free to request mergers at https://github.com/psharma04/ISC-Algorithm.")
prYellow("I recommend closing any CPU- or RAM-intensive programs such as browsers, photo/video editors, basically anything that isn't this window.")
prYellow("There's some huge maths in the background, so the more free your RAM and CPU are, the better.")
print("\033[1;32;40m"+"Press Enter to continue...")
raw_input("")
#Generate a default seed in case the user decides to enter nothing for some reason. Uses a little programming joke
seed("1337h4x")
#Take data, passphrase
dataRaw = raw_input("\033[0;32;40m"+"Please enter the data to encrypt: ")
if dataRaw == None:
    prRed("Error: No data entered. Killing script...")
    exit
passphraseRaw = getpass(prompt="Please enter a password: ")
#check for blank password not working yet
if passphraseRaw == None:
    print "Error: No data entered. Killing script..."
    exit
if passphraseRaw == "\r":
    print "Error: No data entered. Killing script..."
    exit
if passphraseRaw == "\n":
    print "Error: No data entered. Killing script..."
    exit
if passphraseRaw == "\r\n":
    print "Error: No data entered. Killing script..."
    exit
#End of blank password check

#Confirm data and passcode
print("Confirmation sequence: If any of this information is incorrect, please terminate the script with Ctrl-C.")
print("Otherwise, press Enter.")
print("Data (Unencrypted): " + dataRaw)
raw_input()

#Store some big primes as hardcoded numbers for encrypting
prime1 = 1066340417491710595814572169
prime2 = 19134702400093278081449423917
mersenne = 170141183460469231731687303715884105727
#Store a normal number that is also pretty big, just to make it even harder
big = 10001710691975609453355002313078545061039000955081336141319784075645585
#Convert to Hex. Uses binascii. LIFESAVER!!!!!!!!!

dataHex = binascii.hexlify(dataRaw)
passHex = binascii.hexlify(passphraseRaw)

#Might add Base64 encode here

#Convert hex to integer so we can do maths.
dataInt = int(dataHex, 16)
passInt = int(passHex, 16)
#Generate a seed from a pseudorandom algorithm so that it can be reversed by the reciever.
randomiser = randint(0,8589934593)
print randomiser

#Final mathematics, uses a hardcoded prime number, a reandomly generated large number, plus the data, password and seed.
#Uses a mersenne prime, because I like Mersenne Primes, as well as two Fibonnaci Primes, because they're just great.
output = randomiser*passInt*dataInt*prime1*prime2*mersenne*4*big
print output
print randint(0,100000009999999999999999999999999999999999999999999999999999999999913719616611289541053076968599661479447733154317979395978282004892330091592423742509631213523303249483737807190892121608031150007560498448141526131827611328380371122916283599575998507974909152240)
