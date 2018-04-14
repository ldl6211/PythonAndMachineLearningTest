from matplotlib.pyplot import *
from math import log
from operator import itemgetter

decisionNode = dict(boxstyle='sawtooth', fc='0.8')
leafNode = dict(boxstyle='round4', fc='0.8')
arrow_args = dict(arrowstyle='<-')


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


def createTree(dataSet, labels):
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
        myTree[bestFeatureLabel][item] = createTree(newBataSet, newLabels)
    return myTree


def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.axl.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction', xytext=centerPt, textcoords='axes fraction',
                            va='center', ha='center', bbox=nodeType, arrowprops=arrow_args)


def createPlot(inTree):
    fig = figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.axl = subplot(111, frameon=False, **axprops)
    plotTree.totalW = float(getNumLeaves(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5 / plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree, (0.5, 1.0), '')
    show()


def getNumLeaves(myTree):
    numLeaves = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeaves += getNumLeaves(secondDict[key])
        else:
            numLeaves = 1
    return numLeaves


def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.axl.text(xMid, yMid, txtString)


def plotTree(myTree, parentPt, nodeTxt):
    numLeaves = getNumLeaves(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeaves)) / 2.0 / plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD


def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth


def main():
    myData = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    createPlot(createTree(myData, labels))


main()
