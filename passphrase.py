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
            print ("numWords needs to be a positive integer")

    #print("ARG CAPS "+args.capitalize)
    #print("ARG CAPS "+args.capitalize.lower())
    #print("ARG CAPS "+args.capitalize.lower().strip("''"))

    if (args.capitalize is None):
        capitilize = False
        print("FALSE CAP")
    elif (args.capitalize.lower().strip("'") == "true" or args.capitalize.lower().strip("'") == "t"):
        capitalize = True
        print("TRUE CAP")

    if (args.useNumbers is None):
        useNumbers = False
    elif (args.useNumbers.lower().strip("'") == "true" or args.useNumbers.lower().strip("'") == "t"):
        useNumbers = True



    if (args.delimiter is None):
        delimiter = '-'
    else:
        delimiter = args.delimiter.strip("'")
        if (len(delimiter)) > 1:
            print("did you want a long delimiter?")


    print ("QTY"+str(args.quantity))
    if (args.quantity is None):
        quantity = 1
    elif (isinstance(args.quantity, int)):
        if (args.quantity < 1):
            print ("numWords needs to be a positive integer")
        else:
            quantity = args.quantity


    #diceList = {}
    diceList2 = []
    with open('EFF-7776-diceware.txt','r') as file:
        for line in file:
            line = file.readline()
            #print("RAW "+line)
            #print("SPLIT" + str(line.split()))
            item = line.split()
            #print(item[0])
            #print(item[1])
            #diceList[item[0]] = item[1]
            diceList2.append(item[1])
            #diceList.update(line.split())

    #print("Total words: "+ str(len(diceList)))

    #print("WORD LIST: "+ wordList[0])
    #word1 = diceList.get(wordList[0])
    #print ("Word1"+str(word1))

    print("----")
    random_entry = random.choice(diceList2)
    #print(random_entry)
    #print(len(diceList2))

    for i in range(quantity):
        for j in range(numWords):
            currentWord = random.choice(diceList2)
            if(capitalize):
                currentWord = currentWord.capitalize()
                #print(currentWord)
            passPhrase = passPhrase + currentWord + delimiter

        if (useNumbers):
            passPhrase = passPhrase + str(random.randrange(1,9))
            print(passPhrase)
        else:
            print(passPhrase[:-1])
        passPhrase = ''

if __name__ == '__main__':


    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('--numWords', type=int, help='number of words to use')
    parser.add_argument('--useNumbers', type=ascii, help='use random numbers')
    parser.add_argument('--capitalize', type=ascii, help='radndom capitzliaze first letter')
    parser.add_argument('--delimiter', type=ascii, help='delimiter between phrases')
    parser.add_argument('--quantity', type=int, help='quantity to generate')
    print ("elements seperated by space: ")
    # arr = list(map(int, input().rstrip().split()))
    args = parser.parse_args()
    passPhraseGenerator(args)
