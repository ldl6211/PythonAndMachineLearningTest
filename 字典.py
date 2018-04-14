from numpy import *
aline_0 = {'color': 'yellow', 'sex': 'male', 'weight': 50, 'hight': 100}
print(aline_0)
iter = list(aline_0.items())
print(iter[0][0])
print(aline_0['hight'])
aline_0['hair'] = 'long'
print(aline_0)
aline_0['hair'] = 'short'
print(aline_0)
del aline_0['color']
print(aline_0)
for key, value in aline_0.items():
    print(key+':'+str(value))
print('***********')
for key in aline_0.keys():
    print(key)
print('#################')
for value in aline_0.values():
    print(value)
print('^^^^^^^^^^^^^^^^^')
aline_0['lover'] = 'male'
for value in set(aline_0.values()):
    print(value)
print('&&&&&&&&&&&&&&')
for value in aline_0.values():
    print(value)
print()
alines = []
for num in range(50):
    new_aline = {'color':'red','sex':'male'}
    alines.append(new_aline)
for aline in alines:
    print(aline)
print('$$$$$$$$$$$$$$$')
aline_0['hair'] = ['long','red']
print(aline_0)
print('%%%%%%%%%%%%%')
aline_0['hair'] = {'lenth':10,'color':'red'}
print(aline_0['hair']['color'])
print('@@@@@@@@@@@@@@@@@@@@@@@@')
def f(x):
    return x**2
a = [1,2,3,4,5]
b = map(f,a)
for i in b:
    print(i)
b = list(b)
print(b)

