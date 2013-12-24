import pprint, pickle
import sys
import requests


#peak.html

#load in a pickled (marshalled) string, unmarsall it, and print the banner, awesome!

def performPickle(url):
	r= requests.get(url)
	data= pickle.loads(str(r.text))
	for line in data:
		toPrint=""
		for pound in line:
			toPrint += ''.join([pound[0]]*pound[1])
		print toPrint

if __name__ == '__main__': 
	performPickle(sys.argv[1])