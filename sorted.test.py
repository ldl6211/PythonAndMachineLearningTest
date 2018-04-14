from numpy import *
from operator import *
dict = {'first':1,'second':2,'third':3,'zero':0}
ls = list(dict.items())
print(ls)
sortedLs = sorted(ls,key=itemgetter(1),reverse=True)
print(sortedLs)