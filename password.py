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
    numNumbers = 0
    numSpeicals = 0
    countNumbers = 0
    countSpecials = 0
    abcList = ''
    numberList = ''

    length = 0

    specialList1 = '!@#$%^&*.-_'
    specialList2 = ',<>?/[]:;{}'
    specialList3 = '!#.-^_'


    if (args.length is None):
        length = 15
    elif (isinstance(args.length, int)):
        length = args.length
        if (args.length < 1):
            print ("numWords needs to be a positive integer")

    if (args.numNumber is None):
        numNumbers = 3
    elif (isinstance(args.numNumber, int)):
        numNumbers = args.numNumber
        if (args.numNumber < 1):
            print ("ERROR: numNumbers needs to be a positive integer")
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
        countSpecial = 0
        password = ''
        for j in range(length):

            characterType = random.randrange(1,4)
            if (characterType == 1):
                password = password + random.choice(abcList)
            elif ((characterType == 2) and (countNumbers < numNumbers)):
                password = password + random.choice(numberList)
                countNumbers = countNumbers + 1
            elif ((characterType == 3) and (countSpecials < numSpecials)):
                password = password + random.choice(specialList1)
                countSpecials = countSpecials + 1
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
    args = parser.parse_args()
    passwordGenerator(args)
