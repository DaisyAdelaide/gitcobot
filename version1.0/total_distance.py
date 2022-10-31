import pandas as pd
import csv
import math

data = pd.read_csv('PositionData.csv')
df = pd.DataFrame(data)
total_rotations = 0

for i in range(len(df)):
	total_rotations += df.iloc[i][0]

total_distance = (total_rotations/3.44) * (163*math.pi) / 1000000
total_distance = round(total_distance, 3)

print('The total distance travelled is: ' + str(total_distance) + ' km')