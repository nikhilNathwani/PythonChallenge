import sys
import requests
from bs4 import BeautifulSoup, Comment
import re

#equality.html

#look in HTML source, use regex to find pattern xXXXxXXXx (upper/lower-case), get middle letter

def getSource(url):
	r= requests.get(url)
	soup= BeautifulSoup(r.text)
	comments= soup.findAll(text=lambda text:isinstance(text, Comment))
	pattern= re.compile('[a-z][A-Z]{3,3}[a-z][A-Z]{3,3}[a-z]')
	matches= pattern.findall(str(comments[0]))
	matchString= ''.join(elem[4] for elem in matches)
	return matchString


if __name__=="__main__":
	print getSource(sys.argv[1])