import Image
import sys
from StringIO import StringIO
import requests

#oxygen.html

#see comment in getGrayLine function

def isGray(pix):
	return pix[0]==pix[1] and pix[1]==pix[2]

def findGrayscaleLine():
	for i in range(img.size[0]):    # for every pixel:
		two_prev= [(1,2,3),(1,2,3)]
		for j in range(img.size[1]):
			if pix[i,j]==two_prev[1] and two_prev[0]==two_prev[1] and isGray(pix[i,j]):
				return j
			else:
				two_prev[0]= two_prev[1]
				two_prev[1]= pix[i,j]

def getGrayLine(rowInd):
	lst= [pix[i,rowInd] for i in range(0,img.size[0],7) if isGray(pix[i,rowInd])]
	prev= (-1,-1,-1)
	newList=[]
	#somehow, when I had this and didn't have te "7" argument in range(0,img...etc), I cut
	#out duplicate DIGITS in the final number sequence [105, 110, 116, 101, 103, 114, 105, 
	#116, 121], i.e. 110 became 10 and 116 became 16
	#for i in range(len(lst)):
	#	if lst[i]!=prev:
	#		prev=lst[i]	
	#		newList += [lst[i]]
	return lst #newList

def genMessageFromGrays(lst):
	ords= [elem[0] for elem in lst] #get R value of RGB
	return ''.join([chr(elem) for elem in ords])


if __name__=="__main__":
	global img,pix
	r = requests.get(sys.argv[1])
	img = Image.open(StringIO(r.content))
	pix= img.load()
	rowInd= findGrayscaleLine()
	line= getGrayLine(rowInd)
	print genMessageFromGrays(line)
	print img.size[0], img.size[1]
	print [chr(num) for num in [105, 110, 116, 101, 103, 114, 105, 116, 121]]


