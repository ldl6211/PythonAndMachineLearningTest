from numpy import *
from operator import *


def classify(inx, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inx, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDisIndix = argsort(distances)
    classCount = {}
    for i in range(k):
        currentLabel = labels[sortedDisIndix[i]]
        classCount[currentLabel] = classCount.get(currentLabel, 0) + 1
    sortedClassCount = sorted(list(classCount.items()), key=itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def main():
    dataSet = array([[1, 1], [2, 3], [4, 3], [2, 2], [1, 2], [5, 6], [7, 6], [6, 6], [5, 8], [0, 0]])
    labels = array(['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b'])
    i = 0
    count = 0
    for item in dataSet:
        test = classify(item, dataSet, labels, 5)
        print('The program tells me it\'s ' + test + ', the real answer is ' + labels[i] + '!')
        if labels[i] == test:
            count += 1
        i += 1
    print('The rate is ' + str(100 * count / float(len(labels))) + '% !')

main()
