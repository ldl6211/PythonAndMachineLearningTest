from numpy import *
from matplotlib.pyplot import *


def loadDataSet(fileName):
    with open(fileName) as fp:
        numX = len(fp.readline().split()) - 1
    dataSet = []
    labelMat = []
    fp = open(fileName)
    for line in fp.readlines():
        list = line.split()
        currentList = []
        for i in range(numX):
            currentList.append(float(list[i]))
        dataSet.append(currentList)
        labelMat.append(float(list[-1]))
    return dataSet, labelMat


def standRegres(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    xTx = xMat.T * xMat
    weight = xTx.I * (xMat.T * yMat)
    return weight


def paintPoints(fileName):
    yValue = []
    xValue = []
    fp = open(fileName)
    for line in fp.readlines():
        list = line.split()
        yValue.append(float(list[-1]))
        xValue.append(float(list[-2]))
    scatter(xValue, yValue, s=10)


def paintLine(weight, xArr):
    xList = []
    for list in xArr:
        xList.append(list[-1])
    xList.sort()
    xMin = xList[0]
    xMax = xList[-1]
    yMin = float(weight[0] + weight[1] * xMin)
    yMax = float(weight[0] + weight[1] * xMax)
    xValue = [xMin, xMax]
    yValue = [yMin, yMax]
    plot(xValue, yValue, c = 'green')


xArr, yArr = loadDataSet('regression.data.txt')
w = standRegres(xArr, yArr)
paintPoints('regression.data.txt')
paintLine(w, xArr)
show()
