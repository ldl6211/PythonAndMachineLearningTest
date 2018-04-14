from math import log
from operator import itemgetter


def caluShannonEnt(dataSet):
    dataSetSize = len(dataSet)
    labelCount = {}
    for itme in dataSet:
        currentLabel = itme[-1]
        if currentLabel not in labelCount.keys():
            labelCount[currentLabel] = 0
        labelCount[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCount.keys():
        prob = float(labelCount[key]) / dataSetSize
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def splitDataSet(dataSet, axis, value):
    newList = []
    for item in dataSet:
        if item[axis] == value:
            currentList = item[:axis]
            currentList.extend(item[axis + 1:])
            newList.append(currentList)
    return newList


def chooseBestFeatureToSplit(dataSet):
    bestFeature = -1
    bestInfoGain = 0.0
    baseEnt = caluShannonEnt(dataSet)
    numFeature = len(dataSet[0]) - 1
    for i in range(numFeature):
        featList = [example[i] for example in dataSet]
        featSet = set(featList)
        newEnt = 0.0
        for value in featSet:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = float(len(subDataSet)) / len(dataSet)
            newEnt += prob * caluShannonEnt(subDataSet)
        infoGain = baseEnt - newEnt
        if infoGain > bestInfoGain:
            bestFeature = i
            bestInfoGain = infoGain
    return bestFeature


def majorityCount(classList):
    classDict = {}
    for item in classList:
        if item not in classDict.keys():
            classDict[item] = 0
        classDict[item] += 1
    sortedClassDict = sorted(list(classDict.items()), key=itemgetter(1), reverse=True)
    return sortedClassDict[0][0]


def creatTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCount(classList)
    bestFeature = chooseBestFeatureToSplit(dataSet)
    bestFeatureLabel = labels[bestFeature]
    myTree = {bestFeatureLabel: {}}
    del (labels[bestFeature])
    featValue = [example[bestFeature] for example in dataSet]
    featValueSet = set(featValue)
    for item in featValueSet:
        newBataSet = splitDataSet(dataSet, bestFeature, item)
        newLabels = labels[:]
        myTree[bestFeatureLabel][item] = creatTree(newBataSet, newLabels)
    return myTree


def main():
    myData = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    print(creatTree(myData, labels))


main()
