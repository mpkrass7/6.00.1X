# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 11:53:07 2018

@author: pl89155
"""

import itertools 

productList = ['International', 'Payables', 'Receivables', 'Liquidity Management', 'PINACLE']

WORDLIST_FILENAME = "Product Tuples.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    WORDLIST_FILENAME = "Product Tuples.txt"
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    tupleList = []
    for line in inFile:
        wordList.append(line.strip())
    print("  ", len(wordList), "words loaded.")
#    return wordList
    list1 = wordList[:len(wordList)//2]
    list2 = wordList[(len(wordList)//2):len(wordList)]
    for i in range(len(list1)):
        tupleList.append((list2[i], list1[i]))
    return tupleList

clientList = loadWords()


def powerset(prodList, combos, clientTuples):
    "Returns every combination for a sorted list of products"
    sortProducts = sorted(prodList)
    clientDict = {}
    comboDict = {}
    possibleCombos = itertools.combinations(sortProducts, combos)
    for i in list(possibleCombos):
            comboDict[i] = 0
#    print(comboDict)
    for client in clientTuples:
        if client[0] in clientDict:
            clientDict[client[0]].append(client[1])
        else:
            clientDict[client[0]] = [client[1]]
    for i in clientDict:
        if len(clientDict[i]) == combos:
            for combo in comboDict:
#                print(clientDict[i])
#                print(combo[0])
                check = True
                for product in clientDict[i]:
#                    print(product)
                    if product not in combo:
                        check = False
                if check == True:
#                    print("Success!")
                    comboDict[combo] += 1
#                    print("Success!")
#                    comboList[1] += 1            
    return comboDict

comboThree = powerset(productList, 3, clientList)
maxCountEntry = ""
maxCount = 0
for entry in comboThree:
    print("Product set includes:", entry, "with", comboThree[entry], "occurence(s)\n")

def maxAll(prodList, clients):
    for group in range(1, len(prodList)):
        groupNum = group
        maxCount = 0
        maxCountEntry = ""
        groupDict = powerset(productList, group, clientList)
        for occurence in groupDict:
            if groupDict[occurence] > maxCount:
                maxCount = groupDict[occurence]
                maxCountEntry = occurence
        print("Biggest set of", groupNum, "products is", maxCountEntry, "with count of:", maxCount)

maxAll(productList, clientList)
    
#dataTest = pd.DataFrame.from_dict(powerset(productList, 3, clientList))


#dataTest2 = pd.read_excel('TestProductUsage.xlsx', converters = {'Relationship ID': str})
#print(dataTest2.head())
#dataTest2 = dataTest2.pivot(index = 'Relationship ID', columns = 'Product Family',\
#                      values = 'Dummy')
#dataTest2 = dataTest2.fillna(0)
#print(dataTest2.head())
