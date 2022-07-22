import re
import random

name_index = 0
pickname_index = 0

def get_response(text):

	negative_responses = ()
	random_questions = ()

	if text in negative_responses:
		return 'exit'

	if name_index == 1 and text != 'I didnt catch that!':
		return name(text)

	if pickname_index == 1 and text != 'I didnt catch that!':
		return DescribeSelf(text)

	if text == 'I didnt catch that!':
		return 'I didnt catch that, try again!'

	reply = get_intent(text)
	print(reply)
	return (reply)


def get_intent(text):
	input_phrase = {
					'name': r'.*\s*Hi.*',
					'Greeting': r'.*\s*hello.*',
					'DescribeSelf': r'.*\s*name.*',
					'How': r'.*\s*how.*',
					'Animal':  r'.*\s*animal.*',
					'Colour': r'.*\s*colour.*',
					'Food': r'.*\s*food.*',
					'What': r'.*\s*what.*',
					'Robot': r'.*\s*robot.*',
					'Home': r'.*\s*where.*',
					'Home': r'.*\s*from.*',
					'no_match_intent': r''

					}

	for key,value in input_phrase.items():
		intent = key
		regex_pattern = value
		found_match = re.match(regex_pattern, text)

		if found_match and intent == 'no_match_intent':
			return no_match_intent()
		if found_match and intent == 'Greeting':
			return name(text)
		if found_match and intent == 'DescribeSelf':
			return DescribeSelf(text)
		if found_match and intent == 'How':
			return How()
		if found_match and intent == 'Animal':
			return Animal()
		if found_match and intent == 'Colour':
			return Colour()
		if found_match and intent == 'Food':
			return Food()
		if found_match and intent == 'What':
			return What()
		if found_match and intent == 'Robot':
			return Robot()
		if found_match and intent == 'Home':
			return 
			Home()



def name(text):
	global name_index
	if name_index == 0:
		responses = ('What is your name?')
		name_index = 1
		return responses
	if name_index == 1:
		name_greet = 'Hi ' + text + ' , nice to meet you!'
		responses = name_greet
		name_index = 0
		return responses

def no_match_intent():
	responses = ('Please tell me more.','Tell me more!','“Why do you say that?','I see. Can you elaborate?','Interesting. Can you tell me more?','I see. How do you think?','Why?','How do you think I feel when you say that?')
	return random.choice(responses)

def Greet():
	responses = ('Hi there', 'Hi !', 'Hello')
	return random.choice(responses)

def DescribeSelf(text):
	global pickname_index
	if pickname_index == 0:
		responses = ('I dont have a name ! Suggest one!')
		name_index = 1
		return responses
	if name_index == 1:
		with open('NameSuggestions.csv','a',encoding='UTF8') as file:
			writer = csv.writer(file)
			writer.writerow([text])
		name_greet = 'Ooh, I like ' + text 
		responses = name_greet
		pickname_index = 0
		return responses

def How():
	responses = ('I am great', 'Doing well and you?', 'Thanks for asking! Good!')
	return random.choice(responses)

def Animal():
	responses = ('I like frogs')
	return responses

def Colour():
	responses = ('Orange ! I like to eat oranges too')
	return responses

def Food():
	responses = ('Oranges ! What about you ?')
	return responses

def What():
	responses = ('What was the question?')
	return responses

def Robot():
	responses = ('I am not a robot!', 'I like to think I am a person', 'Personally, I consider myself a frog','shhhhhh it is a secret')
	return random.choice(responses)

def Home():
	responses = ('I am from planet Zen!', 'I am an alien robot from space!')
	return random.choice(responses)

#get_response('whats yiur animal favourite')
