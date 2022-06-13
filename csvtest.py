
import csv
import python3-pandas as pd

with open('file2.csv','w',encoding='UTF8') as f:
    data1 = ['command','response']
    data2 = ['how are you', 'i am grand']
    data3 = ['what is your name', 'my name is cobot']
    data4 = ['hello','hi there']

    writer = csv.writer(f)
    writer.writerow(data1)
    writer.writerow(data2)
    writer.writerow(data3)
    writer.writerow(data4)