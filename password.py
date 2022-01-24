#!/bin/python3

import math
import os
import random
import re
import sys
import argparse


def passwordGenerator(args):


    diceNumber = ''
    randomNumber = 0
    passPhrase = ''
    capitalize = False
    useNumbers = False
    specialEnd = True
    numNumbers = 0
    numSpeicals = 0
    countNumbers = 0
    countSpecials = 0
    abcList = ''
    numberList = ''

    length = 0

    specialSet = 1
    specialList1 = '!@#$%^&*.-_' # special set of ASCII characters
    specialList2 = ',<>?/[]:;{}' # extended set of speical ASCII characters
    specialList3 = '!#.-^_' # limited, some systems only allow basic special characters
    specialList4 = '!@#$%^&*.-_,<>?/[]:;{}'  # full list

    specialList = ''

    if (args.length is None):
        length = 15
    elif (isinstance(args.length, int)):
        length = args.length
        if (args.length < 1):
            print ("numWords needs to be a positive integer")
            exit()

    if (args.numNumber is None):
        numNumbers = 3
    elif (isinstance(args.numNumber, int)):
        numNumbers = args.numNumber
        if (args.numNumber < 1):
            print ("ERROR: numNumbers needs to be a positive integer")
            exit()

    if (args.specialSet is None):
        specialSet = 1
        specialList = specialList1
        print ("Here0")
    elif (isinstance(args.specialSet, int)):
        specialSet = args.specialSet
        if (specialSet == 1):
            specialList = specialList1
            print ("Here1")
        elif (specialSet == 2):
            specialList = specialList2
            print ("Here2")
        elif (specialSet == 3):
            specialList = specialList3
            print ("Here3")
        elif (specialSet == 4):
            specialList = specialList4
            print ("Here4")
        else:
            print ("ERROR: special set must be a number.")
            print ("Here5")
            exit()

    if (args.numSpecial is None):
        numSpecials = 2
    elif (isinstance(args.numSpecial, int)):
        numSpecials = args.numSpecial
        if (args.numSpecial < 1):
            print ("ERROR: numNumbers needs to be a positive integer")
            exit()

    userLength = numSpecials + numNumbers
    if (userLength >= length):
        print("ERROR: Requested number "+str(numNumbers)+" and special length "+str(numSpecials)+" greater than your max length of:" +str(length))
        exit()

    if (args.capitalize is None):
        capitilize = False
    elif (args.capitalize.lower().strip("'") == "true" or args.capitalize.lower().strip("'") == "t"):
        capitalize = True

    if (args.specialEnd is None):
        specialEnd = True
    elif (args.specialEnd.lower().strip("'") == "false" or args.specialEnd.lower().strip("'") == "f"):
        specialEnd = False

    if (args.ambiguous is None):
        ambiguous = False
        abcList = 'abcdefghjkpqrstuvwxyz'
        numberList = '234578'
    elif (args.ambiguous.lower().strip("'") == "true" or args.ambiguous.lower().strip("'") == "t"):
        ambiguous = True
        abcList = 'abcdefghijklmnopqrstuvwxyz'
        numberList = '0123456789'

    if (args.useNumbers is None):
        useNumbers = False
    elif (args.useNumbers.lower().strip("'") == "true" or args.useNumbers.lower().strip("'") == "t"):
        useNumbers = True


    if (args.quantity is None):
        quantity = 1
    elif (isinstance(args.quantity, int)):
        if (args.quantity < 1):
            print ("ERROR: quantity needs to be a positive integer")
            exit()
        else:
            quantity = args.quantity

    for i in range(quantity):
        countNumbers = 0
        countSpecials = 0
        password = ''
        for j in range(length):

            characterType = random.randrange(1,4)
            if (characterType == 1):
                if (capitalize and (random.randrange(1,2)==1)):
                    password = password + random.choice(abcList).upper()
                else:
                    password = password + random.choice(abcList)
            elif ((characterType == 2) and (countNumbers < numNumbers)):
                password = password + random.choice(numberList)
                countNumbers = countNumbers + 1
            elif ((characterType == 3) and (countSpecials < numSpecials)):
                if ((j == 0) or (j == length -1)) and specialEnd:
                    countSpecials = countSpecials + 1
                    password = password + random.choice(specialList)
                elif (j > 0 and j < length -1):
                    password = password + random.choice(specialList)
                    countSpecials = countSpecials + 1
                else:
                    password = password + random.choice(abcList)
            else:
                password = password + random.choice(abcList)

        print(password)


if __name__ == '__main__':


    parser = argparse.ArgumentParser(description='password generator')
    parser.add_argument('--length', type=int, help='character length of password, default is 15')
    parser.add_argument('--useSpecial', type=ascii, help='use special')
    parser.add_argument('--capitalize', type=ascii, help='use capital letters, default True')
    parser.add_argument('--useNumbers', type=ascii, help='use numbers, default  True')
    parser.add_argument('--numSpecial', type=int, help='number of special characters, default is 2')
    parser.add_argument('--numNumber', type=int, help='number of numbers, default is 2')
    parser.add_argument('--quantity', type=int, help='how many passwords to generate, default is 1')
    parser.add_argument('--ambiguous', type=ascii, help='do not use characters that look similar, like 1 and l')
    parser.add_argument('--specialEnd', type=ascii, help='allow special characters at beginning and end of password, default True')
    parser.add_argument('--specialSet', type=int, help="special set 1 = '!@#$%^&*.-_'  ', 2 = <>?/[]:;{}' 3 = '!#.-^_' 4 = '!@#$%^&*.-_,<>?/[]:;{}' ")
    args = parser.parse_args()
    passwordGenerator(args)
