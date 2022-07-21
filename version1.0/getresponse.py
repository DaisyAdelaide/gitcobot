import re
import random

name_index = 0

def get_response(text):

	negative_responses = ()
	random_questions = ()

	if text in negative_responses:
		return 'exit'

	if name_index == 1:
		return name(text)

	reply = get_intent(text)
	print(reply)
	return (reply)


def get_intent(text):
	input_phrase = {
					'name': r'.*\s*Hi.*',
					'Greeting': r'.*\s*hello.*',
					'DescribeSelf': r'.*\s*name.*',
					'How': r'how\s',
					'Animal':  r'.*\s*animal.*',
					'Colour': r'.*\s*colour.*',
					'Food': r'.*\s*food.*',
					'What': r'.*\s*what.*',
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
			return DescribeSelf()
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

def DescribeSelf():
	responses = ('I am the Cobot, no name yet !')
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

#get_response('whats yiur animal favourite')
