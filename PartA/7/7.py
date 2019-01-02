def atomic_dictionary():
	Atomic_elements = {"C":"Carbon","N":"Nitrogen","O":"Oxygen"}
	print(Atomic_elements)

	new_symbol = raw_input("Enter the symbol of the new element: ")

	new_element = raw_input("Enter the name of the new element: ")

	if new_symbol in Atomic_elements.keys():
		print("Element already exits")
	else:
		print("New entry added to the dictionary")


	Atomic_elements[new_symbol] = new_element
	print(Atomic_elements)

	print("The number of elements in the dictionary is:")
	print(len(Atomic_elements))

	key = raw_input("Enter the key of the element to be searched: ")
	if key in Atomic_elements.keys():
		print(Atomic_elements[key])
	else:
		print("Key does not exist in the dictionary")




