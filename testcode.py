# -*- coding:utf-8 -*-

def my_abs(x):
	if x>=0:
		return x
	else:
		return -x

def calc(*numbers,num=10):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum+num
#print(calc(1,2,num=20))

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
	
#print(f1(1,2,e=3,d='a',f='b'))
#print(f2(1, 2, e=88, d=99, ext=None))
n=1
if n=1:
	print('Y')