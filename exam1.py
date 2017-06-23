l=list(range(1,5))
x,y,z=0,0,0
for x in l:
	for y in l:
		for z in l:
			if x!=y and x!=z and y!=z:
				print(x*100+10*y+z)
			