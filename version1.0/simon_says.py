import random

line = 'Speak'


if line == 'Speak':
    simon_says = ['move forward','turn green','turn yellow', 'move backwards', 'Spin']
    action = random.randint(1,3)
    pick = random.randint(0,4)
    if action % 2 == 0:
        say = simon_says[pick]
    else:
        say = 'Simon Says ' + simon_says[pick]

print(say)