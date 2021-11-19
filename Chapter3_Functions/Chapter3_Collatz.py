n=int(input("Enter a number: \n"))
def collatz(number):
	if number%2==0:
		print(number//2)
		if number//2!=1:
			collatz(number//2)
	else:
		print(3*number+1)
		if 3*number+1!=1:
			collatz(3*number+1)
collatz(n)
