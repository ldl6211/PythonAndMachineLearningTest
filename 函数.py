def hello():
    print('hello_world')
hello()
def pri(str1='none',str2='none'):
    print(str1)
    print(str2)
pri('hello',' python')
print('**********')
pri(str2='world',str1='hello ')
pri()
def rt_ls(int):
    a = []
    for num in range(int):
        a.append('a')
    return a
print(rt_ls(10))
print('%%%%%%%%%%%%%%%%%')
def p(*aa):
    for a in aa:
        print(a)
p('a','b','c')
def usr(**inf):
    d = {}
    for key, val in inf.items():
        d[key] = val
    return d
a = usr(a='a',b='b',c='c')
print(a)
a['d']='d'
print(a)