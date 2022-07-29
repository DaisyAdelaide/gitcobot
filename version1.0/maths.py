numbers = []
operations = []

operation = ('/', '+', '-', '*')

text = '20 + 2 * 10 + 10 / 50 - 51 * 8 / 7'

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
    
    return str(answer)

def check_if_maths(text):
    global operation, numbers
    
    for x in text.split(' '):
        if x.isdigit():
            numbers.append(x)
        for expression in operation:
            if expression == x:
                operations.append(x)
    if len(operations) > 0:
        return True
    
if check_if_maths(text):
    print(maths())
    