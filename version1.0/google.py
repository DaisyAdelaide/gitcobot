from bs4 import BeautifulSoup
import requests

headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

html = requests.get('https://www.google.com/search?q="where is google', headers=headers)
soup = BeautifulSoup(html.text, 'html.parser')

answer = 'i dont know'


#try:
#answer = soup.select_one('.SPZz6b').text

#except:
	#answer = soup.select_one('.t2b5Cf').text

answer = soup.find('div',class_='SPZz6b').find_next('span').text


print(answer)




# This kinda works !!!! Fix it up a bit
# Try is not working maybe if statements ? 