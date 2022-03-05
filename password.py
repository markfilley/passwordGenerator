#!/bin/python3

import math
import os
import random
import re
import sys
import argparse


def passwordGenerator(args):


    # default settings for password
    capitalize = False
    useNumbers = False
    specialEnd = False
    numNumbers = 0
    numSpeicals = 0
    length = 15
    specialSet = 0

    # init vars
    diceNumber = ''
    randomNumber = 0
    passPhrase = ''
    abcList = ''
    numberList = ''
    specialList = ''
    countNumbers = 0
    countSpecials = 0

    # define special character lists, some LDAP registries limit characters
    specialList0 = '!@#$%^&*.-_' # special set of ASCII characters
    specialList1 = ',<>?/[]:;{}' # extended set of speical ASCII characters
    specialList2 = '!#.-^_' # limited
    specialList3 = '!@#$%^&*.-_,<>?/[]:;{}'  # full list, sets 0 and 1


    if (args.length is None):
        length = 15
    elif (isinstance(args.length, int)):
        length = args.length
        if (args.length < 1):
            print ("length needs to be a positive integer, reccomend 15 or higher")
            exit()

    if (args.numNumber is None):
        numNumbers = 3
    elif (isinstance(args.numNumber, int)):
        numNumbers = args.numNumber
        if (args.numNumber < 1):
            print ("ERROR: numNumbers needs to be a positive integer")
            exit()

    if (args.specialSet is None):
        specialSet = 0
        specialList = specialList1
    elif (isinstance(args.specialSet, int)):
        specialSet = args.specialSet
        if (specialSet == 0):
            specialList = specialList0
        elif (specialSet == 1):
            specialList = specialList1
        elif (specialSet == 2):
            specialList = specialList2
        elif (specialSet == 3):
            specialList = specialList3
        else:
            print ("ERROR: special set must be a number, {0,1,2,3}.")
            exit()

    if (args.numSpecial is None):
        numSpecials = 2
    elif (isinstance(args.numSpecial, int)):
        numSpecials = args.numSpecial
        if (args.numSpecial < 1):
            print ("ERROR: numNumbers needs to be a positive integer, recommend 2")
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
    elif (args.ambiguous.lower().strip("'") == "true" or args.ambiguous.lower().strip("'") == "t"):
        ambiguous = True

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


    # use preset types, for easy use. Over rides all above settings
    if (args.preset == 0):
        capitalize = False
        useNumbers = False
        specialEnd = False
        numNumbers = 0
        numSpeicals = 0
        length = 15
        specialSet = 0
        ambiguous = True
        quantity = 1
    elif (args.preset == 1):
        capitalize = True
        useNumbers = True
        specialEnd = False
        numNumbers = 2
        numSpeicals = 2
        length = 15
        specialSet = 3
        ambiguous = False
        quantity = 5
    elif (args.preset == 2):
        capitalize = True
        useNumbers = True
        specialEnd = True
        numNumbers = 4
        numSpeicals = 4
        length = 32
        specialSet = 0
        ambiguous = True
        quantity = 1
    elif (args.preset == 3):
        capitalize = True
        useNumbers = True
        specialEnd = False
        numNumbers = 0
        numSpeicals = 0
        length = 20
        specialSet = 3
        ambiguous = False
        quantity = 5
    elif (args.preset == 4):
        capitalize = True
        useNumbers = True
        specialEnd = False
        numNumbers = 2
        numSpeicals = 2
        length = 25
        specialSet = 0
        ambiguous = True
        quantity = 1
    else:
        print("Unknown preset, choose 0, 1, 2, 3")

    if (ambiguous == False):
        abcList = 'abcdefghjkpqrstuvwxyz'
        numberList = '234578'
    else:
        abcList = 'abcdefghijklmnopqrstuvwxyz'
        numberList = '0123456789'


    for i in range(quantity):
        countNumbers = 0
        countSpecials = 0
        password = ''
        for j in range(length):

            characterType = random.randrange(1,3) # 1 letters, 2 number, 3 special
            if (characterType == 1):
                if (capitalize and (random.randrange(1,2)==1)):
                    password = password + random.choice(abcList).upper()
                else:
                    password = password + random.choice(abcList)
            elif ((characterType == 2) and (countNumbers < numNumbers)):
                password = password + random.choice(numberList)
                countNumbers = countNumbers + 1
            elif ((characterType == 3) and (countSpecials < numSpecials)):
                print("special set")
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

        print(password + " " + str(len(password)))


if __name__ == '__main__':


    parser = argparse.ArgumentParser(description='password generator')
    parser.add_argument('--length', type=int, help='character length of password, default is  fifteen (15)')
    parser.add_argument('--useSpecial', type=ascii, help='use special characters')
    parser.add_argument('--capitalize', type=ascii, help='use capital letters, default True')
    parser.add_argument('--useNumbers', type=ascii, help='use numbers, default  True')
    parser.add_argument('--numSpecial', type=int, help='number of special characters, default is two (2)')
    parser.add_argument('--numNumber', type=int, help='number of numbers, default is two (2)')
    parser.add_argument('--quantity', type=int, help='how many passwords to generate, default is one (1)')
    parser.add_argument('--ambiguous', type=ascii, help='do not use characters that look similar, like 1 and l')
    parser.add_argument('--specialEnd', type=ascii, help='allow special characters at beginning and end of password, default True')
    parser.add_argument('--specialSet', type=int, help="special set 1 = '!@#$%^&*.-_'  ', 2 = <>?/[]:;{}' 3 = '!#.-^_' 4 = '!@#$%^&*.-_,<>?/[]:;{}' ")
    parser.add_argument('--preset', type=int, help="preset type of passp, 0 is default, 1 uses numbers and capitals, 2 is more words. This overrides other options")
    args = parser.parse_args()
    passwordGenerator(args)
