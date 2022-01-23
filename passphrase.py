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
    parser.add_argument('--numWords', type=int, help='number of words to use, default is 3')
    parser.add_argument('--useNumbers', type=ascii, help='use random numbers, deafult is false')
    parser.add_argument('--capitalize', type=ascii, help='radndom capitzliaze first letter, default is false')
    parser.add_argument('--delimiter', type=ascii, help='character between phrases, default is dash')
    parser.add_argument('--quantity', type=int, help='quantity to generate, deafult is one')
    args = parser.parse_args()
    passPhraseGenerator(args)
