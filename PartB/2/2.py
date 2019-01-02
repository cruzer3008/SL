import operator

class python_solution:
	def reverse(self,s):
		return " ".join(reversed(s.split()))
	def vowelCount(self,s):
		vowel = 0
		for i in range(len(s)):
			if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
				vowel=vowel+1
		return vowel

myDict = {}
sortedDict = {}

firstString = raw_input("Enter the first string\n")
firstStringReverse = python_solution().reverse(firstString)
firstStringCount = python_solution().vowelCount(firstString)
myDict[firstString] = firstStringCount

secondString = raw_input("Enter the second string\n")
secondStringReverse = python_solution().reverse(secondString)
secondStringCount = python_solution().vowelCount(secondString)
myDict[secondString] = secondStringCount

thirdString = raw_input("Enter the third string\n")
thirdStringReverse = python_solution().reverse(thirdString)
thirdStringCount = python_solution().vowelCount(thirdString)
myDict[thirdString] = thirdStringCount

sortedDict = sorted(myDict.items(),key = operator.itemgetter(1),reverse=True)
print(sortedDict)
