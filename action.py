#### goal ####
# to read the voice recording csv, compare it to actions csv, 
# and perform an action

import pandas as pd
import csv

testing = []
actions = []

def write_file_2():
    data1 = ['command','response']
    data2 = ['how are you', 'i am grand']
    data3 = ['what is your name', 'my name is cobot']
    data4 = ['hello','hi there']

    f = open("file2.csv", "w")
    f.truncate()
    f.close()

    with open('file2.csv','w',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data1)
        writer.writerow(data2)
        writer.writerow(data3)
        writer.writerow(data4)

    files = glob.glob('file*.csv')
    matches = []

    testing = pd.read_csv('file1.csv')
    actions = pd.read_csv('file2.csv')

    
    print_reply(testing,actions)
    return testing,actions


def print_reply(testing,actions,axis=1):
    index = 0
    for command in testing.command:
        for action in actions.command:
            if command == action:
                print(actions.response[index])
            index = index + 1
        index =0
