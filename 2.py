import sys
import requests
from bs4 import BeautifulSoup, Comment

#ocr.html

#look in HTML source, find hidden message in comment

def getSource(url):
	r= requests.get(url)
	soup= BeautifulSoup(r.text)
	comments= soup.findAll(text=lambda text:isinstance(text, Comment))
	comments= [''.join(elem for elem in list(comment) if elem.isalnum()) for comment in comments]
	print comments[1]

if __name__=="__main__":
	getSource(sys.argv[1])