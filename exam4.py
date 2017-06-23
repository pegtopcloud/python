year=int(input('year:'))
month=int(input('month:'))
day=int(input('day:'))
d={1:31,2:59,3:90,4:120,5:151,6:181,7:212,8:243,9:273,10:304,11:334,0:0}
run=0
if year%100==0:
	if int(year)%400==0:
		run=1
	else:
		run=0
else:
	if year%4==0:
		run=1
	else:
		run=0
m=d[month-1]
if(month<3):
	run=0
print(run,run+m+day)