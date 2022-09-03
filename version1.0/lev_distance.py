import numpy

def find_match(isolate):
	all_distances = []
	lowest = 10
	returning = ''

	words = (
		'zero',
		'one',
		'two',
		'three',
		'four',
		'five',
		'six',
		'seven',
		'eight',
		'nine',
		'ten',
		'eleven',
		'twelve',
		'thirteen',
		'fourteen',
		'fifteen',
		'sixteen',
		'seventeen',
		'eighteen',
		'nineteen',
		'twenty-one',
		'twenty-two',
		'twenty-three',
		'twenty-four',
		'twenty-five',
		'twenty-six',
		'twenty-seven',
		'twenty-eight',
		'twenty-nine',
		'thirty-one',
		'thirty-two',
		'thirty-three',
		'thirty-four',
		'thirty-five',
		'thirty-six',
		'thirty-seven',
		'thirty-eight',
		'thirty-nine',
		'forty-one',
		'forty-two',
		'forty-three',
		'forty-four',
		'forty-five',
		'forty-six',
		'forty-seven',
		'forty-eight',
		'forty-nine',
		'fifty-one',
		'fifty-two',
		'fifty-three',
		'fifty-four',
		'fifty-five',
		'fifty-six',
		'fifty-seven',
		'fifty-eight',
		'fifty-nine',


		)

	for word in words:
		wordDistance = LDM(word,isolate)
		if wordDistance < lowest:
			lowest = wordDistance
			returning = word

	return returning

def LDM(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2
        
    a = 0
    b = 0
    c = 0
    
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                
                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    return distances[len(token1)][len(token2)]
