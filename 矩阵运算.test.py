from numpy import *
ar1 = array([[1,2],[3,4],[5,6]])
ar2 = array([[1,2],[3,4],[5,6]])
print('ar1-ar2:')
print(ar1-ar2)
print('ar1+ar2:')
print(ar1+ar2)
print('ar1**2:')
print(ar1**2)
print('***************')
mar1 = mat(ar1)
print('mat(ar1):\n',mar1)
print('mar1.T:\n',mar1.T)
print('mar1.transpose():\n',mar1.transpose())
print('mat(ar1):\n',mar1)
mar2 = mat(ar2)
print('mar1*2:\n',mar1*2)
print('***************')
aa = ones((5,2))
print('ones((5,2)):\n',aa)
print('&&&&&&&&&&&&&&&&&&&')
a = mat([1,2,3,4,5])
b = a.T
c = a*b
print(c)
d = mat(eye(5))
for i in range(5):
    d[i,i] = i+1
a = mat([[1,2],[3,4],[5,6],[7,8],[9,8]])
print(d*a)
a = mat([2,1,3,5,4])
b = a.argsort()
print(b)
print('@@@@@@@@@@@@@@@@')
a = mat([[1,2,3,4,5],[2,6,4,5,6]])
print(a)
print(a.T)
print(a*a.T)
print(a.I*a)
a = mat([[1,2,3],[2,5,4],[3,4,5]])
print(a)
print(a.I)
print(a.I*a)