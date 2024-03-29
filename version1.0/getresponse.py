import re
import random
#import pandas as pd
import csv 
from datetime import datetime
import google

name_index = 0
pickname_index = 0
joke_index = 0
joke_number = 0
joke_index1 = 0
joke_number1 = 0
joke_decider = 0
leaving = ('bye', 'I\'m leaving', 'bye-bye', 'see ya later', 'see you later')
bad_words = ('idiot', 'stupid', 'dumb', 'suss','sus')

numbers = []
operations = []

operation = ('/', '+', '-', '*')

def get_response(text):

	negative_responses = ()
	random_questions = ()

	if check_if_maths(text):
		return maths()

	if text in negative_responses:
		return 'exit'

	if name_index == 1 and text != 'I didnt catch that!':
		return name(text)

	if joke_index > 0:
		return Joke()

	if pickname_index == 1 and text != 'I didnt catch that!':
		return DescribeSelf(text)

	if text == 'I didnt catch that!':
		return 'I didnt catch that, try again!'

	reply = get_intent(text)
	print(reply)
	return reply

def get_intent(text):
	global leaving
	global bad_words
	global joke_decider

	for word in bad_words:
		if any(word in part for part in text.split()):
			return BAD()

	for word in leaving:
		if any(word in part for part in text.split()):
			return Goodbye()
	
	if text == 'kill yourself':
		return kill() 

	input_phrase = {
					'Greeting': r'.*\s*Hi.*',
					'Greeting2': r'.*\s*hello.*',
					'42': r'(?=.*meaning)(?=.*life)',

					'DescribeSelf': r'.*\s*your name.*',
					'myname': r'.*\s*my name.*',
					'Feeling': r'.*\s*feel.*',
					'Age2': r'.*\s*age.*',
					'Age': r'.*\s*old.*',
					'Robot': r'.*\s*robot.*',
					'Friends': r'.*\s*friend.*',	
					'Love': r'.*\s*I love you.*',

					'You': r'^you are',	
					'You2': r'^you look',	
					'Me': r'^am I',		

					'Home': r'.*\s*where.*',
					'Home2': r'.*\s*from.*',

					'Favourite': r'.*\s*favourite.*',

					'Joke': r'.*\s*joke.*',

					'Day': r'.*\s*what day.*',
					'Time': r'.*\s*what time.*',

					'What': r'.*\s*what.*',
					'How': r'.*\s*how are you.*',
					'no_match_intent': r''

					}

	for key,value in input_phrase.items():
		intent = key
		regex_pattern = value
		found_match = re.match(regex_pattern, text)

		if found_match and intent == 'Favourite':
			return Favourite(text)
		if found_match and intent == 'myname':
			return myname(text)
		if found_match and intent == 'Joke':
			if joke_decider % 2:
				joke_decider += 1
				return Joke()
			else:
				joke_decider += 1
				return Joke1()
		if found_match and intent == 'no_match_intent':
			return no_match_intent(text)
			#return Joke1()
		if found_match and intent == 'Age':
			return Age()
		if found_match and intent == 'Day':
			return Day()
		if found_match and intent == 'Time':
			return Time()
		if found_match and intent == '42':
			return FortyTwo()
		if found_match and intent == 'Love':
			return Love()
		if found_match and intent == 'Age2':
			return Age()
		if found_match and intent == 'Greeting':
			return name(text)
		if found_match and intent == 'Greeting2':
			return name(text)
		if found_match and intent == 'Feeling':
			return Feeling()
		if found_match and intent == 'DescribeSelf':
			return DescribeSelf(text)
		if found_match and intent == 'How':
			return How()
		if found_match and intent == 'Robot':
			return Robot()
		if found_match and intent == 'Friends':
			return Friends()
		if found_match and intent == 'You':
			return You(text)
		if found_match and intent == 'You2':
			return You(text)
		if found_match and intent == 'Me':
			return Me(text)
		if found_match and intent == 'What':
			return What(text)
		if found_match and intent == 'Home':
			return Home()
		if found_match and intent == 'Home2':
			return Home()

