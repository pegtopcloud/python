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

def fib(max):
	a,b,n=0,1,0
	while n<max:
		yield b
		a,b=b,a+b
		n=n+1
	return 'done'


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
	
