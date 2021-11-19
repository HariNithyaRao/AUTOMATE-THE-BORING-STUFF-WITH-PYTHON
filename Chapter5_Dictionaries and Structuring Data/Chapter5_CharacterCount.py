#															-------------<<<<<<<<|  CHARACTER_COUNT |>>>>>-------------


# importing pprint to get a pretty text 
#--------------------------------------

import pprint

# a string
#----------
													
message='Count the frequency of the letters in this message'
	
# created a dictionary
#---------------------

count={}	

#The program loops over each character in the message variable’s string,counting how often each character appears
#----------------------------------------------------------------------------------------------------------------
													
for i in message:												
	
	#The setdefault() method callensures that the key is in the count dictionary (with a default value of 0 )
	count.setdefault(i,0)										
	count[i]=count[i]+1

#print(count)
pprint.pprint(count)
