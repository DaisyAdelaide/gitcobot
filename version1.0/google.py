from bs4 import BeautifulSoup
import requests

def goooogle(question):

	headers = {
	    'User-agent':
	    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
	}


	html = requests.get('https://www.google.com/search?q="{}'.format(question), headers=headers)
	soup = BeautifulSoup(html.text, 'html.parser')

	answer = 'i dont know'
	typee = ''

	try:
		answer = soup.select_one('.hgKElc').text
		if 'https' in answer:
			answer = answer.split('https',1)
			answer = answer [0]
		typee = 'one'
	except:
		answer = 'Not this one'

	#This option is the dictionary
	if answer == 'Not this one':
		try:
			answer = soup.select_one('.MjjYud').text
			answer = answer.split(';',1)
			answer = answer [1]
			answer = answer.split('.',1)
			answer = answer [0]
			typee = 'two'
		except:
			answer = 'Not this one'

	if answer == 'Not this one':
		try:
			answer = soup.select_one('.t2b5Cf').text
			typee = 'two'
		except:
			answer = 'Not this one'

	#This one is the first line of a landmark i think
	if answer == 'Not this one':
		try:
			answer = soup.select_one('.kno-rdesc').text
			answer = answer.split('Description',1)
			answer = answer [1]
			answer = answer.split('. ',1)
			answer = answer [0]
			typee = 'three'
		except:
			answer = 'Not this one'

	#does the first line of a wesite, sometimes good sometimes bad, will always return something
	if answer == 'Not this one':
		try:
			answer = soup.select_one('.lyLwlc').text
			answer = answer.split('— ',1)
			answer = answer [1]
			answer = answer.split('.',1)
			answer = answer [0]
			typee = 'four'
		except:
			answer = 'I dont know! google'

	return answer

#print(goooogle('tell me a joke'))


#can do what,how,where

# This kinda works !!!! Fix it up a bit
# Try is not working maybe if statements ? 