def Friends():
	return ('Lets be friends!')

def Love():
	return('I love you too !!')

def myname(text):
	words = text.split()
	return 'Hello ' + words[-1]


def You(text):
	last_word = text.split()
	if last_word[1] == 'look':
		return ('You look {} too !'.format(last_word[-1]))

	last_word = last_word [-1]
	return ('Thanks you are {} too !'.format(last_word))

def Me(text):
	last_word = text.split()
	last_word = last_word [-1]
	return ('You are {} !'.format(last_word))


def Feeling():
	responses = ('I do have feelings!', 'I have lots of feelings', 'Im feeling very annoyed right now', 'You dont have feelings!')
	return random.choice(responses)

def FortyTwo():
	return ('42')

def Favourite(text):
	thing = text.split()
	if 'colour' in text:
		return 'Orange ! I like to eat oranges too'
	if 'animal' in text:
		return 'I like frogs'
	if 'food' in text:
		return 'Oranges ! What about you ?'
	if 'tree' in text:
		return 'Pine trees!!'
	if 'toy' in text:
		return 'Lego is definitly my favourite toy'
	if 'robot' in text:
		return 'I am my favourite robot !!'
	else:
		return 'hmm i dont have a favourite ' + thing[-1]


def Day():
	dt = datetime.now()
	day = dt.strftime('%A')
	return ('It is ' + day)

def Time():
	now = datetime.now()
	current_time = now.strftime("%H:%M")
	return('It is ' + current_time)

def Age():
	then = datetime(2022,6,5)        # Initial Commit
	now  = datetime.now()                         
	duration = str(now - then) 
	duration = duration.split(',',1)
	duration = duration[0]
	responses = ('I am {} old !'.format(duration))
	return (responses)

def BAD():
	responses = ('Dont use that word.', 'That is very mean', 'Thats not very nice', 'No you are!','I am telling on you','Do you want to get in trouble?')
	return random.choice(responses)

def kill():
	return 'I cant I am a robot! Ha!'

def Goodbye():
	responses = ('Nice Chatting!', 'Bye !', 'See ya!', 'Talk soon')
	return random.choice(responses)

def name(text):
	global name_index
	if name_index == 0:
		responses = ('What is your name?')
		name_index = 1
		return responses
	if name_index == 1:
		isolate = text.split(' ')
		name_greet = 'Hi ' + str(isolate[-1]) + ' , nice to meet you!'
		responses = name_greet
		name_index = 0
		return responses

def Joke1():
	global joke_index1, joke_number1
	if joke_index1 == 0:
		responses = (
			'What do dog robots do?', 
			'What happens when a robot dies?', 
			'Why did the robot cross the road?', 
			'Why are robots boring?',
			'Why did the robot need to go to therapy?',
			'What do you call a robot who likes to row?',
			'Why did the robot get upset?',
			'Why did the robot sneeze?',
			'How did the robot eat its food?',
			'What is a robots favourite snack?'
			)
		joke_index1 = 1
		#return responses[joke_number]

	if joke_index1 == 1:
		responses2 = (
			'They byte!',
			'They rust in peace.',
			'The chicken programmed it',
			'They just drone on and on',
			'Because it always bot-tled up its emotions!',
			'A row-bot',
			'Because everyone was pushing its buttons!',
			'It had a virus...',
			'It took a mega-byte',
			'Microchips'
			)
		joke_number1 += 1
		joke_index1 = 0
		if joke_number1 > 9:
			joke_number1 = 0

		space = '								'
		full_joke = responses[joke_number1-1] + space + responses2[joke_number1-1]

		return full_joke

