from math import log
from numpy import *


def loadingData():
    dataSet = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
               ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
               ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
               ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
               ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
               ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classList = [0, 1, 0, 1, 0, 1]

    return dataSet, classList


def toVocaList(dataSet):
    vocaList = []
    for i in range(len(dataSet)):
        for j in range(len(dataSet[i])):
            word = dataSet[i][j]
            if word not in vocaList:
                vocaList.append(word)

    return vocaList


def toValueList(vocaList, dataLine):
    numOfVoca = len(vocaList)
    valueList = zeros(numOfVoca)
    for i in range(numOfVoca):
        if vocaList[i] in dataLine:
            valueList[i] = 1

    return valueList


def trainProb(dataSet, classList):
    dataSet, classList = loadingData()
    numWords = len(toVocaList(dataSet))
    vocaList = toVocaList(dataSet)
    p1 = classList.count(1) / float(len(classList))
    p0 = classList.count(0) / float(len(classList))
    numOfp1 = ones(numWords)
    numOfp0 = ones(numWords)
    p1Sum = 2
    p0Sum = 2
    for i in range(len(dataSet)):
        if classList[i] == 1:
            numOfp1 += toValueList(vocaList, dataSet[i])
            p1Sum += sum(toValueList(vocaList, dataSet[i]))
        elif classList[i] == 0:
            numOfp0 += toValueList(vocaList, dataSet[i])
            p0Sum += sum(toValueList(vocaList, dataSet[i]))
    p1List = log(numOfp1 / float(p1Sum))
    p0List = log(numOfp0 / float(p0Sum))

    return p0, p1, p0List, p1List


def judgeYorN(realDataLine):
    dataSet, classList = loadingData()
    vocaList = toVocaList(dataSet)
    valueList = toValueList(vocaList, realDataLine)
    p0, p1, p0List, p1List = trainProb(dataSet, classList)
    pY = sum(valueList * p1List) + log(p1)
    pN = sum(valueList * p0List) + log(p0)
    if pY > pN:
        return True
    else:
        return False


def main():
    testEntry = ['love', 'my', 'dalmation']
    if judgeYorN(testEntry) == True:
        print(testEntry, ' is 1')
    else:
        print(testEntry, ' is 0')

    testEntry = ['stupid', 'garbage']
    if judgeYorN(testEntry) == True:
        print(testEntry, ' is 1')
    else:
        print(testEntry, ' is 0')


main()
