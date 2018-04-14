import numpy as np
import random as rd
import math as ma
import matplotlib.pyplot as plt


def loadDataSet(fileName):
    fp = open(fileName, 'r')
    dataSet = []
    for line in fp.readlines():
        values = line.split()
        values = list(map(float, values))
        dataSet.append(values)
    return np.mat(dataSet)


def initVector(k, dataSet):
    m = dataSet.shape[0]
    dataSet = dataSet.tolist()
    l = list(range(m))
    initV = []
    for i in range(k):
        index = rd.choice(l)
        initV.append(dataSet[index][:])
        l.remove(index)
    return initV


def createAverageVector(cluster):
    cluster = np.array(cluster)
    averageVector = sum(cluster)/len(cluster)
    return averageVector


def calculateDis(a, b):
    a, b = np.array(a), np.array(b)
    return ma.sqrt(sum(pow(a-b, 2)))


def kMeans(dataSet, k):
    m = dataSet.shape[0]
    initV = initVector(k, dataSet)
    dataSet = dataSet.tolist()
    circulation = True
    while(circulation):
        circulation = False
        result = []
        for i in range(k):
            result.append([])
        for i in range(m):
            for j in range(k):
                dis = calculateDis(dataSet[i], initV[j])
                if j == 0:
                    minDis = dis
                    index = 0
                elif dis < minDis:
                    minDis = dis
                    index = j
            result[index].append(dataSet[i])
        newV = []
        for i in range(k):
            v = createAverageVector(result[i])
            newV.append(v)
        for i in range(k):
            if sum(pow(np.array(initV[i])-np.array(newV[i]), 2)) > 0:
                initV = newV
                circulation = True
                break
    return result


def drawChart(result):
    k = len(result)
    l = ['0', '1', '2', '3', '4', '5', '6', '7',
         '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    colorList = []
    for i in range(k):
        color = '#'
        for j in range(6):
            color += rd.choice(l)
        colorList.append(color)
    index = 0
    for cluster in result:
        xVal = []
        yVal = []
        for point in cluster:
            xVal.append(point[0])
            yVal.append(point[1])
        plt.scatter(xVal, yVal, c=colorList[index])
        index += 1
    plt.show()


fileName = 'ClusteringFile.txt'
dataSet = loadDataSet(fileName)
result = kMeans(dataSet, 4)
print(result)
drawChart(result)
