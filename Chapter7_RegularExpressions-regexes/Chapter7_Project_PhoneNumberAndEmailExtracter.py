#																		   <<<<<<<<<<| PHONENUMBER AND EMAIL EXTRACTER |>>>>>>>>>


import re, pyperclip

text=str(pyperclip.paste())

#phoneRegex=re.compile(r'\d\d\d\d\d\d\d\d\d\d') 		#this regex for general tendigit phonenumbers.

phoneRegex=re.compile(r'''(
						(\d{3}|\(d{3}\))?				#AREA OF CODE
						(\s|-|\.)?						#SEPARATOR
						(\d{3})							#FIRST 3 DIGITS
						(\s|-|\.)						#SEPARATOR
						(\d{4})							#LAST 4 DIGITS
						(\s*(ext|x|ext.)\s*(\d{2,5}))?	#EXTENSION
						)''',re.VERBOSE)

list_of_phonenum=[]
for groups in phoneRegex.findall(text):
	list_of_phonenum.append(groups[0])

EmailRegex=re.compile(r'''(
		[a-zA-Z0-9._%+-]+	#USERNAME
		@					#@ SYMBOL
		[a-zA-Z0-9.-]+		#DOMAIN NAME
		(\.[a-zA-Z]{2,4})	#DOT-SOMETHING
		)''',re.VERBOSE)		
list_of_emails=[]
for groups in EmailRegex.findall(text):
	list_of_emails.append(groups[0])

if len(list_of_phonenum)>0:
	pyperclip.copy('\n'.join(list_of_phonenum))
	print('Copied to Cipboard')
	print('\n'.join(list_of_phonenum))
else:
	print('No phone numbers  found.')

if len(list_of_emails)>0:
	pyperclip.copy('\n'.join(list_of_emails))
	print('Copied to Cipboard')
	print('\n'.join(list_of_emails))
else:
	print('No emails found.')

