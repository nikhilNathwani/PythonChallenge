import sys
import zipfile

#channel.html

#navigate through linked list of files in a zipfile, collecting the comments
#my code looks right but I don't get any comments! :-(

filename= 'channel.zip'

def zip_journey(start):
	next= str(start)
	comments= ""
	while '.' not in next:
		comments+=str(channel.getinfo("channel/"+str(next)+".txt").comment)
		text= channel.read("channel/"+str(next)+".txt")
		print text
		next= text.split()[-1]
	print "comments",comments

if __name__=='__main__':
	global channel
	channel= zipfile.ZipFile(open(sys.argv[1],'r'))
	zip_journey(90052)