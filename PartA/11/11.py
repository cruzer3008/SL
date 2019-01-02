myList = ["Yash is my name 1203","Abdul 9 is my friend","Jamal is my best friend","Rafiq is my enemy","Taufin if an idiot","Pasha 89 is lol","Ajmal is killer","Osama is innocent","Mohd is funny"]
print(myList)
for i in range(len(myList)):
	if(i%2==0):
		print(myList[i])
	
for i in range(len(myList)):
	if(i%3==0):
		myList[i] = myList[i].upper()
print(myList)

for i in range(len(myList)):
	myList[i] = " ".join(reversed(myList[i].split()))
	print(myList[i])

num = []
for i in range(len(myList)):
	for s in myList[i].split():
		if s.isdigit():
			num.append(s)
print(num)
