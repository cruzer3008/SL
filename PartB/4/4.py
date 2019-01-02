from collections import Counter
from functools import reduce
import operator

def word_count(fname):
	with open(fname) as f:
		return Counter(f.read().split())
myDict = dict(word_count('myFile.txt'))
print(myDict)	

sortedDict = {}
sortedDict = sorted(myDict.items(),key=operator.itemgetter(1),reverse=True)
print(sortedDict)
words = [x[0] for x in sortedDict][0:10]
print(words)

numbers = [x[1] for x in sortedDict]
avg_length = reduce(lambda x,y:x+y,numbers)/len(numbers)
print("The avg length is ",avg_length)

squares = [x*x for x in numbers]
print("Squares ",squares)


