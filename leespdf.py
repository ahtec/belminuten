#!/usr/bin/python
import datetime
import os

#install pyDF2
# /Users/gerard/Library/Python/2.7/bin/pip install PyPDF2

# importing all the required modules
import PyPDF2

# creating an object 
#file = open('factuur_september_2020.pdf', 'rb')
#file = open('factuur_februari_2020.pdf', 'rb')

#file = open('/Users/gerard/Downloads/factuur_februari_2020.pdf', 'rb')#
#file = open('/Users/gerard/Downloads/factuur_maart_2020.pdf', 'rb')
spitText = ""
for file in os.listdir("/Users/gerard/Documents/facturen/ben/"):
	if (file.endswith("_2020.pdf")) or (file.endswith("_2019.pdf")):
		if (file.endswith("_2020.pdf")):
			splitText = "-2020"
		if (file.endswith("_2019.pdf")):
			splitText = "-2019"
		

		fileObject = open(os.path.join("/Users/gerard/Documents/facturen/ben/", file),'rb')
		fileReader = PyPDF2.PdfFileReader(fileObject)
		page         = fileReader.getPage(1)
		page_content = page.extractText()
		tekst        =  page_content.encode('utf-8')

		regels = tekst.split(splitText)
		totaalMinuten = 0
		totaalSeconden = 0
		seconden = 0
		minuten = 0
		duurStr = ""
		woordArray = "jjj:jj".split(":")
		for regel  in regels:
			deelRegel    = regel[5:]
			if "binnen bundel" in regel[4:]:
				if deelRegel[4] == "b":
					duurStr = deelRegel[0:4]
					woordArray = duurStr.split(":")
					minuten  = int(woordArray[0])
					seconden = int(woordArray[1])
					totaalSeconden = totaalSeconden + seconden
					if totaalSeconden > 59 :
						totaalMinuten = totaalMinuten +1
						totaalSeconden = totaalSeconden - 60	
					totaalMinuten = totaalMinuten + minuten 

				if deelRegel[5] == "b":
					duurStr = deelRegel[0:5]
					woordArray = duurStr.split(":")
					minuten  = int(woordArray[0])
					seconden = int(woordArray[1])
					totaalSeconden = totaalSeconden + seconden
					if totaalSeconden > 59 :
						totaalMinuten = totaalMinuten +1
						totaalSeconden = totaalSeconden - 60	
					totaalMinuten = totaalMinuten + minuten 
#####				print(woordArray[0]  + " " + str(totaalMinuten) + " " + woordArray[1] + " " + str(totaalSeconden) )	
		print(str(totaalMinuten) + " minuten     " + str(totaalSeconden) + " seconden ")
	print(os.path.join("/Users/gerard/Documents/facturen/ben/", file))


