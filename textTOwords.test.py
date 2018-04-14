from re import *

while(True):
    fileName = input('请输入要读取的文件名：')
    try:
        with open(fileName) as pf:
            mySent = pf.read()
    except FileNotFoundError:
        print('Cannot find the file!')
    else:
        reg = compile('\W+')
        list = [word.lower() for word in reg.split(mySent) if len(word)>0]
        print(list)
        set = set(list)
        print(set)
        break