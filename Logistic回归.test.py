from numpy import *
from random import *
from matplotlib.pyplot import *

fileName = 'Logistic回归.test'
fileLines = 1000


def writingFile():
    with open(fileName, 'w') as pf:
        for line in range(fileLines):
            label = choice([0, 1])
            x1 = uniform(0, 20)
            if label == 1:
                x2 = 5 * x1 + 20 + uniform(-10 * 20, 50 * 20)
            elif label == 0:
                x2 = 5 * x1 + 20 + uniform(-50 * 20, 10 * 20)
            pf.write(str(x1) + '\t\t' + str(x2) + '\t\t' + str(label) + '\n')


def readingFile(fileName):
    dataSet = []
    labelList = []
    with open(fileName) as pf:
        for line in pf.readlines():
            currentList = [1]
            lineList = line.split()
            currentList.append(float(lineList[0]))
            currentList.append(float(lineList[1]))
            labelList.append(int(lineList[2]))
            dataSet.append(currentList)
    print(dataSet)
    print(labelList)

    return dataSet, labelList


def displayPoints(dataSet, labelList):
    for lineNum in range(len(dataSet)):
        if labelList[lineNum] == 1:
            color = 'red'
        elif labelList[lineNum] == 0:
            color = 'blue'
        scatter(dataSet[lineNum][1], dataSet[lineNum][2], c=color, edgecolors='none', s=5)
    title('Logistic', fontsize=30)
    xlabel('x1', fontsize=15)
    ylabel('x2', fontsize=15)

'''
def sigmoid(inX):
    value = 1.0 / (1 + exp(-inX))
    return value


'''

def sigmoid(inX):
    if inX < 0:
        return 0.0
    elif inX == 0:
        return 0.5
    else:
        return 1.0
'''

def getWeights(dataSet, labelList):
    dataSet = mat(dataSet)
    labelList = mat(labelList).T
    m, n = shape(dataSet)
    weights = ones((n, 1))
    alpha = 0.01
    maxCycles = 5000
    for i in range(maxCycles):
        h = sigmoid(dataSet*weights)
        error = labelList - h
        weights = weights + alpha * dataSet.T * error

    return weights
'''


def getWeights(dataSet, labelList, numItem=200):
    m, n = shape(dataSet)
    dataSet = array(dataSet)
    weights = ones(n)
    for j in range(numItem):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4.0 / (1.0 + i + j) + 0.01
            randomIndex = int(uniform(0, len(dataIndex)))
            h = sigmoid(sum(weights * dataSet[randomIndex]))
            error = labelList[randomIndex] - h
            weights = weights + error * alpha * dataSet[randomIndex]
            del (dataIndex[randomIndex])
    return weights


def displayLine(weights):
    x = arange(0, 20, 0.05)
    y = -(float(weights[0]) + x * float(weights[1])) / float(weights[2])
    plot(x, y, c='green')


def showAll(dataSet, labelList, weight):
    displayPoints(dataSet, labelList)
    displayLine(weights)
    show()


def calculateAccuracyRate(weights, dataSet, labelList):
    a, b, c = float(weights[0]), float(weights[1]), float(weights[2])
    count = 0
    whole = len(dataSet)
    for index in range(len(dataSet)):
        x0, x1, x2, label = dataSet[index][0], dataSet[index][1], dataSet[index][2], labelList[index]
        value = a * x0 + b * x1 + c * x2
        if (value > 0 and label == 1) or (value < 0 and label == 0) or value == 0:
            count += 1
    rate = 100 * float(count) / whole
    print('The accuracy is %.2f' % rate, '%.')


writingFile()
dataSet, labelList = readingFile(fileName)
weights = getWeights(dataSet, labelList)
showAll(dataSet, labelList, weights)
calculateAccuracyRate(weights, dataSet, labelList)
