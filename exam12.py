for x in range(101,201):
	i=1
	for k in range(2,x):
		i=i*(x%k)
	if i!=0:
		print(x)