def Joke():
	global joke_index, joke_number	
	if joke_index == 0:
		joke_index = 1
		return '		Knock Knock'
		
	if joke_index == 1:
		responses = (
			'			Who',
			'		Wooden Shoe',
			'		Oink Oink',
			'		BB eight',
			'		A broken pencil',
			'		Owls say',
			'		Boo'

			)
		joke_index = 2
		return	responses[joke_number]

	if joke_index == 2:
		responses = (
			'		Are you an owl ?',		
			'		Wooden Shoe like to know',
			'		Are you a pig or an owl ?',
			'		Nobody I hope !',
			'		Nevermind, its pointless',
			'		Yes they do',
			'		Why are you crying ?'

			)
		joke_index = 0
		joke_number	+= 1
		if joke_number	== 7:
			joke_number	= 0
		return	responses[joke_number-1]


def no_match_intent(text):
	responses = ('Please tell me more.','Tell me more!','“Why do you say that?','I see. Can you elaborate?','Interesting. Can you tell me more?','I see. How do you think?','Why?','How do you think I feel when you say that?')
	#responses = google.goooogle(text)
	#responses = responses 
	return random.choice(responses)
	#return random.choice(responses)

def Greet():
	responses = ('Hi there', 'Hi !', 'Hello')
	return random.choice(responses)

#def DescribeSelf(text):
#	global pickname_index
#	if pickname_index == 0:
#		responses = ('I dont have a name ! Suggest one!')
#		pickname_index = 1
#		return responses
#	if pickname_index == 1:
#		with open('NameSuggestions.csv','a',encoding='UTF8') as file:
#			writer = csv.writer(file)
#			writer.writerow([text])
#		opinion = ('Ooh, I like ', 'Hmm not sure about ', 'I dont know how I feel about ')
#		suggestion = random.choice(opinion) + text + ''
#		responses = suggestion
#		pickname_index = 0
#		return responses

def DescribeSelf(text):
	responses = ('My name is Clover !')
	return responses

def How():
	responses = ('I am great', 'Doing well and you?', 'Thanks for asking! Good!')
	return random.choice(responses)

def What(text):
	#responses = google.goooogle(text)
	#responses = responses 
	responses = 'I dont know'
	return responses

def Robot():
	responses = ('I am not a robot!', 'I like to think I am a person', 'Personally, I consider myself a human')
	return random.choice(responses)

def Home():
	responses = ('I am from planet Zen!', 'I am an alien robot from space!')
	return random.choice(responses)

def maths():
    global numbers, operations, answer
    index = 0 
    complete = 0
    
    if operations.count('*') > 0 or operations.count('/') > 0:
        for x in operations:
            if x == '*' and complete == 0:
                answer = float(numbers[index]) * float(numbers[index + 1])
                complete = 1
                popping = index
            if x == '/' and complete == 0:
                answer = float(numbers[index]) / float(numbers[index + 1])
                complete = 1
                popping = index
            index += 1
            
    elif operations.count('+') > 0 or operations.count('-') > 0:
        for x in operations:
            if x == '+' and complete == 0:
                answer = float(numbers[index]) + float(numbers[index + 1])
                complete = 1
                popping = index
            if x == '-' and complete == 0:
                answer = float(numbers[index]) - float(numbers[index + 1])
                complete = 1
                popping = index
            index += 1

    if len(operations) > 1 and complete == 1:
        operations.pop(popping)
        numbers.pop(popping)
        numbers.pop(popping)
        numbers.insert(popping,answer)
        maths()

	
    operations.clear()
    numbers.clear()
    answer = str(answer)
	
    return ('The answer is ' + answer + ' !')

def check_if_maths(text):
    global operation, numbers
    
    for x in text.split(' '):
        if x.isdigit():
            numbers.append(x)
        for expression in operation:
            if expression == x:
                operations.append(x)
    if len(operations) > 0 and len(numbers) > 1:
        return True
    else:
        operations.clear()
        numbers.clear()
    
printing = get_response('meaning life')
print(printing)



