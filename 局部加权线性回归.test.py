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


def paintPoints(fileName):
    yValue = []
    xValue = []
    fp = open(fileName)
    for line in fp.readlines():
        list = line.split()
        yValue.append(float(list[-1]))
        xValue.append(float(list[-2]))
    scatter(xValue, yValue, s=5)


def lwlr(testPoint, xArr, yArr, k=1):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    num = shape(xMat)[0]
    weight = mat(eye(num))
    for i in range(num):
        diffMat = testPoint - xMat[i]
        weight[i, i] = exp(diffMat * diffMat.T / (-2.0 * k ** 2))
    xTx = xMat.T * (weight * xMat)
    ws = xTx.I * (xMat.T * (weight * yMat))
    return testPoint * ws


def lwlrTest(testxArr, xArr, yArr, k=1):
    num = shape(xArr)[0]
    yHat = zeros(num)
    for i in range(num):
        yHat[i] = lwlr(testxArr[i], xArr, yArr, k)
    return yHat


def paintLine(xArr, yHat):
    xMat = mat(xArr)
    index = xMat[:, 1].argsort(0)
    xValue = []
    yValue = []
    num = shape(xMat)[0]
    for i in range(num):
        xValue.append(xMat[int(index[i]), 1])
        yValue.append(yHat[int(index[i])])
    plot(xValue, yValue, c='green')


fileName = 'regression.data.txt'
xArr, yArr = loadDataSet(fileName)
paintPoints(fileName)
yHat = lwlrTest(xArr, xArr, yArr, 0.01)
paintLine(xArr, yHat)
show()
