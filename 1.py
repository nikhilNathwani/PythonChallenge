import sys

#274877906944.html

#implement caesar cipher

def cipher(phrase):
	lst= list(phrase)
	newString= ""
	for char in lst:
		if char.isalnum():
			newString += chr(97+((ord(char)+2)%97)%26)
		else: 
			newString += char
	return newString


if __name__=="__main__":
	print cipher(sys.argv[1])
