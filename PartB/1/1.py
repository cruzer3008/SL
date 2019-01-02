def c2k():
	celcius = int(input("Enter the temparature in Celcius\n"))
	return celcius+273
def k2c():
	kelvin = int(input("Enter the temperature in Kelvin\n"))
	return kelvin-273
def c2f():
	celcius = int(input("Enter the temperature in Celcuis\n"))
	return ((celcius*9)/5)+32
def f2c():
	fahrenheit = int(input("Enter the temperature in Fahrenheit\n"))
	return ((fahrenheit-32)*5)/9

choice = 0
while choice!=5:
	choice = int(input("Enter 1 to convert from Celcius to Kelvin\nEnter 2 to convert from Celcius to Kelvin\nEnter 3 to convert from Celcius to Fahrenheit\nEnter 4 to convert from Fahrenheit to Celcius\n"))
	if choice==1:
		print(c2k())
	elif choice == 2:
		print(k2c())
	elif choice == 3:
		print(c2f())
	elif choice == 4:
		print(f2c())
	elif choice == 5:
		exit()
