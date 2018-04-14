a = [1,2,3,4,5,6]
b = list(range(1,10,2))
print(a,b)
c = [val**2 for val in b if val>2]
print(c)
print(a == b)
a = b
print(a == b)
a[0]=0
print(a)
print(b)
c = [0,3,5,7,9]
print(c)
print(a == c)
print(1>2 or 2>1)
print('*****************')
print('0' not in a)
t = 0
if t:
    print('#########')
elif t+3:
    print('$$$$$$$$$$$')