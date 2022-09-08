from collections import OrderedDict
import operator

scores = [4, 0, 2, 2, 1, 6]
animal_images = ['rat', 'cat', 'mouse', 'bear', 'moose', 'shark']

from collections import OrderedDict

dict1 = {}

dict1 = {animal_images[i]:scores[i] for i in range(len(animal_images))}

print(dict1)

dict1 = dict(sorted(dict1.items(), key=operator.itemgetter(1)))

list1 = list(dict1.keys())

print(dict1)
print(list1)






























