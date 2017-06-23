
Y=[100,60,40,20,10,0]
k=[0.01,0.015,0.03,0.05,0.075,0.1]

i=float(input('净利润'))
y=0

for x in range(0,6):
	if i>I[x]:
		sum=(sum+x-I[x])*k[x]
	i=I[x]
print(sum)