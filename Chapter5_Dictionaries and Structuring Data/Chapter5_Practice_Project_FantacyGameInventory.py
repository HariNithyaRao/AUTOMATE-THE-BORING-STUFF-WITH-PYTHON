#											   							----------<<<<| FantacyGameInventory |>>>>-----------


# DEFINING A FUNCTION TO GET INVENTORIES OR ITEMS AND THEIR COUNT
#----------------------------------------------------------------

def displayInventory(inventory):
	count=0
	for j in inventory.values():
		count+=j
	print("Total number of inventories:",count)

# CREATING A DICTIONARY TO STORE THE ITEM AND IT'S COUNT
#-------------------------------------------------------

inventory={}
for i in range(10):
	k,v=input().split()
	inventory[k]=int(v)	

#CALLING THE FUNCTION
#----------------------

displayInventory(inventory)
