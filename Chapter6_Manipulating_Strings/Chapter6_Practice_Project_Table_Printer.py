#

#
#-------------
tableData=[]
while True:
	a=list(map(str,input().split()))
	if a==\n:
		break
	tableData.append(a)
for i in tableData:
	print(" ".join(i).rjust())
	
