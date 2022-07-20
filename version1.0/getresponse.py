import re
import random

def get_response(text):
	negative_responses = ()
	random_questions = ()

	if text in negative_responses:
		return 'exit'

	reply = get_intent(text)
	return (reply)


def get_intent(text):
	input_phrase = {
					'Greeting': r'hi\s',
					'Greeting': r'hello\s',
					'DescribeSelf': r'what is\s',
					'How': r'how\s',
					'no_match_intent': r''

					}

	for key,value in input_phrase.items():
		intent = key
		regex_pattern = value
		found_match = re.match(regex_pattern, text)

		if found_match and intent == 'no_match_intent':
			return no_match_intent()
		if found_match and intent == 'Greeting':
			return Greet()
		if found_match and intent == 'DescribeSelf':
			return DescribeSelf()
		if found_match and intent == 'How':
			return How()


def no_match_intent():
	responses = ('Please tell me more.','Tell me more!','“Why do you say that?','I see. Can you elaborate?','Interesting. Can you tell me more?','I see. How do you think?','Why?','How do you think I feel when you say that?')
	return random.choice(responses)

def Greet():
	responses = ('Hi there', 'Hi !', 'Hello')
	return random.choice(responses)

def DescribeSelf():
	responses = ('I am the Cobot', 'I am a robot')
	return random.choice(responses)

def How():
	responses = ('I am great', 'Doing well and you?', 'Thanks for asking! Good!')
	return random.choice(responses)

#get_response('what is your name ')
