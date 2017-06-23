l=[1,1]
x=1
y=1
n=0
max=int(input())
while n<max:
	z=y
	y=x+y
	x=z
	l.append(y)
	n=n+1
print(l)