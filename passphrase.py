#!/bin/python3

import math
import os
import random
import re
import sys
import argparse


def passPhraseGenerator(args):


    # print("ARGS: "+str(args.numWords))
    diceNumber = ''
    # numWords = 2
    randomNumber = 0
    passPhrase = ''
    capitalize = False
    useNumbers = False


    if (args.numWords is None):
        numWords = 3
    elif (isinstance(args.numWords, int)):
        numWords = args.numWords
        if (args.numWords < 1):
            print ("ERROR: numWords needs to be a positive integer")
            exit()


    if (args.capitalize is None):
        capitilize = False
    elif (args.capitalize.lower().strip("'") == "true" or args.capitalize.lower().strip("'") == "t"):
        capitalize = True

    if (args.useNumbers is None):
        useNumbers = False
    elif (args.useNumbers.lower().strip("'") == "true" or args.useNumbers.lower().strip("'") == "t"):
        useNumbers = True



    if (args.delimiter is None):
        delimiter = '-'
    else:
        delimiter = args.delimiter.strip("'")
        if (len(delimiter)) > 1:
            print("Did you want a long delimiter?")

    if (args.quantity is None):
        quantity = 1
    elif (isinstance(args.quantity, int)):
        if (args.quantity < 1):
            print ("ERROR: numWords needs to be a positive integer")
            exit()
        else:
            quantity = args.quantity


    elif (isinstance(args.quantity, int)):
        if (args.quantity < 1):
            print ("ERROR: numWords needs to be a positive integer")
            exit()
        else:
            quantity = args.quantity

    # use preset types, for easy use. Over rides all above settings
    if (args.preset == 0):
        quantity = 1
        numWords = 3
        delimiter = '-'
        capitalize = False
        useNumbers = False
    elif (args.preset == 1):
        quantity = 5
        numWords = 3
        delimiter = '-'
        capitalize = True
        useNumbers = True
    elif (args.preset == 2):
        quantity = 5
        numWords = 6
        delimiter = '-'
        capitalize = True
        useNumbers = True
    elif (args.preset == 3):
        quantity = 3
        numWords = 6
        delimiter = '-'
        capitalize = False
        useNumbers = False
    elif (args.preset == 4):
        quantity = 1
        numWords = 3
        delimiter = '-'
        capitalize = True
        useNumbers = True
    else:
        print("Unknown preset, choose 0, 1, 2, 3, 4")
        exit()


    #diceList = {}
    diceList2 = []
    with open('EFF-7776-diceware.txt','r') as file:
        for line in file:
            line = file.readline()
            item = line.split()
            diceList2.append(item[1])

    for i in range(quantity):
        for j in range(numWords):
            currentWord = random.choice(diceList2)
            if(capitalize):
                currentWord = currentWord.capitalize()
            passPhrase = passPhrase + currentWord + delimiter

        if (useNumbers):
            passPhrase = passPhrase + str(random.randrange(1,9))
            print(passPhrase)
        else:
            print(passPhrase[:-1])
        passPhrase = ''

if __name__ == '__main__':


    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('--numWords', type=int, help='number of words to use, default is three (3)')
    parser.add_argument('--useNumbers', type=ascii, help='use random numbers, deafult is false')
    parser.add_argument('--capitalize', type=ascii, help='radndom capitzliaze first letter, default is false')
    parser.add_argument('--delimiter', type=ascii, help='character between phrases, default is dash - ')
    parser.add_argument('--quantity', type=int, help='quantity to generate, deafult is one (1)')
    parser.add_argument('--preset', type=int, help='preset type of passphrase, 0 is default, 1 uses numbers and capitals, 2 is more words. This overrides other options')

    args = parser.parse_args()
    passPhraseGenerator(args)
