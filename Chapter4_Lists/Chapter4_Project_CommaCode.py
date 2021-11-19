def Comma_Code(l):
	s=''
	for i in l[0:len(l)-1]:
		s+=i+", "
	s+="and "+l[-1]
	print(s)
Comma_Code(['apples', 'bananas', 'tofu', 'cats'])
