#											                                 -------<<<<<| TIC-TAC-TOE |>>>>>>------

# USING DICTIONARY DATASTRUCTURE/DATATYPE FOR THE TIC-TAC-TOE BOARD
#------------------------------------------------------------------

hash={'top-L':' ','top-M':' ','top-R':' ',
	  'mid-L':' ','mid-M':' ','mid-R':' ',
	  'low-L':' ','low-M':' ','low-R':' '}

# PRINTING THE TIC-TAC-TOE BOARD ON TO THE SCREEN
#------------------------------------------------

def printboard(board):
	print(hash['top-L'] + '|' + hash['top-M'] + '|' + hash['top-R'])
	print('-----')
	print(hash['mid-L'] + '|' + hash['mid-M'] + '|' + hash['mid-R'])
	print('-----')
	print(hash['low-L'] + '|' + hash['low-M'] + '|' + hash['low-R'])

# DEFINING A FUNCTION FOR ANNOUNCING THE WINNER
#----------------------------------------------

def winner(hash,turn):
	if hash['top-L']==hash['top-M']==hash['top-R']!=' ' or hash['low-L']==hash['low-M']==hash['low-R']!=' ' or hash['mid-L']==hash['mid-M']==hash['mid-R']!=' ' or hash['top-L']==hash['mid-L']==hash['low-L']!=' ' or hash['top-M']==hash['mid-M']==hash['low-M']!=' ' or hash['top-R']==hash['mid-R']==hash['low-R']!=' ' or hash['top-L']==hash['mid-M']==hash['low-R']!=' ' or hash['top-R']==hash['mid-M']==hash['low-L']!=' ' or hash['top-L']==hash['mid-L']==hash['low-L']!=' ':
		return turn

# GETTING THE INPUTS FROM THE USER
#---------------------------------

turn='X'
for i in range(9):
	printboard(hash)
	hash[input("It's your turn "+turn+".Whats your move?: \n")]=turn
	win= winner(hash,turn)
	if win== ("X" or "O"):
		print("winner is",turn)
		printboard(hash)
		break
	if turn=='X':
		turn='O'
	else:
		turn="X"
