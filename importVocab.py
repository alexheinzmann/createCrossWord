#This class will check to see if a Kindle is plugged in, pull the highlights,
#identify single word highlights, and the create a map pairing words with
#definitions

#temporarily just read in My Clippings.txt from this directory
inputFilePath = 'My Clippings.txt'

#open the file
inputFile = open(inputFilePath, 'r')

#test
print inputFile.readline()
print inputFile.readline()

#iterate through file and find single-word highlights. 

	#find next line blank line. The following line is the quote

	#store the quote in variable "quote"

	#strip quote of extra characters (.,!- etc.)

	#if quote is single word
		#lookup dictionary definition in kindle
		#add to quote_dictionary

#iterate through file and add new quotes to user's database


