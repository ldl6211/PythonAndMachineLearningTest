with open('/home/ldl/桌面/aaa.txt') as pf:
    lines = pf.readlines()
print(lines)
with open('/home/ldl/桌面/bbb.txt', 'w') as wf:
    wf.write('abc\n')
    wf.write('bcd\n')
with open('/home/ldl/桌面/bbb.txt', 'a') as af:
    af.write('ccc\n')
print('****************')
try:
    print(3/0)
except ZeroDivisionError:
    pass
s = 'acb abc sbc'
ss = s.split('b')
print(ss)