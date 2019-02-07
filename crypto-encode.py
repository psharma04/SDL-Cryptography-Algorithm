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
    key_check = getpass(prompt="Please verify your passcode: ")
    if key != key_check:
        keycheck = getpass(prompt="That wasn't right. You have 3 attempts remaining. Please try again: ")
        if key != key_check:
            keycheck = getpass(prompt="That wasn't right. You have 2 attempts remaining. Please try again: ")
            if key != key_check:
                keycheck = getpass(prompt="That wasn't right. You have 2 attempts remaining. Please try again: ")
                if key !=keycheck:
                    passwd()
enc0de = 130261921814816914322611266142071681981781251702372051421981291438281934689215149113652392462091668189101231822345215133241170866614710969219220651991957222921057172184942914917949513416620119552301352261382291091811422914813516317315514136218238180176191342271679097249132441251262042385131392104711272082512712311118221399742091622694216145961348116658944531841322512573123635182186591261211691310924825416822422701873138191755523525321621905717495220431191221283114012821623417232202234191998858591761406524712519415922111826492181742512251578741412785196172009674253164111208177238204125206174181119133402121499923489207170209240777019519495131329365721617563227616724368231185215941011171392261881198816823152801539019373819322921915817198371893923424163171161091792256142212227151160105161102682431351292102011833922221420311610964225172291101021852402431951231251712115693101185920485571422011915654032194125200137249142232101582291341051012342028523325224087231297812831106285872281232011414741088615715575487496739120221133215136134717411659106175172193781501171627615224915421515178630184149241121161247473357186336311184205276315123012522632206612789512717710319449192621725516916111918686227731862078338190581201821664612024337114180213120792010524431236138152205321422251454191107198158215461741831271922398058195208141
#Introduction
print("Welcome to SSC, the simple symmetric cipher algorithm by RBXII3!")
print("This cipher is still in beta, so feel free to report issues at https://rbxii3.com/SSC")
#Input data. Code will enter a while loop if no data is entered for the primary input.
primary_data = raw_input("Please input a piece of data to encode: ")
while primary_data is None:
        primary_data = raw_input("No data entered. Please enter a piece of data to encode: ")
passwd()
hash = raw_input("Please enter an encryption key (optional step): ")
if hash is None:
    hash = enc0de
