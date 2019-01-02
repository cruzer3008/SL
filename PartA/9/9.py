class Student:
	name = ""
	age = 0
	marks = []

	def __init__(self,x,y,l):
		self.name = x
		self.age = y
		self.marks = l

	def accept(self):
		self.name = raw_input("Enter name: ")
		self.age = raw_input("Enter age: ")
		print("Enter the marks of three subjects")
		l = raw_input()
		l = l.split(" ")
		x = []
		for i in range(len(l)):
			x.append(int(l[i]))
		self.marks = x
	def disp(self):
		print(self.name)
		print(self.age)
		print(self.marks)


s1 = Student("Yash",20,[100,90,85])
s1.disp()

s2 = Student('sanj',23,[60,82,75])
s2.disp()
s2.accept()
s2.disp()

