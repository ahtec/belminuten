#!/usr/bin/python
import datetime
import os
import PyPDF2
#  dez prg leest in de directory alle pdf en die eindigen op pdf
# in elke pdf leest i de gebelde minuten , sommeert per pdf
#  g.w. doets  7 nov 2020

#install pyDF2
# /Users/gerard/Library/Python/2.7/bin/pip install PyPDF2

def maandnummer(i):
        switcher={
                'januari':1,
                'februari':2,
                'maart':3,
                'april':4,
                'mei':5,
                'juni':6,
                'juli':7,
                'augustus':8,
                'september':9,
                'oktober':10,
                'november':11,
                'december':12
             }
	return( switcher.get(i))

def jaarmaand (erin):
	erinWoordenArray1 = erin.split(".")
	erinWoordenArray2 = erinWoordenArray1[0].split("_")
	return (erinWoordenArray2[2] +  '{:>3}'.format(maandnummer(erinWoordenArray2[1])))



spitText = ""
outputArray=[]
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
#####				print(woordArray[0]  + " :  " + str(totaalMinuten) + " " + woordArray[1] + " " + str(totaalSeconden) )	

		outputArray.append(jaarmaand(file)+ " " + '{:>5}'.format(totaalMinuten) + ":" + '{:>2}'.format(totaalSeconden) + " in " + file)
outputArray.sort()
for outputregel in outputArray:
	print(outputregel)


####		print(jaarmaand(file)+ " " + str(totaalMinuten) + " :   " + str(totaalSeconden) + "    in    " + file)
#####	print(os.path.join("/Users/gerard/Documents/facturen/ben/", file))


