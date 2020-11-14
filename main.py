#This is an Audio Book Python Project

import pyttsx3 #library installed using command : pip install pyttsx3
import PyPDF2 #library installed using command : pip install PyPDF2

book = open('Horror.pdf', 'rb') #read file in binary format
pdfReader = PyPDF2.PdfFileReader(book)

#get number of pages
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init() #initialize speaker
#loop for reading pages 1-5
for num in range(1,5):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()