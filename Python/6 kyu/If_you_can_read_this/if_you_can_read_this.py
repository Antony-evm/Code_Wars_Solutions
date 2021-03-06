#You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet)
#Note:

#The set of used punctuation is .!?.
#Punctuation should be kept in your return string, but spaces should not.
#Xray should not have a dash within.
#Every word and punctuation mark should be seperated by a space ' '.
#There should be no trailing whitespace

def to_nato(words):
	my_dict = ({'a':'Alfa','b':'Bravo','c':'Charlie','d':'Delta','e':'Echo','f':'Foxtrot',
			   'g':'Golf','h':'Hotel','i':'India','j':'Juliett','k':'Kilo','l':'Lima',
			   'm':'Mike','n':'November','o':'Oscar','p':'Papa','q':'Quebec','r':'Romeo',
			   's':'Sierra','t':'Tango','u':'Uniform','v':'Victor','w':'Whiskey',
			   'x':'Xray','y':'Yankee','z':'Zulu'})
	
	words = words.lower().replace(' ','')
	return ''.join([my_dict[i]+' ' if i in my_dict.keys() else i+' ' for i in words ]).rstrip()