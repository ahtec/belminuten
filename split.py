#!/usr/bin/python
import datetime
woord = ""
positie = 1
totaalMinuten = 0
totaalSeconden = 0
file = open("Naamloos", "r")
for line in file:
    for character in line:
	if character == " " :
		if positie == 2:
			woordArray = woord.split(":")
			minuten = int(woordArray[0])
			seconden = int(woordArray[1])
			totaalSeconden = totaalSeconden + seconden 
			if totaalSeconden > 59 :
				totaalMinuten = totaalMinuten +1
				totaalSeconden = totaalSeconden - 60	
			totaalMinuten = totaalMinuten + minuten 
		        print(woord  + " " + str(totaalMinuten) + " " + str(totaalSeconden) )


			woord = ""
			positie = 1
		else:
			positie = 2	
	else:
		if positie == 2:
			woord = woord + character

woordArray = woord.split(":")
minuten = int(woordArray[0])
seconden = int(woordArray[1])
totaalSeconden = totaalSeconden + seconden 
if totaalSeconden > 59 :
	totaalMinuten = totaalMinuten +1
	totaalSeconden = totaalSeconden - 60	
	totaalMinuten = totaalMinuten + minuten 
print(woord  + " " + str(totaalMinuten) + " " + str(totaalSeconden) )
