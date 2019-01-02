my_list = [1,2,3,4,5,6]
print("The list of numbers is: ",my_list)

newList = [x*3 for x in my_list]
print("The list after multiply each number by 3 is: ",newList)

or_sum = reduce(lambda x,y:x+y,my_list)
print("Original Sum: ",or_sum)

new_sum = reduce(lambda x,y:x+y,newList)
print("New Sum: ",new_sum)
