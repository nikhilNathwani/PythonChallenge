import sys
import requests
import unicodedata
import random
import string
from bs4 import BeautifulSoup

#linkedlist.py

#follow chain of URLs, each specifying a new query value

def followChain(url):
  	  r= requests.get(url)
  	  if len(r.text.split())==1: 
  	  	return r.text
  	  next= str(r.text.split()[-1])
	  return followChain(base+'?nothing='+next)



if __name__ == '__main__':
	global base
	base= str(sys.argv[1].split('?')[0])
	print followChain(sys.argv[1])
